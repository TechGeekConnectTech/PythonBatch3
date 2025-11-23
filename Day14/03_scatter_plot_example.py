"""
SCATTER PLOT EXAMPLE - Correlation Analysis
===========================================
Scatter plots show relationships between two continuous variables.
Use cases: Price vs Volume, Temperature vs Humidity, Performance correlations, etc.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load multiple datasets
stock_df = pd.read_csv('Day14/stock_market_data.csv')
sales_df = pd.read_csv('Day14/sales_data.csv')
student_df = pd.read_csv('Day14/student_grades.csv')

print("SCATTER PLOT EXAMPLE: Correlation Analysis")
print("=" * 50)

# Create figure with multiple scatter plots
plt.figure(figsize=(15, 12))

# 1. Basic Scatter Plot - Stock Price vs Volume
plt.subplot(2, 3, 1)
reliance_data = stock_df[stock_df['Company'] == 'RELIANCE']
plt.scatter(reliance_data['Volume'], reliance_data['Close'], 
           alpha=0.6, color='blue', s=50)
plt.title('RELIANCE: Stock Price vs Trading Volume', fontsize=14, fontweight='bold')
plt.xlabel('Trading Volume')
plt.ylabel('Closing Price (₹)')
plt.grid(True, alpha=0.3)

# Add correlation coefficient
correlation = reliance_data['Volume'].corr(reliance_data['Close'])
plt.text(0.05, 0.95, f'Correlation: {correlation:.3f}', 
         transform=plt.gca().transAxes, bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))

# 2. Colored Scatter Plot - Sales Units vs Revenue by Product
plt.subplot(2, 3, 2)
products = sales_df['Product'].unique()
colors = ['red', 'blue', 'green', 'orange', 'purple']

for product, color in zip(products, colors):
    product_data = sales_df[sales_df['Product'] == product]
    plt.scatter(product_data['Sales_Units'], product_data['Revenue'], 
               label=product, alpha=0.7, s=60, color=color)

plt.title('Sales Units vs Revenue by Product', fontsize=14, fontweight='bold')
plt.xlabel('Sales Units')
plt.ylabel('Revenue (₹)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)

# 3. Size-coded Scatter Plot - Student Performance Analysis
plt.subplot(2, 3, 3)
# Calculate average marks by student
student_avg = student_df.groupby('Student_ID').agg({
    'Marks': 'mean',
    'Attendance': 'first'
}).reset_index()

# Use marks as color and attendance as size
scatter = plt.scatter(student_avg['Attendance'], student_avg['Marks'], 
                     c=student_avg['Marks'], s=student_avg['Attendance']*100, 
                     alpha=0.6, cmap='RdYlGn', edgecolors='black', linewidth=0.5)

plt.title('Student Performance: Attendance vs Marks', fontsize=14, fontweight='bold')
plt.xlabel('Attendance Rate')
plt.ylabel('Average Marks')
plt.colorbar(scatter, label='Average Marks')
plt.grid(True, alpha=0.3)

# 4. Multiple Series Scatter Plot - Stock Returns Comparison
plt.subplot(2, 3, 4)
companies = ['RELIANCE', 'TCS', 'INFY', 'HDFC']
colors = ['blue', 'green', 'red', 'orange']

for company, color in zip(companies, colors):
    company_data = stock_df[stock_df['Company'] == company]
    plt.scatter(company_data['Daily_Return'], company_data['Volume']/1000, 
               label=company, alpha=0.6, s=30, color=color)

plt.title('Daily Returns vs Volume (All Companies)', fontsize=14, fontweight='bold')
plt.xlabel('Daily Return (%)')
plt.ylabel('Volume (Thousands)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.axvline(x=0, color='black', linestyle='--', alpha=0.5)  # Zero return line

# 5. Trend Line Scatter Plot - Sales Performance with Trend
plt.subplot(2, 3, 5)
# Calculate monthly total sales
monthly_sales = sales_df.groupby(['Year', 'Month']).agg({
    'Sales_Units': 'sum',
    'Revenue': 'sum'
}).reset_index()

# Create a month number for plotting
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_sales['Month_Num'] = monthly_sales['Month'].map(lambda x: month_order.index(x) + 1)
monthly_sales['Period'] = (monthly_sales['Year'] - 2022) * 12 + monthly_sales['Month_Num']

plt.scatter(monthly_sales['Sales_Units'], monthly_sales['Revenue'], 
           alpha=0.7, s=80, color='purple', edgecolors='black', linewidth=1)

# Add trend line
z = np.polyfit(monthly_sales['Sales_Units'], monthly_sales['Revenue'], 1)
p = np.poly1d(z)
plt.plot(monthly_sales['Sales_Units'], p(monthly_sales['Sales_Units']), 
         "r--", alpha=0.8, linewidth=2, label=f'Trend Line')

plt.title('Monthly Sales: Units vs Revenue with Trend', fontsize=14, fontweight='bold')
plt.xlabel('Total Sales Units')
plt.ylabel('Total Revenue (₹)')
plt.legend()
plt.grid(True, alpha=0.3)

# 6. Bubble Chart - Three Variables
plt.subplot(2, 3, 6)
# Regional performance analysis
regional_perf = sales_df.groupby('Region').agg({
    'Sales_Units': 'sum',
    'Revenue': 'sum',
    'Profit_Margin': 'mean'
}).reset_index()

bubble_sizes = regional_perf['Revenue'] / 50000  # Scale for visibility

scatter = plt.scatter(regional_perf['Sales_Units'], regional_perf['Profit_Margin'], 
                     s=bubble_sizes, alpha=0.6, c=regional_perf['Revenue'], 
                     cmap='plasma', edgecolors='black', linewidth=1)

plt.title('Regional Performance Bubble Chart', fontsize=14, fontweight='bold')
plt.xlabel('Total Sales Units')
plt.ylabel('Average Profit Margin')
plt.colorbar(scatter, label='Total Revenue (₹)')

# Add region labels
for i, region in enumerate(regional_perf['Region']):
    plt.annotate(region, 
                (regional_perf['Sales_Units'].iloc[i], regional_perf['Profit_Margin'].iloc[i]),
                xytext=(5, 5), textcoords='offset points', fontsize=10, fontweight='bold')

plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('Day14/03_scatter_plot_example.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n📊 KEY LEARNING POINTS:")
print("• Scatter plots reveal relationships between variables")
print("• Positive correlation: points trend upward")
print("• Negative correlation: points trend downward")
print("• No correlation: points scattered randomly")
print("• Use color/size to encode additional dimensions")
print("• Add trend lines to highlight relationships")

# Statistical Analysis
print(f"\n📈 CORRELATION INSIGHTS:")

# Stock analysis
stock_correlations = []
for company in stock_df['Company'].unique():
    company_data = stock_df[stock_df['Company'] == company]
    corr = company_data['Volume'].corr(company_data['Close'])
    stock_correlations.append((company, corr))

print("Stock Price-Volume Correlations:")
for company, corr in sorted(stock_correlations, key=lambda x: abs(x[1]), reverse=True):
    print(f"  • {company}: {corr:.3f}")

# Student performance correlation
attendance_marks_corr = student_avg['Attendance'].corr(student_avg['Marks'])
print(f"\nStudent Attendance-Marks Correlation: {attendance_marks_corr:.3f}")

# Sales correlation
sales_revenue_corr = monthly_sales['Sales_Units'].corr(monthly_sales['Revenue'])
print(f"Sales Units-Revenue Correlation: {sales_revenue_corr:.3f}")

print(f"\n✓ Chart saved as: Day14/03_scatter_plot_example.png")