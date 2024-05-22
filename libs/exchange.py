from binance.spot import Spot as Client


def check_login(public_key, private_key):
    client = Client(public_key, private_key, base_url="https://testnet.binance.vision")
    try:
        client.account(self=client)
        return client
    except:
        return False


def balanceOf(client, symbol):
    account = Client.account(self=client)
    balances = account['balances']

    for balance in balances:
        if balance['asset'] == symbol:
            return (float)(balance['free'])


# #Check Order
def checkOrder(client, symbol, side):
    check = False
    order = client.get_orders(symbol=symbol, limit=1)

    if order:
        last_order = order[0]
        if last_order['status'] == 'FILLED':
            check = True
            return check

        else:
            check = False
            return check


# Take Buy Order
def takeBuyOrder(client, symbol, side, quantity):
    # quantity = round(round(balanceOf("USDT"),-1)/(float)(client.ticker_price(symbol=f"{symbol}USDT")['price']),1)
    symbol = f"{symbol}USDT"

    order = client.new_order(symbol=symbol, quantity=quantity, side=side, type='MARKET')


def takeSellOrder(client, symbol, side, quantity):
    # quantity = round(balanceOf(symbol)-0.1,1)
    symbol = f"{symbol}USDT"

    order = client.new_order(symbol="BTCUSDT", quantity=quantity, side=side, type='MARKET')
