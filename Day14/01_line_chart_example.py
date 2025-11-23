"""
LINE CHART EXAMPLE - Stock Price Trends
==========================================
Line charts are perfect for showing trends over time.
Use cases: Stock prices, temperature changes, sales growth, etc.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load stock market data
df = pd.read_csv('Day14/stock_market_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Filter data for one company
reliance_data = df[df['Company'] == 'RELIANCE'].copy()
reliance_data = reliance_data.sort_values('Date')

print("LINE CHART EXAMPLE: Stock Price Trends")
print("=" * 50)
print(f"Plotting stock price trend for RELIANCE")
print(f"Data points: {len(reliance_data)}")
print(f"Date range: {reliance_data['Date'].min()} to {reliance_data['Date'].max()}")

# Create the figure and axis
plt.figure(figsize=(12, 8))

# Plot closing price trend
plt.subplot(2, 2, 1)
plt.plot(reliance_data['Date'], reliance_data['Close'], 
         color='blue', linewidth=2, label='Closing Price')
plt.title('RELIANCE Stock - Closing Price Trend', fontsize=14, fontweight='bold')
plt.xlabel('Date')
plt.ylabel('Price (₹)')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.legend()

# Plot multiple lines (OHLC)
plt.subplot(2, 2, 2)
plt.plot(reliance_data['Date'], reliance_data['Open'], color='green', label='Open', alpha=0.7)
plt.plot(reliance_data['Date'], reliance_data['High'], color='red', label='High', alpha=0.7)
plt.plot(reliance_data['Date'], reliance_data['Low'], color='orange', label='Low', alpha=0.7)
plt.plot(reliance_data['Date'], reliance_data['Close'], color='blue', label='Close', linewidth=2)
plt.title('RELIANCE Stock - OHLC Prices', fontsize=14, fontweight='bold')
plt.xlabel('Date')
plt.ylabel('Price (₹)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, alpha=0.3)

# Compare multiple companies
plt.subplot(2, 2, 3)
companies = ['RELIANCE', 'TCS', 'INFY']
colors = ['blue', 'green', 'red']

for company, color in zip(companies, colors):
    company_data = df[df['Company'] == company].sort_values('Date')
    plt.plot(company_data['Date'], company_data['Close'], 
             color=color, label=company, linewidth=2)

plt.title('Stock Price Comparison - Multiple Companies', fontsize=14, fontweight='bold')
plt.xlabel('Date')
plt.ylabel('Price (₹)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, alpha=0.3)

# Stock returns over time
plt.subplot(2, 2, 4)
reliance_data['Cumulative_Return'] = (1 + reliance_data['Daily_Return']/100).cumprod()
plt.plot(reliance_data['Date'], reliance_data['Cumulative_Return'], 
         color='purple', linewidth=2)
plt.title('RELIANCE - Cumulative Returns', fontsize=14, fontweight='bold')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

# Adjust layout and save
plt.tight_layout()
plt.savefig('Day14/01_line_chart_example.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n📊 KEY LEARNING POINTS:")
print("• Line charts show continuous data over time")
print("• Perfect for trends, patterns, and time series data")
print("• Can compare multiple series on same plot")
print("• Use different colors/styles to distinguish lines")
print("• Add grid and labels for better readability")

print(f"\n✓ Chart saved as: Day14/01_line_chart_example.png")