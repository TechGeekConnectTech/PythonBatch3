    """
BAR CHART EXAMPLE - Sales Analysis
==================================
Bar charts are perfect for comparing categories.
Use cases: Sales by region, product performance, survey results, etc.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load sales data
df = pd.read_csv('Day14/sales_data.csv')

print("BAR CHART EXAMPLE: Sales Analysis")
print("=" * 50)
print(f"Analyzing sales data with {len(df)} records")

# Create the figure
plt.figure(figsize=(15, 10))

# 1. Vertical Bar Chart - Sales by Product
plt.subplot(2, 3, 1)
product_sales = df.groupby('Product')['Sales_Units'].sum().sort_values(ascending=False)
bars = plt.bar(product_sales.index, product_sales.values, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57'])
plt.title('Total Sales by Product', fontsize=14, fontweight='bold')
plt.ylabel('Sales Units')
plt.xticks(rotation=45)
# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 100,
             f'{int(height):,}', ha='center', va='bottom', fontweight='bold')

# 2. Horizontal Bar Chart - Sales by Region
plt.subplot(2, 3, 2)
region_sales = df.groupby('Region')['Revenue'].sum().sort_values()
bars = plt.barh(region_sales.index, region_sales.values, color='lightcoral')
plt.title('Total Revenue by Region', fontsize=14, fontweight='bold')
plt.xlabel('Revenue (₹)')
# Add value labels
for i, v in enumerate(region_sales.values):
    plt.text(v + 100000, i, f'₹{v/1000000:.1f}M', va='center', fontweight='bold')

# 3. Grouped Bar Chart - Sales by Product and Year
plt.subplot(2, 3, 3)
yearly_product_sales = df.groupby(['Year', 'Product'])['Sales_Units'].sum().unstack()
x = np.arange(len(yearly_product_sales.columns))
width = 0.35

plt.bar(x - width/2, yearly_product_sales.loc[2022], width, label='2022', color='skyblue', alpha=0.8)
plt.bar(x + width/2, yearly_product_sales.loc[2023], width, label='2023', color='orange', alpha=0.8)

plt.title('Sales Comparison: 2022 vs 2023', fontsize=14, fontweight='bold')
plt.ylabel('Sales Units')
plt.xlabel('Products')
plt.xticks(x, yearly_product_sales.columns, rotation=45)
plt.legend()

# 4. Stacked Bar Chart - Revenue by Region and Product
plt.subplot(2, 3, 4)
revenue_pivot = df.groupby(['Region', 'Product'])['Revenue'].sum().unstack()
revenue_pivot.plot(kind='bar', stacked=True, ax=plt.gca(), colormap='Set3')
plt.title('Revenue Distribution by Region & Product', fontsize=14, fontweight='bold')
plt.ylabel('Revenue (₹)')
plt.xlabel('Region')
plt.xticks(rotation=45)
plt.legend(title='Product', bbox_to_anchor=(1.05, 1), loc='upper left')

# 5. Bar Chart with Error Bars - Average Sales by Month
plt.subplot(2, 3, 5)
monthly_stats = df.groupby('Month')['Sales_Units'].agg(['mean', 'std'])
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.bar(months, monthly_stats['mean'], yerr=monthly_stats['std'], 
        capsize=5, color='lightgreen', alpha=0.7, error_kw={'color': 'red', 'linewidth': 2})
plt.title('Average Monthly Sales (with Std Dev)', fontsize=14, fontweight='bold')
plt.ylabel('Average Sales Units')
plt.xlabel('Month')
plt.xticks(rotation=45)

# 6. Top 10 Performance - Best Product-Region Combinations
plt.subplot(2, 3, 6)
product_region_perf = df.groupby(['Product', 'Region'])['Revenue'].sum().sort_values(ascending=False).head(10)
labels = [f"{prod}\n({region})" for (prod, region) in product_region_perf.index]

bars = plt.bar(range(len(labels)), product_region_perf.values, 
               color=plt.cm.viridis(np.linspace(0, 1, len(labels))))
plt.title('Top 10: Product-Region Performance', fontsize=14, fontweight='bold')
plt.ylabel('Revenue (₹)')
plt.xlabel('Product-Region Combination')
plt.xticks(range(len(labels)), labels, rotation=45, ha='right')

# Format y-axis to show values in millions
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x/1000000:.1f}M'))

plt.tight_layout()
plt.savefig('Day14/02_bar_chart_example.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n📊 KEY LEARNING POINTS:")
print("• Vertical bars: Good for comparing categories")
print("• Horizontal bars: Better when category names are long")
print("• Grouped bars: Compare multiple series across categories")
print("• Stacked bars: Show part-to-whole relationships")
print("• Error bars: Display uncertainty or variability")
print("• Color coding: Use colors to distinguish categories")

# Additional Analysis
print(f"\n📈 SALES INSIGHTS:")
top_product = product_sales.index[0]
top_revenue_region = region_sales.index[-1]
print(f"• Best-selling product: {top_product} ({product_sales.iloc[0]:,} units)")
print(f"• Highest revenue region: {top_revenue_region} (₹{region_sales.iloc[-1]/1000000:.1f}M)")

seasonal_sales = df.groupby('Month')['Sales_Units'].mean()
best_month = seasonal_sales.idxmax()
worst_month = seasonal_sales.idxmin()
print(f"• Best performing month: {best_month}")
print(f"• Lowest performing month: {worst_month}")

print(f"\n✓ Chart saved as: Day14/02_bar_chart_example.png")