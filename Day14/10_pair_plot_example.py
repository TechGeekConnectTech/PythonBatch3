"""
PAIR PLOT EXAMPLE - Multi-variable Relationship Analysis
=======================================================
Pair plots show relationships between all pairs of numerical variables.
Use cases: Exploratory data analysis, feature correlation, pattern discovery, etc.
"""

import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

# Set seaborn style
sns.set_style("whitegrid")
plt.rcParams['figure.facecolor'] = 'white'

# Load and prepare datasets
stock_df = pd.read_csv('Day14/stock_market_data.csv')
student_df = pd.read_csv('Day14/student_grades.csv')
weather_df = pd.read_csv('Day14/weather_data.csv')

print("PAIR PLOT EXAMPLE: Multi-variable Relationship Analysis")
print("=" * 50)

# 1. Basic Pair Plot - Stock Market Analysis
print("\n1. Creating Stock Market Pair Plot...")

# Prepare RELIANCE stock data with technical indicators
reliance_data = stock_df[stock_df['Company'] == 'RELIANCE'].copy().head(200)  # Limit for performance
reliance_data['Price_Range'] = reliance_data['High'] - reliance_data['Low']
reliance_data['Volume_MA'] = reliance_data['Volume'].rolling(window=5).mean()
reliance_data['Volatility'] = reliance_data['Daily_Return'].rolling(window=10).std()
reliance_data = reliance_data.dropna()

# Create pair plot for stock analysis
stock_features = ['Close', 'Volume', 'Daily_Return', 'Price_Range', 'Volatility']
stock_plot_data = reliance_data[stock_features]

plt.figure(figsize=(12, 10))
pair_plot = sns.pairplot(stock_plot_data, diag_kind='hist', plot_kws={'alpha': 0.6})
pair_plot.fig.suptitle('RELIANCE Stock - Multi-variable Analysis', y=1.02, fontsize=16, fontweight='bold')
plt.savefig('Day14/10a_stock_pairplot.png', dpi=300, bbox_inches='tight')
plt.show()

# 2. Categorical Pair Plot - Student Performance Analysis
print("\n2. Creating Student Performance Pair Plot...")

# Prepare student data with performance metrics
student_analysis = student_df.copy()

# Calculate student-level metrics
student_metrics = student_analysis.groupby('Student_ID').agg({
    'Marks': ['mean', 'std'],
    'Attendance': 'first',
    'Gender': 'first'
}).reset_index()

student_metrics.columns = ['Student_ID', 'Avg_Marks', 'Marks_Std', 'Attendance', 'Gender']
student_metrics['Performance_Consistency'] = 1 / (1 + student_metrics['Marks_Std'])  # Higher = more consistent

# Create performance categories
student_metrics['Performance_Level'] = pd.cut(student_metrics['Avg_Marks'], 
                                             bins=[0, 60, 75, 85, 100], 
                                             labels=['Below Average', 'Average', 'Good', 'Excellent'])

# Sample data for performance
student_sample = student_metrics.sample(min(150, len(student_metrics)))

plt.figure(figsize=(12, 10))
pair_plot = sns.pairplot(student_sample, 
                        vars=['Avg_Marks', 'Marks_Std', 'Attendance', 'Performance_Consistency'],
                        hue='Gender', 
                        diag_kind='kde',
                        plot_kws={'alpha': 0.7})
pair_plot.fig.suptitle('Student Performance - Multi-dimensional Analysis', y=1.02, fontsize=16, fontweight='bold')
plt.savefig('Day14/10b_student_pairplot.png', dpi=300, bbox_inches='tight')
plt.show()

# 3. Weather Pattern Analysis Pair Plot
print("\n3. Creating Weather Pattern Pair Plot...")

# Prepare weather data with derived features
weather_analysis = weather_df.copy()
weather_analysis['Date'] = pd.to_datetime(weather_analysis['Date'])
weather_analysis['Month'] = weather_analysis['Date'].dt.month

# Create seasonal categories
def get_season(month):
    if month in [12, 1, 2]: return 'Winter'
    elif month in [3, 4, 5]: return 'Spring'  
    elif month in [6, 7, 8]: return 'Summer'
    else: return 'Autumn'

weather_analysis['Season'] = weather_analysis['Month'].apply(get_season)

# Calculate comfort index and other metrics
weather_analysis['Heat_Index'] = weather_analysis['Temperature'] + (weather_analysis['Humidity'] * 0.1)
weather_analysis['Weather_Comfort'] = (100 - abs(weather_analysis['Temperature'] - 25)) * (100 - weather_analysis['Humidity']) / 100

# Sample weather data for pair plot (focus on Mumbai)
mumbai_weather = weather_analysis[weather_analysis['City'] == 'Mumbai'].sample(200)

plt.figure(figsize=(12, 10))
pair_plot = sns.pairplot(mumbai_weather,
                        vars=['Temperature', 'Humidity', 'Rainfall', 'Wind_Speed', 'Weather_Comfort'],
                        hue='Season',
                        diag_kind='kde',
                        plot_kws={'alpha': 0.7})
pair_plot.fig.suptitle('Mumbai Weather - Seasonal Patterns Analysis', y=1.02, fontsize=16, fontweight='bold')
plt.savefig('Day14/10c_weather_pairplot.png', dpi=300, bbox_inches='tight')
plt.show()

# 4. Custom Pair Plot with Regression Lines
print("\n4. Creating Custom Regression Pair Plot...")

# Create enhanced stock analysis with multiple companies
stock_comparison = []
for company in ['RELIANCE', 'TCS', 'INFY']:
    company_data = stock_df[stock_df['Company'] == company].head(100)
    company_data['Company'] = company
    company_data['Price_Volatility'] = company_data['Daily_Return'].rolling(5).std()
    company_data['Volume_Normalized'] = company_data['Volume'] / company_data['Volume'].mean()
    stock_comparison.append(company_data[['Company', 'Close', 'Volume_Normalized', 'Daily_Return', 'Price_Volatility']].dropna())

stock_multi = pd.concat(stock_comparison, ignore_index=True)

plt.figure(figsize=(12, 10))
pair_plot = sns.pairplot(stock_multi,
                        vars=['Close', 'Volume_Normalized', 'Daily_Return', 'Price_Volatility'],
                        hue='Company',
                        kind='reg',  # Add regression lines
                        diag_kind='kde',
                        plot_kws={'scatter_kws': {'alpha': 0.6}})
pair_plot.fig.suptitle('Stock Comparison - Regression Analysis', y=1.02, fontsize=16, fontweight='bold')
plt.savefig('Day14/10d_regression_pairplot.png', dpi=300, bbox_inches='tight')
plt.show()

# 5. Advanced Pair Plot with Custom Functions
print("\n5. Creating Advanced Custom Pair Plot...")

# Create comprehensive student analysis
subjects_pivot = student_df.pivot_table(index='Student_ID', columns='Subject', values='Marks', aggfunc='first')
subjects_pivot = subjects_pivot[['Math', 'Physics', 'Chemistry', 'Biology']].dropna()

# Add student metadata
student_meta = student_df.drop_duplicates('Student_ID')[['Student_ID', 'Gender', 'Class', 'Attendance']]
subjects_analysis = subjects_pivot.merge(student_meta, on='Student_ID')

# Create performance ratios
subjects_analysis['STEM_Avg'] = (subjects_analysis['Math'] + subjects_analysis['Physics'] + subjects_analysis['Chemistry']) / 3
subjects_analysis['Science_Ratio'] = subjects_analysis['Physics'] / subjects_analysis['Biology']

# Sample for visualization
subjects_sample = subjects_analysis.sample(min(100, len(subjects_analysis)))

def custom_scatter(x, y, **kwargs):
    """Custom scatter plot with correlation coefficient"""
    ax = plt.gca()
    sns.scatterplot(x=x, y=y, **kwargs)
    
    # Calculate and display correlation
    if len(x) > 1 and len(y) > 1:
        corr = np.corrcoef(x, y)[0, 1]
        ax.text(0.05, 0.95, f'r = {corr:.3f}', transform=ax.transAxes, 
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

def custom_hist(x, **kwargs):
    """Custom histogram with statistics"""
    ax = plt.gca()
    sns.histplot(x=x, **kwargs)
    
    # Add mean line
    mean_val = np.mean(x)
    ax.axvline(mean_val, color='red', linestyle='--', alpha=0.7)
    ax.text(0.7, 0.9, f'μ = {mean_val:.1f}', transform=ax.transAxes,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))

# Create custom pair plot
g = sns.PairGrid(subjects_sample, vars=['Math', 'Physics', 'Chemistry', 'STEM_Avg'], hue='Gender')
g.map_upper(custom_scatter, alpha=0.7)
g.map_lower(sns.scatterplot, alpha=0.7)
g.map_diag(custom_hist, alpha=0.7)
g.add_legend()

plt.suptitle('Student Subject Performance - Detailed Analysis', y=1.02, fontsize=16, fontweight='bold')
plt.savefig('Day14/10e_custom_pairplot.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n📊 KEY LEARNING POINTS:")
print("• Pair plots show all pairwise relationships in one view")
print("• Diagonal shows distribution of individual variables")
print("• Upper/lower triangles show scatter plots or correlations")
print("• Color coding (hue) reveals patterns across categories")
print("• Regression lines help identify linear relationships")
print("• Custom functions allow specialized analysis")

# Statistical Analysis Summary
print(f"\n📈 MULTI-VARIABLE INSIGHTS:")

# Stock correlations
print("Stock Market Variable Correlations:")
stock_corr = stock_plot_data.corr()
high_corr_pairs = []
for i in range(len(stock_corr.columns)):
    for j in range(i+1, len(stock_corr.columns)):
        corr_val = stock_corr.iloc[i, j]
        if abs(corr_val) > 0.3:  # Significant correlation
            high_corr_pairs.append((stock_corr.columns[i], stock_corr.columns[j], corr_val))

for var1, var2, corr in sorted(high_corr_pairs, key=lambda x: abs(x[2]), reverse=True):
    print(f"  • {var1} ↔ {var2}: {corr:.3f}")

# Student performance correlations
print(f"\nStudent Subject Correlations:")
subject_corr = subjects_analysis[['Math', 'Physics', 'Chemistry', 'Biology']].corr()
strongest_corr = subject_corr.unstack().drop_duplicates().nlargest(2).iloc[1]
weakest_corr = subject_corr.unstack().drop_duplicates().nsmallest(2).iloc[1]
print(f"  • Strongest correlation: {strongest_corr.name[0]} ↔ {strongest_corr.name[1]} ({strongest_corr:.3f})")
print(f"  • Weakest correlation: {weakest_corr.name[0]} ↔ {weakest_corr.name[1]} ({weakest_corr:.3f})")

# Weather correlations
print(f"\nWeather Variable Correlations (Mumbai):")
weather_corr = mumbai_weather[['Temperature', 'Humidity', 'Rainfall', 'Wind_Speed']].corr()
temp_humidity_corr = weather_corr.loc['Temperature', 'Humidity']
temp_rainfall_corr = weather_corr.loc['Temperature', 'Rainfall']
print(f"  • Temperature ↔ Humidity: {temp_humidity_corr:.3f}")
print(f"  • Temperature ↔ Rainfall: {temp_rainfall_corr:.3f}")

# Performance insights
print(f"\nPerformance Insights:")
avg_performance = student_metrics.groupby('Gender')['Avg_Marks'].mean()
consistency = student_metrics.groupby('Gender')['Performance_Consistency'].mean()
print(f"  • Average marks by gender: Male={avg_performance.get('Male', 0):.1f}, Female={avg_performance.get('Female', 0):.1f}")
print(f"  • Performance consistency: Male={consistency.get('Male', 0):.3f}, Female={consistency.get('Female', 0):.3f}")

print(f"\n✓ Charts saved as:")
print("  • Day14/10a_stock_pairplot.png")
print("  • Day14/10b_student_pairplot.png") 
print("  • Day14/10c_weather_pairplot.png")
print("  • Day14/10d_regression_pairplot.png")
print("  • Day14/10e_custom_pairplot.png")