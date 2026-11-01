import json
import os
import time

import bitstamp.client
import websocket


PRECO_VENDA = 9000          
PRECO_COMPRA = 8100         
QUANTIDADE = 0.001          
INTERVALO_MINIMO = 60       
SIMULACAO = True            


USERNAME = os.environ.get("BITSTAMP_USERNAME")
KEY = os.environ.get("BITSTAMP_KEY")
SECRET = os.environ.get("BITSTAMP_SECRET")

estado = {"ultima_ordem": 0.0}


def cliente():
    return bitstamp.client.Trading(username=USERNAME, key=KEY, secret=SECRET)


def comprar(quantidade):
    if SIMULACAO:
        print(f"[SIMULAÇÃO] Compraria {quantidade} BTC a mercado.")
        return
    cliente().buy_market_order(amount=quantidade)
    print(f"Ordem de COMPRA enviada: {quantidade} BTC.")


def vender(quantidade):
    if SIMULACAO:
        print(f"[SIMULAÇÃO] Venderia {quantidade} BTC a mercado.")
        return
    cliente().sell_market_order(amount=quantidade)
    print(f"Ordem de VENDA enviada: {quantidade} BTC.")


def ao_abrir(ws):
    print("Conexão aberta com o WebSocket do Bitstamp.")
    ws.send(json.dumps({
        "event": "bts:subscribe",
        "data": {"channel": "live_trades_btcusd"},
    }))


def ao_fechar(ws, close_status_code, close_msg):
    print("Conexão fechada com o WebSocket do Bitstamp.")


def ao_errar(ws, erro):
    print(f"Erro no WebSocket do Bitstamp: {erro}")


def ao_receber_mensagem(ws, message):
    mensagem = json.loads(message)
    if mensagem.get("event") != "trade":
        return

    preco = float(mensagem["data"]["price"])
    print(f"Preço da última transação: {preco}")

    if preco > PRECO_VENDA:
        acao = vender
    elif preco < PRECO_COMPRA:
        acao = comprar
    else:
        print("Preço dentro da faixa de negociação. Nenhuma ação tomada.")
        return

    # Evita disparar uma ordem a cada trade recebido
    agora = time.time()
    if agora - estado["ultima_ordem"] < INTERVALO_MINIMO:
        print("Ordem recente já enviada. Aguardando intervalo mínimo.")
        return

    try:
        acao(QUANTIDADE)
        estado["ultima_ordem"] = agora
    except Exception as e:
        print(f"Falha ao enviar ordem: {e}")


if __name__ == "__main__":
    ws = websocket.WebSocketApp(
        "wss://ws.bitstamp.net",
        on_open=ao_abrir,
        on_close=ao_fechar,
        on_error=ao_errar,
        on_message=ao_receber_mensagem,
    )
    ws.run_forever()
