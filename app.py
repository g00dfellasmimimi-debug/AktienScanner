import streamlit as st

from stocks import detail_info
from stocks import lade_daten
from stocks import top_trend_aktien

st.title("AktienScanner")

ticker = st.text_input("Ticker", "NVDA")

if st.button("Firmeninfo"):
    info = detail_info(ticker)

    st.subheader(info["name"])

    st.write(f"Aktueller Preis: ${info['preis']}")
    st.write(f"52W Hoch: ${info['hoch']}")
    st.write(f"52W Tief: ${info['tief']}")

if st.button("Chart anzeigen"):
    data = lade_daten(ticker)

    if not data.empty:
        st.line_chart(data["Close"])

st.header("🔥 Top Trend Aktien")

for platz, (ticker, aenderung) in enumerate(top_trend_aktien(), start=1):
    st.write(f"{platz}. {ticker}: {aenderung:.2f}%")
