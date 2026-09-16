import yfinance as yf


def lade_daten(ticker):

    return yf.download(ticker, period="1mo", auto_adjust=True, progress=False)


def firmeninfo(ticker):

    aktie = yf.Ticker(ticker)

    return (aktie.info.get("longName", ticker), aktie.info.get("currentPrice", 0))

    return data
