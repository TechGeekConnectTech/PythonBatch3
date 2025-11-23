"""
AREA CHART EXAMPLE - Trends and Cumulative Values
=================================================
Area charts show trends over time and cumulative effects.
Use cases: Portfolio growth, market share evolution, cumulative sales, etc.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load datasets
stock_df = pd.read_csv('Day14/stock_market_data.csv')
sales_df = pd.read_csv('Day14/sales_data.csv')
weather_df = pd.read_csv('Day14/weather_data.csv')

print("AREA CHART EXAMPLE: Trends and Cumulative Analysis")
print("=" * 50)

# Prepare data
stock_df['Date'] = pd.to_datetime(stock_df['Date'])
weather_df['Date'] = pd.to_datetime(weather_df['Date'])

# Create figure with multiple area chart types
plt.figure(figsize=(15, 12))

# 1. Basic Area Chart - Stock Price Trend
plt.subplot(2, 3, 1)
reliance_data = stock_df[stock_df['Company'] == 'RELIANCE'].sort_values('Date')

plt.fill_between(reliance_data['Date'], reliance_data['Close'], 
                alpha=0.6, color='skyblue', label='Stock Price')
plt.plot(reliance_data['Date'], reliance_data['Close'], 
         color='blue', linewidth=2)

plt.title('RELIANCE Stock Price Trend', fontsize=14, fontweight='bold')
plt.xlabel('Date')
plt.ylabel('Price (₹)')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.legend()

# 2. Multiple Area Chart - Stock Portfolio Value
plt.subplot(2, 3, 2)
companies = ['RELIANCE', 'TCS', 'INFY']
colors = ['lightblue', 'lightgreen', 'lightcoral']

# Get common date range
min_date = stock_df['Date'].min()
max_date = stock_df['Date'].max()
date_range = pd.date_range(min_date, max_date, freq='D')

# Normalize prices to show relative performance (base = 100)
for i, (company, color) in enumerate(zip(companies, colors)):
    company_data = stock_df[stock_df['Company'] == company].sort_values('Date')
    
    # Normalize to starting price = 100
    normalized_price = (company_data['Close'] / company_data['Close'].iloc[0]) * 100
    
    plt.fill_between(company_data['Date'], normalized_price,
                    alpha=0.4, color=color, label=company)
    plt.plot(company_data['Date'], normalized_price,
            color=color.replace('light', ''), linewidth=2)

plt.title('Stock Performance Comparison\n(Normalized to 100)', fontsize=14, fontweight='bold')
plt.xlabel('Date')
plt.ylabel('Normalized Price')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, alpha=0.3)

# 3. Stacked Area Chart - Monthly Sales by Product
plt.subplot(2, 3, 3)

# Prepare monthly sales data
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_pivot = sales_df.groupby(['Month', 'Product'])['Sales_Units'].sum().unstack().fillna(0)
sales_pivot = sales_pivot.reindex(month_order)

# Create stacked area chart
plt.stackplot(sales_pivot.index, 
             sales_pivot['Smartphones'], sales_pivot['Laptops'], 
             sales_pivot['Tablets'], sales_pivot['Headphones'], sales_pivot['Watches'],
             labels=['Smartphones', 'Laptops', 'Tablets', 'Headphones', 'Watches'],
             colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57'],
             alpha=0.8)

plt.title('Monthly Sales Distribution\n(Stacked by Product)', fontsize=14, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Sales Units')
plt.xticks(rotation=45)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# 4. Area Chart with Confidence Interval - Temperature Trends
plt.subplot(2, 3, 4)

# Calculate monthly average temperature with confidence interval
mumbai_weather = weather_df[weather_df['City'] == 'Mumbai'].copy()
mumbai_weather['Month'] = mumbai_weather['Date'].dt.month

monthly_temp_stats = mumbai_weather.groupby('Month')['Temperature'].agg(['mean', 'std']).reset_index()
monthly_temp_stats['upper'] = monthly_temp_stats['mean'] + monthly_temp_stats['std']
monthly_temp_stats['lower'] = monthly_temp_stats['mean'] - monthly_temp_stats['std']

months = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']

# Plot confidence interval
plt.fill_between(monthly_temp_stats['Month'], monthly_temp_stats['lower'], 
                monthly_temp_stats['upper'], alpha=0.3, color='orange', 
                label='±1 Std Dev')

# Plot mean line
plt.plot(monthly_temp_stats['Month'], monthly_temp_stats['mean'], 
         color='red', linewidth=3, label='Mean Temperature')

plt.title('Mumbai Temperature Variation\n(with Confidence Interval)', fontsize=14, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(monthly_temp_stats['Month'], months)
plt.legend()
plt.grid(True, alpha=0.3)

# 5. Cumulative Area Chart - Portfolio Growth Simulation
plt.subplot(2, 3, 5)

# Simulate portfolio performance
np.random.seed(42)
days = 250
initial_investment = 100000

# Three investment strategies
conservative_returns = np.random.normal(0.0003, 0.01, days)  # Conservative
moderate_returns = np.random.normal(0.0005, 0.015, days)     # Moderate
aggressive_returns = np.random.normal(0.0008, 0.025, days)   # Aggressive

# Calculate cumulative portfolio values
conservative_value = initial_investment * np.cumprod(1 + conservative_returns)
moderate_value = initial_investment * np.cumprod(1 + moderate_returns)
aggressive_value = initial_investment * np.cumprod(1 + aggressive_returns)

dates = pd.date_range('2023-01-01', periods=days, freq='D')

# Plot cumulative performance
plt.fill_between(dates, 0, conservative_value, alpha=0.4, color='green', label='Conservative')
plt.fill_between(dates, conservative_value, moderate_value, alpha=0.4, color='orange', label='Moderate')
plt.fill_between(dates, moderate_value, aggressive_value, alpha=0.4, color='red', label='Aggressive')

plt.title('Investment Portfolio Growth\n(Cumulative Performance)', fontsize=14, fontweight='bold')
plt.xlabel('Date')
plt.ylabel('Portfolio Value (₹)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, alpha=0.3)

# Format y-axis to show values in lakhs
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x/100000:.1f}L'))

# 6. Streamgraph - Regional Sales Evolution
plt.subplot(2, 3, 6)

# Create monthly regional data
sales_df['Period'] = sales_df['Year'].astype(str) + '-' + sales_df['Month']
period_order = []
for year in [2022, 2023]:
    for month in month_order:
        period_order.append(f'{year}-{month}')

regional_sales = sales_df.groupby(['Period', 'Region'])['Sales_Units'].sum().unstack().fillna(0)
regional_sales = regional_sales.reindex(period_order).fillna(0)

# Create streamgraph (centered stacked area)
baseline = regional_sales.sum(axis=1) / 2

# Calculate cumulative values for centering
cumulative = regional_sales.cumsum(axis=1)
centered_data = []

for i, region in enumerate(regional_sales.columns):
    if i == 0:
        bottom = baseline - cumulative.iloc[:, i] / 2
        top = baseline + cumulative.iloc[:, i] / 2
    else:
        bottom = baseline - cumulative.iloc[:, i-1] - regional_sales.iloc[:, i] / 2
        top = baseline - cumulative.iloc[:, i-1] + regional_sales.iloc[:, i] / 2
    
    centered_data.append((bottom, top))

# Plot streamgraph
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57']
x_positions = range(len(regional_sales.index))

for i, (region, color) in enumerate(zip(regional_sales.columns, colors)):
    bottom, top = centered_data[i]
    plt.fill_between(x_positions, bottom, top, alpha=0.7, color=color, label=region)

plt.title('Regional Sales Evolution\n(Streamgraph)', fontsize=14, fontweight='bold')
plt.xlabel('Time Period')
plt.ylabel('Sales Distribution')
plt.xticks(range(0, len(period_order), 6), [period_order[i] for i in range(0, len(period_order), 6)], rotation=45)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.savefig('Day14/07_area_chart_example.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n📊 KEY LEARNING POINTS:")
print("• Area charts emphasize the magnitude of change over time")
print("• Fill area under line to show volume/cumulative effect")
print("• Stacked areas show part-to-whole relationships over time")
print("• Multiple areas can compare different series")
print("• Confidence intervals show uncertainty ranges")
print("• Streamgraphs create flowing, organic visualizations")

# Analysis Summary
print(f"\n📈 TREND INSIGHTS:")

# Stock performance analysis
print("Stock Performance Summary (Normalized):")
for company in companies:
    company_data = stock_df[stock_df['Company'] == company].sort_values('Date')
    start_price = company_data['Close'].iloc[0]
    end_price = company_data['Close'].iloc[-1]
    total_return = ((end_price - start_price) / start_price) * 100
    print(f"  • {company}: {total_return:+.1f}% total return")

# Sales seasonality analysis
print(f"\nSales Seasonality Analysis:")
monthly_totals = sales_df.groupby('Month')['Sales_Units'].sum()
peak_month = monthly_totals.idxmax()
low_month = monthly_totals.idxmin()
seasonality = ((monthly_totals.max() - monthly_totals.min()) / monthly_totals.mean()) * 100

print(f"  • Peak sales month: {peak_month} ({monthly_totals[peak_month]:,} units)")
print(f"  • Lowest sales month: {low_month} ({monthly_totals[low_month]:,} units)")
print(f"  • Seasonality factor: {seasonality:.1f}% variation from mean")

# Temperature variation analysis
print(f"\nTemperature Variation (Mumbai):")
temp_variation = mumbai_weather.groupby(mumbai_weather['Date'].dt.month)['Temperature'].agg(['min', 'max', 'mean'])
max_variation_month = (temp_variation['max'] - temp_variation['min']).idxmax()
most_stable_month = (temp_variation['max'] - temp_variation['min']).idxmin()

print(f"  • Most variable month: {max_variation_month} ({temp_variation.loc[max_variation_month, 'max'] - temp_variation.loc[max_variation_month, 'min']:.1f}°C range)")
print(f"  • Most stable month: {most_stable_month} ({temp_variation.loc[most_stable_month, 'max'] - temp_variation.loc[most_stable_month, 'min']:.1f}°C range)")

print(f"\n✓ Chart saved as: Day14/07_area_chart_example.png")