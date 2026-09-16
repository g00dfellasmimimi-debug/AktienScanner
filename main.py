import yfinance as yf

aktien = [
    "AAPL",
    "MSFT",
    "NVDA",
    "TSLA",
    "META",
    "AMD",
    "AMZN",
    "GOOGL",
    "NFLX",
    "PLTR",
    "AVGO",
    "INTC",
    "MU",
    "QCOM",
    "CRM",
    "ADBE",
    "SNOW",
    "SHOP",
    "UBER",
    "ASML",
    "TXN",
    "AMAT",
    "PANW",
    "CRWD",
    "MSTR",
    "COIN",
    "ARM",
    "SMCI",
    "RDDT",
    "NET",
    "ZS",
    "DDOG",
    "TEAM",
    "MDB",
    "NOW",
    "SHOP",
    "PYPL",
    "XYZ",
    "ROKU",
    "DOCU",
    "BABA",
    "NIO",
    "LI",
    "XPEV",
    "SOFI",
    "HOOD",
    "RBLX",
    "FUBO",
    "IONQ",
    "RKLB",
]

ergebnisse = []

for ticker in aktien:
    try:
        data = yf.download(ticker, period="1mo", auto_adjust=True, progress=False)

        startkurs = data[("Close", ticker)].iloc[0]
        endkurs = data[("Close", ticker)].iloc[-1]

        aenderung = ((endkurs - startkurs) / startkurs) * 100

        volumen = data[("Volume", ticker)].mean()

        score = aenderung + (volumen / 10000000)

        ergebnisse.append(
            {"ticker": ticker, "kurs": endkurs, "aenderung": aenderung, "score": score}
        )

    except Exception as e:
        print(f"Fehler bei {ticker}: {e}")

ergebnisse = sorted(ergebnisse, key=lambda x: x["score"], reverse=True)

print("\nTOP 10 TREND-AKTIEN\n")

for i, aktie in enumerate(ergebnisse[:10], start=1):
    print(
        f"{i:2d}. "
        f"{aktie['ticker']:6s} "
        f"Preis: ${aktie['kurs']:7.2f} "
        f"Änd.: {aktie['aenderung']:6.2f}% "
        f"Score: {aktie['score']:6.2f}\n"
    )
