import pandas as pd

def calculate_sma(df, window=20):
    """
    Calculates Simple Moving Average (SMA).
    """
    df[f'SMA_{window}'] = df['Close'].rolling(window=window).mean()
    return df

def calculate_ema(df, window=20):
    """
    Calculates Exponential Moving Average (EMA).
    """
    df[f'EMA_{window}'] = df['Close'].ewm(span=window, adjust=False).mean()
    return df
