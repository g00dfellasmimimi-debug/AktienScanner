import streamlit as st
from stocks import detail_info, top_trend_aktien
from config import AKTIEN
from scoring import berechne_score

st.title("AktienScanner")

ticker = st.text_input("Ticker", "NVDA")

if st.button("Firmeninfo"):
    info = detail_info(ticker)

    st.subheader(info["name"])

    st.write(f"Aktueller Preis: ${info['preis']}")
    st.write(f"52W Hoch: ${info['hoch']}")
    st.write(f"52W Tief: ${info['tief']}")

from stocks import lade_daten

if st.button("Chart anzeigen"):
    data = lade_daten(ticker)

    if not data.empty:
        st.line_chart(data["Close"])

st.header("🔥 Top Trend Aktien")

if st.button("Top 10 berechnen"):
    st.write("Top 10 werden geladen...")

    aktien = AKTIEN

    ergebnisse = []

    st.write("Berechne Top 10...")

    for ticker in aktien[:5]:
        st.write(f"Lade: {ticker}")

        data = lade_daten(ticker)

        st.write(f"Daten erhalten: {ticker}")

        if data.empty:
            continue

        st.write(ticker)
        st.write(data["Close"].tail(1))
