# Bot de Trading de Bitcoin (Bitstamp)

Bot em Python que acompanha o preço do Bitcoin (BTC/USD) em tempo real pelo WebSocket da [Bitstamp](https://www.bitstamp.net/) e, de acordo com uma faixa de preço definida, compra ou vende a mercado.

> ⚠️ **Aviso:** projeto educacional feito para fins de aprendizado em ambiente controlado. Operar criptomoedas envolve risco de perda financeira. O bot vem em **modo simulação** por padrão, sem enviar ordens reais. Nada aqui é recomendação de investimento.

## Como funciona

1. Conecta ao WebSocket da Bitstamp e assina o canal `live_trades_btcusd`.
2. A cada negociação recebida, lê o preço da última transação.
3. Se o preço estiver **acima** do limite de venda, vende; se estiver **abaixo** do limite de compra, compra; entre os dois, não faz nada.
4. Um intervalo mínimo entre ordens evita disparos repetidos.

## Configuração

Os parâmetros ficam no topo de `bot_bitcoin.py`:

| Parâmetro | Descrição |
|---|---|
| `PRECO_VENDA` | Vende acima deste preço |
| `PRECO_COMPRA` | Compra abaixo deste preço |
| `QUANTIDADE` | Quantidade de BTC por ordem |
| `INTERVALO_MINIMO` | Segundos mínimos entre ordens |
| `SIMULACAO` | `True` = não envia ordens reais |

**Ajuste os preços de compra e venda para valores coerentes com o mercado atual**, senão o bot vai agir em todas as negociações.

### Credenciais

As credenciais da Bitstamp são lidas de variáveis de ambiente e **nunca devem ser colocadas no código nem enviadas ao GitHub**.

**Windows (PowerShell):**

```powershell
$env:BITSTAMP_USERNAME="seu_usuario"
$env:BITSTAMP_KEY="sua_chave"
$env:BITSTAMP_SECRET="seu_secret"
```

**Linux / macOS:**

```bash
export BITSTAMP_USERNAME="seu_usuario"
export BITSTAMP_KEY="sua_chave"
export BITSTAMP_SECRET="seu_secret"
```

## Como executar

```bash
git clone https://github.com/hyccaronogueira-ui/Bot-compra-venda-bitcoin.git
cd Bot-compra-venda-bitcoin

python -m venv venv
# Windows: venv\Scripts\Activate.ps1
# Linux/macOS: source venv/bin/activate

pip install -r requirements.txt
python bot_bitcoin.py
```

## Tecnologias

- Python 3.10+
- [websocket-client](https://pypi.org/project/websocket-client/)
- [bitstamp-python-client](https://pypi.org/project/bitstamp-python-client/)

## Autor

**whoami** — [@whoami-root](https://github.com/wh0am1-root)
