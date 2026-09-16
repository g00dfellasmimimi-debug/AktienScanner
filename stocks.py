import yfinance as yf


def lade_daten(ticker):

    data = yf.download(ticker, period="1mo", auto_adjust=True, progress=False)

    return data
