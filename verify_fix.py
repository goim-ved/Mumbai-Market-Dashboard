from data_loader import get_nifty50_data
import pandas as pd

ticker = "ADANIENT.NS"
print(f"Fetching data for {ticker}...")
df = get_nifty50_data(ticker, period="1mo", interval="1d")

print("Columns:", df.columns)
print("Type of columns:", type(df.columns))

if isinstance(df.columns, pd.MultiIndex):
    print("FAIL: Columns are still MultiIndex")
else:
    print("SUCCESS: Columns are flattened")

try:
    current_price = df['Close'].iloc[-1]
    print(f"Current Price type: {type(current_price)}")
    print(f"Current Price value: {current_price}")
    print(f"Formatted: {current_price:.2f}")
    print("SUCCESS: Formatting worked")
except Exception as e:
    print(f"FAIL: Error accessing/formatting price: {e}")
