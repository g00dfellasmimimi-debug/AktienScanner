import customtkinter as ctk
import yfinance as yf

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def lade_aktien():

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

    ausgabe.delete("1.0", "end")
    ausgabe.insert("end", "Analysiere Aktien...\n")

    app.update()

    ergebnisse = []

    for ticker in aktien:
        try:
            data = yf.download(ticker, period="1mo", auto_adjust=True, progress=False)

            if data.empty:
                continue

            endkurs = data[("Close", ticker)].iloc[-1]

            kurs_30 = (
                (data[("Close", ticker)].iloc[-1] - data[("Close", ticker)].iloc[0])
                / data[("Close", ticker)].iloc[0]
            ) * 100

            kurs_7 = (
                (data[("Close", ticker)].iloc[-1] - data[("Close", ticker)].iloc[-5])
                / data[("Close", ticker)].iloc[-5]
            ) * 100

            aenderung = kurs_30

            volumen = data[("Volume", ticker)].mean()

            score = kurs_30 * 0.7 + kurs_7 * 0.3 + (volumen / 20000000)
            ergebnisse.append(
                {
                    "ticker": ticker,
                    "kurs": endkurs,
                    "aenderung": aenderung,
                    "score": score,
                }
            )

        except Exception as e:
            print(f"Fehler bei {ticker}: {e}")

    ergebnisse.sort(key=lambda x: x["score"], reverse=True)

    ausgabe.delete("1.0", "end")
    ausgabe.insert("end", "TOP 10 TREND AKTIEN\n\n")

    for i, aktie in enumerate(ergebnisse[:10], start=1):
        symbol = "🟢" if aktie["aenderung"] >= 0 else "🔴"

        ausgabe.insert(
            "end",
            f"{symbol} "
            f"{i:2d}. "
            f"{aktie['ticker']:6s} "
            f"Preis: ${aktie['kurs']:8.2f} "
            f"Änd.: {aktie['aenderung']:6.2f}% "
            f"Score: {aktie['score']:6.2f}\n",
        )


app = ctk.CTk()
app.geometry("800x600")
app.title("Trend Aktien Scanner")

titel = ctk.CTkLabel(app, text="Top Trend Aktien", font=("Arial", 24))

titel.pack(pady=20)

button = ctk.CTkButton(app, text="Aktien analysieren", command=lade_aktien)

button.pack(pady=10)

ausgabe = ctk.CTkTextbox(app, width=700, height=400)

ausgabe.pack(pady=20)

app.mainloop()
