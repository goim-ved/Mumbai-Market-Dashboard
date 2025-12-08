import yfinance as yf
import pandas as pd

ticker = "ADANIENT.NS"
data = yf.download(ticker, period="1mo", interval="1d", progress=False)

print("Columns:", data.columns)
print("Type of columns:", type(data.columns))
if isinstance(data.columns, pd.MultiIndex):
    print("MultiIndex levels:", data.columns.levels)

try:
    close = data['Close']
    print("data['Close'] type:", type(close))
    print("data['Close'] head:\n", close.head())
    
    last_close = close.iloc[-1]
    print("last_close type:", type(last_close))
    print("last_close value:\n", last_close)
    
    print(f"Formatted: {last_close:.2f}")
except Exception as e:
    print(f"Error: {e}")
