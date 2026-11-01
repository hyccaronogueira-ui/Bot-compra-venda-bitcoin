import websocket
import ssl
import json

def ao_abrir(ws):
    print("Conexão aberta com o WebSocket do Bitstamp.")
    json_subscribe = {
        "event": "bts:subscribe",
        "data": {
            "channel": "live_trades_btcusd"
        }
    }
    ws.send(json.dumps(json_subscribe))

def ao_fechar(ws, close_status_code, close_msg):
    print("Conexão fechada com o WebSocket do Bitstamp.")

def error(ws, error):
    print("Erro no WebSocket do Bitstamp.")
    print(error)

def ao_receber_mensagem(ws, message):
    mensagem = json.loads(message)
    if mensagem.get('event') != 'trade':
        return
    price = mensagem['data']['price']
    print(f"Preço da última transação: {price}")

    if price > 9000:
        vender()
    elif price < 8100:
        comprar()
    else:
        print("Preço dentro da faixa de negociação. Nenhuma ação tomada.")

def comprar():
    pass  # Função de compra ainda não implementada
def vender():
    pass  # Função de venda ainda não implementada



if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net",
                                on_open=ao_abrir,
                                on_close=ao_fechar,
                                on_error=error,
                                on_message=ao_receber_mensagem)
    ws.run_forever()