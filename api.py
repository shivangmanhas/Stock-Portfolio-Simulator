import yfinance as yf
import pandas as pd

# List of tickers
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'NVDA']

# Date range
start_date = '2020-01-01'
end_date = '2025-01-01'

# List to hold each ticker's DataFrame
all_data = []

for ticker in tickers:
    df = yf.download(ticker, start=start_date, end=end_date)
    df = df.reset_index()
    df['Ticker'] = ticker  # Add a column for ticker
    all_data.append(df)

# Concatenate all into a single DataFrame
portfolio_df = pd.concat(all_data, ignore_index=True)

# Optional: round numeric columns for cleaner export
portfolio_df = portfolio_df.round(2)

# Export to CSV with proper encoding and delimiter
portfolio_df.to_csv("portfolio_data.csv", index=False, encoding='utf-8')

print("✅ Clean data saved to 'portfolio_data.csv'")




