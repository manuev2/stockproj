from coinbase.wallet.client import Client
import config
def dataextraction():
    client = Client(config.api_key, config.api_secret)
    #Historical Data Object
    hist = client.get_historic_prices(currency_pair='ETH-USD', period='all')
    #Retrieve prices from Historical Object
    data = getattr(hist, 'prices')
    return data