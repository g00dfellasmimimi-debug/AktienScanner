import streamlit as st

from stocks import detail_info
from stocks import lade_daten
from stocks import top_trend_aktien

st.title("AktienScanner")

ticker = st.text_input("Ticker", "NVDA")

periode = st.selectbox("Zeitraum", ["1mo", "3mo", "6mo", "1y"])

if st.button("Firmeninfo"):
    info = detail_info(ticker)

    st.subheader(info["name"])

    st.write(f"Aktueller Preis: ${info['preis']}")
    st.write(f"52W Hoch: ${info['hoch']}")
    st.write(f"52W Tief: ${info['tief']}")

if st.button("Chart anzeigen"):
    data = lade_daten(ticker, periode)

    if not data.empty:
        st.line_chart(data["Close"])

st.header("🔥 Top Trend Aktien")

for platz, (ticker, aenderung) in enumerate(top_trend_aktien(periode), start=1):
    if aenderung >= 0:
        st.success(f"{platz}. {ticker}: {aenderung:.2f}%")
    else:
        st.error(f"{platz}. {ticker}: {aenderung:.2f}%")
