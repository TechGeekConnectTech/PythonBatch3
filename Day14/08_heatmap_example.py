"""
HEATMAP EXAMPLE - Correlation and Pattern Analysis
=================================================
Heatmaps show relationships in matrix form using colors.
Use cases: Correlation matrices, confusion matrices, time patterns, etc.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

# Set seaborn style
sns.set_style("whitegrid")
try:
    plt.style.use('seaborn-v0_8')
except:
    plt.style.use('default')

# Load datasets
stock_df = pd.read_csv('Day14/stock_market_data.csv')
student_df = pd.read_csv('Day14/student_grades.csv')
sales_df = pd.read_csv('Day14/sales_data.csv')
weather_df = pd.read_csv('Day14/weather_data.csv')

print("HEATMAP EXAMPLE: Correlation and Pattern Analysis")
print("=" * 50)

# Create figure with multiple heatmap types
plt.figure(figsize=(18, 12))

# 1. Correlation Matrix Heatmap - Stock Market Data
plt.subplot(2, 3, 1)

# Create correlation matrix for stock data
stock_correlation_data = []
for company in stock_df['Company'].unique():
    company_data = stock_df[stock_df['Company'] == company]
    stock_correlation_data.append(company_data['Close'].values[:min(500, len(company_data))])

# Create DataFrame for correlation
stock_corr_df = pd.DataFrame(dict(zip(stock_df['Company'].unique(), stock_correlation_data)))
correlation_matrix = stock_corr_df.corr()

# Create heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='RdYlBu_r', center=0,
           square=True, linewidths=0.5, cbar_kws={"shrink": .8}, fmt='.3f')

plt.title('Stock Price Correlation Matrix', fontsize=14, fontweight='bold')
plt.xlabel('Companies')
plt.ylabel('Companies')

# 2. Performance Heatmap - Student Grades by Subject and Class
plt.subplot(2, 3, 2)

# Create pivot table for student performance
student_performance = student_df.groupby(['Class', 'Subject'])['Marks'].mean().unstack()

# Create heatmap
sns.heatmap(student_performance, annot=True, cmap='RdYlGn', 
           linewidths=0.5, cbar_kws={"shrink": .8}, fmt='.1f')

plt.title('Average Marks by Class & Subject', fontsize=14, fontweight='bold')
plt.xlabel('Subject')
plt.ylabel('Class')

# 3. Sales Heatmap - Product Performance by Region and Time
plt.subplot(2, 3, 3)

# Create pivot table for sales
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_pivot = sales_df.groupby(['Month', 'Product'])['Sales_Units'].sum().unstack()
sales_pivot = sales_pivot.reindex(month_order)

# Create heatmap
sns.heatmap(sales_pivot, annot=True, cmap='Blues', 
           linewidths=0.5, cbar_kws={"shrink": .8}, fmt='.0f')

plt.title('Sales Units by Month & Product', fontsize=14, fontweight='bold')
plt.xlabel('Product')
plt.ylabel('Month')

# 4. Custom Color Heatmap - Weather Patterns by City and Month
plt.subplot(2, 3, 4)

# Prepare weather data
weather_df['Date'] = pd.to_datetime(weather_df['Date'])
weather_df['Month'] = weather_df['Date'].dt.month

# Create pivot table for temperature
weather_pivot = weather_df.groupby(['Month', 'City'])['Temperature'].mean().unstack()

# Create custom heatmap
sns.heatmap(weather_pivot, annot=True, cmap='coolwarm', center=25,
           linewidths=0.5, cbar_kws={"shrink": .8, "label": "Temperature (°C)"}, fmt='.1f')

plt.title('Average Temperature by Month & City', fontsize=14, fontweight='bold')
plt.xlabel('City')
plt.ylabel('Month')

# 5. Binary Heatmap - High Performance Analysis
plt.subplot(2, 3, 5)

# Create binary matrix for high performers (marks >= 85)
student_high_perf = student_df.groupby(['Subject', 'Class'])['Marks'].apply(lambda x: (x >= 85).mean()).unstack()

# Create heatmap
sns.heatmap(student_high_perf, annot=True, cmap='Reds', 
           linewidths=0.5, cbar_kws={"shrink": .8, "label": "Proportion"}, fmt='.2f')

plt.title('High Performers Proportion\n(Marks ≥ 85)', fontsize=14, fontweight='bold')
plt.xlabel('Class')
plt.ylabel('Subject')

# 6. Hierarchical Clustered Heatmap - Regional Sales Patterns
plt.subplot(2, 3, 6)

# Create comprehensive sales matrix
sales_matrix = sales_df.groupby(['Region', 'Product'])['Sales_Units'].sum().unstack().fillna(0)

# Create clustered heatmap
sns.heatmap(sales_matrix, annot=True, cmap='viridis', 
           linewidths=0.5, cbar_kws={"shrink": .8}, fmt='.0f')

plt.title('Sales Matrix by Region & Product', fontsize=14, fontweight='bold')
plt.xlabel('Product')
plt.ylabel('Region')

plt.tight_layout()
plt.savefig('Day14/08_heatmap_example.png', dpi=300, bbox_inches='tight')
plt.show()

# Create additional specialized heatmaps
plt.figure(figsize=(15, 10))

# 7. Time Series Heatmap - Daily Trading Volume Patterns
plt.subplot(2, 2, 1)

# Prepare time series data
reliance_data = stock_df[stock_df['Company'] == 'RELIANCE'].copy()
reliance_data['Date'] = pd.to_datetime(reliance_data['Date'])
reliance_data['Month'] = reliance_data['Date'].dt.month
reliance_data['DayOfWeek'] = reliance_data['Date'].dt.dayofweek

# Create volume heatmap by month and day of week
volume_patterns = reliance_data.groupby(['Month', 'DayOfWeek'])['Volume'].mean().unstack()
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
volume_patterns.columns = days

sns.heatmap(volume_patterns, annot=True, cmap='plasma', 
           linewidths=0.5, fmt='.0f', cbar_kws={"label": "Average Volume"})

plt.title('RELIANCE Trading Volume Patterns\n(Month vs Day of Week)', fontsize=12, fontweight='bold')
plt.xlabel('Day of Week')
plt.ylabel('Month')

# 8. Diverging Heatmap - Stock Returns Above/Below Average
plt.subplot(2, 2, 2)

# Calculate returns deviation from company average
returns_deviation = []
companies = ['RELIANCE', 'TCS', 'INFY', 'HDFC']

for company in companies:
    company_data = stock_df[stock_df['Company'] == company]
    avg_return = company_data['Daily_Return'].mean()
    deviation = company_data['Daily_Return'] - avg_return
    returns_deviation.append(deviation.iloc[:50])  # First 50 days

returns_df = pd.DataFrame(dict(zip(companies, returns_deviation)))
returns_corr = returns_df.corr()

sns.heatmap(returns_corr, annot=True, cmap='RdBu_r', center=0,
           square=True, linewidths=0.5, fmt='.3f')

plt.title('Returns Correlation Matrix\n(Deviation from Mean)', fontsize=12, fontweight='bold')

# 9. Missing Data Heatmap - Data Quality Visualization
plt.subplot(2, 2, 3)

# Create sample data with missing values
sample_data = student_df.sample(100).copy()
# Introduce random missing values
np.random.seed(42)
for col in ['Marks', 'Attendance']:
    missing_indices = np.random.choice(sample_data.index, size=int(len(sample_data)*0.1), replace=False)
    sample_data.loc[missing_indices, col] = np.nan

# Visualize missing data pattern
sns.heatmap(sample_data.isnull(), cbar=True, yticklabels=False, 
           cmap='viridis_r', cbar_kws={"label": "Missing Data"})

plt.title('Missing Data Pattern\n(Sample Student Data)', fontsize=12, fontweight='bold')
plt.xlabel('Columns')
plt.ylabel('Records')

# 10. Custom Annotation Heatmap - Performance Categories
plt.subplot(2, 2, 4)

# Create performance categories
performance_categories = sales_df.groupby(['Region', 'Product']).agg({
    'Sales_Units': 'sum',
    'Revenue': 'sum'
}).reset_index()

performance_categories['Performance'] = pd.cut(performance_categories['Sales_Units'], 
                                             bins=3, labels=['Low', 'Medium', 'High'])

# Create categorical heatmap
perf_matrix = performance_categories.groupby(['Region', 'Product'])['Performance'].first().unstack()

# Convert categories to numbers for heatmap
perf_numeric = perf_matrix.replace({'Low': 1, 'Medium': 2, 'High': 3}).astype(float)

sns.heatmap(perf_numeric, annot=perf_matrix.values, cmap='RdYlGn', 
           linewidths=0.5, fmt='', cbar_kws={"label": "Performance Level"})

plt.title('Performance Categories\n(Region vs Product)', fontsize=12, fontweight='bold')
plt.xlabel('Product')
plt.ylabel('Region')

plt.tight_layout()
plt.savefig('Day14/08b_advanced_heatmaps.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n📊 KEY LEARNING POINTS:")
print("• Heatmaps use color intensity to represent data values")
print("• Perfect for showing correlations and patterns in matrices")
print("• Color scales should match data type (diverging, sequential)")
print("• Annotations help with precise value reading")
print("• Clustering can reveal hidden patterns")
print("• Missing data patterns can be visualized effectively")

# Analysis Summary
print(f"\n📈 PATTERN INSIGHTS:")

# Stock correlation insights
print("Stock Correlation Analysis:")
corr_series = correlation_matrix.unstack().drop_duplicates()
max_corr_pair = corr_series.nlargest(2).iloc[1]
companies_pair = corr_series.nlargest(2).index[1]
print(f"  • Highest correlation: {companies_pair[0]} & {companies_pair[1]} ({max_corr_pair:.3f})")

# Student performance insights
print(f"\nStudent Performance Insights:")
best_subject_class = student_performance.unstack().idxmax()
worst_subject_class = student_performance.unstack().idxmin()
print(f"  • Best performance: {best_subject_class[1]} in {best_subject_class[0]} ({student_performance.unstack().max():.1f} marks)")
print(f"  • Needs improvement: {worst_subject_class[1]} in {worst_subject_class[0]} ({student_performance.unstack().min():.1f} marks)")

# Sales pattern insights
print(f"\nSales Pattern Analysis:")
peak_sales = sales_pivot.unstack().idxmax()
low_sales = sales_pivot.unstack().idxmin()
print(f"  • Peak sales: {peak_sales[1]} in {peak_sales[0]} ({sales_pivot.unstack().max():,} units)")
print(f"  • Lowest sales: {low_sales[1]} in {low_sales[0]} ({sales_pivot.unstack().min():,} units)")

# Weather pattern insights
print(f"\nWeather Pattern Insights:")
hottest = weather_pivot.unstack().idxmax()
coolest = weather_pivot.unstack().idxmin()
print(f"  • Hottest: {hottest[1]} in month {hottest[0]} ({weather_pivot.unstack().max():.1f}°C)")
print(f"  • Coolest: {coolest[1]} in month {coolest[0]} ({weather_pivot.unstack().min():.1f}°C)")

print(f"\n✓ Charts saved as: Day14/08_heatmap_example.png & Day14/08b_advanced_heatmaps.png")