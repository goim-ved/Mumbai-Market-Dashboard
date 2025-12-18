# Mumbai Market Dashboard 

A professional, real-time stock tracking dashboard for the NIFTY 50 index, built with Python and Streamlit. This application combines powerful technical analysis tools with a premium, glassmorphism-inspired user interface.

<img width="2558" height="1298" alt="Screenshot 2025-12-18 205732" src="https://github.com/user-attachments/assets/467dad44-6eef-4518-a076-9e4d72c7f8a8" />

## Features

-   **Real-Time Market Data**: Fetches live data for all NIFTY 50 stocks using the Yahoo Finance API.
-   **Interactive Charts**: High-performance, interactive candlestick charts powered by Plotly.
-   **Technical Analysis**: Built-in Simple Moving Average (SMA) and Exponential Moving Average (EMA) indicators with customizable windows.
-   **Premium UI/UX**:
    -   **Glassmorphism Design**: Modern, translucent card aesthetics.
    -   **Dark Theme**: Sleek, eye-friendly dark mode with subtle gradients.
    -   **Responsive Layout**: Optimized for various screen sizes.
-   **Customizable Timeframes**: flexible period and interval selection (e.g., 1D, 1W, 1M).

## Tech Stack

-   **Frontend**: [Streamlit](https://streamlit.io/)
-   **Data Source**: [yfinance](https://pypi.org/project/yfinance/)
-   **Visualization**: [Plotly](https://plotly.com/python/)
-   **Data Processing**: [Pandas](https://pandas.pydata.org/) & [NumPy](https://numpy.org/)
-   **Styling**: Custom CSS3

## Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/mumbai-market-dashboard.git
    cd mumbai-market-dashboard
    ```

2.  **Create a virtual environment (Optional but recommended)**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

The dashboard will open automatically in your default web browser at `http://localhost:8501`.

### How to use:
1.  **Select Stock**: Choose any NIFTY 50 stock from the sidebar dropdown.
2.  **Adjust Timeframe**: Set your desired historical period (e.g., "1y") and interval (e.g., "1d").
3.  **Add Indicators**: Toggle SMA or EMA checkboxes in the sidebar and adjust the window sizes to analyze trends.

## Project Structure

```
mumbai-market-dashboard/
├── app.py              # Main application entry point
├── data_loader.py      # Data fetching and caching logic
├── indicators.py       # Technical indicator calculations
├── style.css           # Custom CSS for glassmorphism theme
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## Note

This application uses the `yfinance` library, which provides market data that may have a slight delay. It is intended for educational and analytical purposes, not for high-frequency trading.

---

Built with ❤️ by Vedant Goim
