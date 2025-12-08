import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from data_loader import get_nifty50_data, NIFTY50_TICKERS
from indicators import calculate_sma, calculate_ema

st.set_page_config(page_title="Mumbai Market Dashboard", layout="wide")

st.title("Mumbai Market Dashboard 📈")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.sidebar.header("Settings")
selected_ticker = st.sidebar.selectbox("Select Stock", NIFTY50_TICKERS)
period = st.sidebar.selectbox("Period", ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"], index=2)
interval = st.sidebar.selectbox("Interval", ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"], index=8)

st.sidebar.subheader("Technical Indicators")
show_sma = st.sidebar.checkbox("SMA")
sma_window = st.sidebar.number_input("SMA Window", min_value=1, value=20)
show_ema = st.sidebar.checkbox("EMA")
ema_window = st.sidebar.number_input("EMA Window", min_value=1, value=20)

if selected_ticker:
    with st.spinner(f"Loading data for {selected_ticker}..."):
        df = get_nifty50_data(selected_ticker, period=period, interval=interval)
        
        if not df.empty:
            current_price = df['Close'].iloc[-1]
            previous_price = df['Close'].iloc[-2] if len(df) > 1 else current_price
            price_change = current_price - previous_price
            percent_change = (price_change / previous_price) * 100
            
            delta_class = "positive" if price_change >= 0 else "negative"
            delta_sign = "+" if price_change >= 0 else ""
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">Current Price</div>
                    <div class="metric-value">₹{current_price:,.2f}</div>
                </div>
                """, unsafe_allow_html=True)
                
            with col2:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">Change</div>
                    <div class="metric-value metric-delta {delta_class}">
                        {delta_sign}{price_change:.2f}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
            with col3:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">Percent Change</div>
                    <div class="metric-value metric-delta {delta_class}">
                        {delta_sign}{percent_change:.2f}%
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown('<div class="chart-container">', unsafe_allow_html=True)
            fig = go.Figure()
            
            fig.add_trace(go.Candlestick(x=df.index,
                            open=df['Open'],
                            high=df['High'],
                            low=df['Low'],
                            close=df['Close'],
                            name='Price'))
            
            if show_sma:
                df = calculate_sma(df, window=sma_window)
                fig.add_trace(go.Scatter(x=df.index, y=df[f'SMA_{sma_window}'], 
                                         mode='lines', name=f'SMA {sma_window}',
                                         line=dict(color='#00ff88', width=2)))
                
            if show_ema:
                df = calculate_ema(df, window=ema_window)
                fig.add_trace(go.Scatter(x=df.index, y=df[f'EMA_{ema_window}'], 
                                         mode='lines', name=f'EMA {ema_window}',
                                         line=dict(color='#00ccff', width=2)))

            fig.update_layout(
                title=dict(text=f"{selected_ticker} Price Chart", font=dict(color="white", size=20)),
                xaxis=dict(
                    title="Date", 
                    color="white", 
                    showgrid=False, 
                    zeroline=False
                ),
                yaxis=dict(
                    title="Price", 
                    color="white", 
                    showgrid=True, 
                    gridcolor="rgba(255,255,255,0.1)",
                    zeroline=False
                ),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color="white"),
                height=600,
                margin=dict(l=40, r=40, t=60, b=40),
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                )
            )
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.subheader("Historical Data")
            st.dataframe(df.tail(), use_container_width=True)
            
        else:
            st.error("No data found for the selected ticker.")
