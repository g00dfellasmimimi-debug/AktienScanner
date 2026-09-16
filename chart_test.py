import yfinance as yf
import matplotlib.pyplot as plt

ticker = "NVDA"

data = yf.download(ticker, period="6mo", auto_adjust=True, progress=False)

data[("Close", ticker)].plot()

plt.title("NVDA - 6 Monate")
plt.grid(True)
plt.show()
