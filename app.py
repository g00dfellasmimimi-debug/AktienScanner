import streamlit as st
from stocks import detail_info

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
