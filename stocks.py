import yfinance as yf


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


from config import AKTIEN


def top_trend_aktien(periode="1mo"):

    ergebnis = []

    for ticker in AKTIEN:
        data = lade_daten(ticker, periode)

        if data.empty:
            continue

        start = float(data["Close"].iloc[0].iloc[0])
        ende = float(data["Close"].iloc[-1].iloc[0])

        aenderung = ((ende - start) / start) * 100

        ergebnis.append((ticker, aenderung))

    ergebnis.sort(key=lambda x: x[1], reverse=True)
    print(ergebnis)
    return ergebnis


def lade_daten(ticker, periode="1mo"):

    return yf.download(ticker, period=periode, auto_adjust=True, progress=False)
