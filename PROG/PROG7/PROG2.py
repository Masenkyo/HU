def tickersToDict(filename):
    result = {}
    with open(filename, 'r') as ticks:
        for i in ticks:
            items = i.strip().split(':')
            name, symbol = items
            result[name] = symbol
    return result

def nameToSymbol(name, tickerDict):
    return tickerDict.get(name)

def symbolToName(symbol, tickerDict):
    return [name for name, tick in tickerDict.items() if tick == symbol]

print(tickersToDict('tickers.txt'))
tickers = tickersToDict('tickers.txt')

name = input('Enter Company name: ')
print("Ticker symbol: {}".format(nameToSymbol(name, tickers)))

symbol = input('Enter Ticker symbol: ')
print("Company name: {}".format(symbolToName(symbol, tickers)))