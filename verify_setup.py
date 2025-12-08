import sys
import os

sys.path.append(os.getcwd())

try:
    print("Testing imports...")
    import streamlit
    import yfinance
    import pandas
    import plotly
    import numpy
    from data_loader import get_nifty50_data, NIFTY50_TICKERS
    from indicators import calculate_sma, calculate_ema
    print("Imports successful.")

    print("Testing data fetching...")
    ticker = NIFTY50_TICKERS[0]
    df = get_nifty50_data(ticker, period="5d", interval="1d")
    if df.empty:
        print(f"Warning: No data fetched for {ticker}")
    else:
        print(f"Data fetched for {ticker}: {len(df)} rows")
        
        print("Testing indicators...")
        df = calculate_sma(df, window=2)
        df = calculate_ema(df, window=2)
        
        if 'SMA_2' in df.columns and 'EMA_2' in df.columns:
            print("Indicators calculated successfully.")
        else:
            print("Error: Indicators not found in dataframe.")

    print("Verification complete.")

except Exception as e:
    print(f"Verification failed: {e}")
    sys.exit(1)
