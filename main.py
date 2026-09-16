from config import AKTIEN
from stocks import lade_daten
from scoring import berechne_score

aktien = AKTIEN

ergebnisse = []

for ticker in aktien:
    try:
        data = lade_daten(ticker)

        if data.empty:
            continue

        startkurs = data[("Close", ticker)].iloc[0]
        endkurs = data[("Close", ticker)].iloc[-1]

        kurs_30 = ((endkurs - startkurs) / startkurs) * 100

        kurs_7 = (
            (data[("Close", ticker)].iloc[-1] - data[("Close", ticker)].iloc[-5])
            / data[("Close", ticker)].iloc[-5]
        ) * 100

        volumen = data[("Volume", ticker)].mean()

        score = berechne_score(kurs_30, kurs_7, volumen)

        ergebnisse.append(
            {"ticker": ticker, "kurs": endkurs, "aenderung": kurs_30, "score": score}
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
        f"Score: {aktie['score']:6.2f}"
    )
