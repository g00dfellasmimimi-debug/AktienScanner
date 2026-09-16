import yfinance as yf


def lade_daten(ticker):

    return yf.download(ticker, period="1mo", auto_adjust=True, progress=False)


def firmeninfo(ticker):

    aktie = yf.Ticker(ticker)

    return (aktie.info.get("longName", ticker), aktie.info.get("currentPrice", 0))


def detail_info(ticker):

    aktie = yf.Ticker(ticker)

    info = aktie.info

    return {
        "name": info.get("longName", "Unbekannt"),
        "preis": info.get("currentPrice", 0),
        "hoch": info.get("fiftyTwoWeekHigh", 0),
        "tief": info.get("fiftyTwoWeekLow", 0),
        "marketcap": info.get("marketCap", 0),
        "volume": info.get("averageVolume", 0),
    }


def top_trend_aktien():

    return ["NVDA", "META", "MSFT", "AAPL", "TSLA"]
