import customtkinter as ctk
from stocks import lade_daten
from scoring import berechne_score
from stocks import firmeninfo
from stocks import detail_info

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def zeige_info():

    ticker = ticker_eingabe.get().upper()

    if ticker == "":
        return

    name, preis = firmeninfo(ticker)

    ausgabe.delete("1.0", "end")

    ausgabe.insert("end", f"{name}\n\n")

    ausgabe.insert("end", f"Aktueller Preis: ${preis}\n")


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
            data = lade_daten(ticker)

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

            score = berechne_score(kurs_30, kurs_7, volumen)
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


def zeige_chart():

    ticker = ticker_eingabe.get().upper()

    if ticker == "":
        return

    import matplotlib.pyplot as plt

    data = lade_daten(ticker)

    if data.empty:
        return
    plt.close("all")
    data[("Close", ticker)].plot()

    plt.title(f"{ticker} - Kursverlauf")
    plt.grid(True)
    plt.show(block=False)


def zeige_details():

    ticker = ticker_eingabe.get().upper()

    if not ticker:
        return

    info = detail_info(ticker)

    ausgabe.delete("1.0", "end")

    ausgabe.insert(
        "end",
        f"{info['name']}\n\n"
        f"Preis: ${info['preis']}\n"
        f"52W Hoch: ${info['hoch']}\n"
        f"52W Tief: ${info['tief']}\n"
        f"Market Cap: {info['marketcap']}\n"
        f"Volumen: {info['volume']}\n",
    )


app = ctk.CTk()
app.geometry("800x600")
app.title("Trend Aktien Scanner")

titel = ctk.CTkLabel(app, text="Top Trend Aktien", font=("Arial", 24))

titel.pack(pady=20)

ticker_eingabe = ctk.CTkEntry(app, width=200, placeholder_text="Ticker z.B. NVDA")

ticker_eingabe.pack(pady=10)
button = ctk.CTkButton(app, text="Aktien analysieren", command=lade_aktien)
chart_button = ctk.CTkButton(app, text="Chart anzeigen", command=zeige_chart)

chart_button.pack(pady=10)
info_button = ctk.CTkButton(app, text="Firmeninfo", command=zeige_info)

info_button.pack(pady=10)
button.pack(pady=10)
detail_button = ctk.CTkButton(app, text="Details", command=zeige_details)

detail_button.pack(pady=10)
ausgabe = ctk.CTkTextbox(app, width=700, height=400)

ausgabe.pack(pady=20)

app.mainloop()
