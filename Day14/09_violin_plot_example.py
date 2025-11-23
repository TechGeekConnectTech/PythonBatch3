"""
VIOLIN PLOT EXAMPLE - Distribution Shape Analysis
================================================
Violin plots show distribution shape, density, and statistics combined.
Use cases: Compare distributions, see data density, statistical analysis, etc.
"""

import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set seaborn style
sns.set_style("whitegrid")
plt.rcParams['figure.facecolor'] = 'white'

# Load datasets
stock_df = pd.read_csv('Day14/stock_market_data.csv')
student_df = pd.read_csv('Day14/student_grades.csv')
weather_df = pd.read_csv('Day14/weather_data.csv')
sales_df = pd.read_csv('Day14/sales_data.csv')

print("VIOLIN PLOT EXAMPLE: Distribution Shape Analysis")
print("=" * 50)

# Create figure with multiple violin plot types
plt.figure(figsize=(18, 12))

# 1. Basic Violin Plot - Stock Returns by Company
plt.subplot(2, 3, 1)

# Prepare stock returns data
stock_returns = stock_df[stock_df['Company'].isin(['RELIANCE', 'TCS', 'INFY', 'HDFC'])]

sns.violinplot(data=stock_returns, x='Company', y='Daily_Return', 
              palette='Set2', inner='box')

plt.title('Daily Returns Distribution by Company', fontsize=14, fontweight='bold')
plt.xlabel('Company')
plt.ylabel('Daily Return (%)')
plt.xticks(rotation=45)

# 2. Split Violin Plot - Student Marks by Gender and Subject
plt.subplot(2, 3, 2)

# Filter to key subjects for clarity
key_subjects = ['Math', 'Physics', 'Chemistry']
student_subset = student_df[student_df['Subject'].isin(key_subjects)]

sns.violinplot(data=student_subset, x='Subject', y='Marks', hue='Gender',
              split=True, palette='Set1', inner='quartile')

plt.title('Student Marks Distribution\n(Split by Gender)', fontsize=14, fontweight='bold')
plt.xlabel('Subject')
plt.ylabel('Marks')
plt.legend(title='Gender')

# 3. Violin Plot with Points - Weather Data by City
plt.subplot(2, 3, 3)

# Select subset of cities for clarity
weather_subset = weather_df[weather_df['City'].isin(['Mumbai', 'Delhi', 'Bangalore', 'Chennai'])]

sns.violinplot(data=weather_subset, x='City', y='Temperature', 
              palette='coolwarm', inner='points', orient='v')

plt.title('Temperature Distribution by City', fontsize=14, fontweight='bold')
plt.xlabel('City')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)

# 4. Horizontal Violin Plot - Sales Performance by Product
plt.subplot(2, 3, 4)

sns.violinplot(data=sales_df, y='Product', x='Sales_Units',
              palette='viridis', inner='box', orient='h')

plt.title('Sales Units Distribution by Product', fontsize=14, fontweight='bold')
plt.xlabel('Sales Units')
plt.ylabel('Product')

# 5. Multi-level Violin Plot - Student Performance by Class and Subject
plt.subplot(2, 3, 5)

# Focus on specific classes
class_subset = student_df[student_df['Class'].isin(['10A', '11A', '12A']) & 
                         student_df['Subject'].isin(['Math', 'Physics'])]

sns.violinplot(data=class_subset, x='Class', y='Marks', hue='Subject',
              palette='Dark2', inner='quartile')

plt.title('Marks Distribution\n(Class & Subject)', fontsize=14, fontweight='bold')
plt.xlabel('Class')
plt.ylabel('Marks')
plt.legend(title='Subject')

# 6. Violin Plot with Custom Statistics - Stock Volume Analysis
plt.subplot(2, 3, 6)

# Prepare volume data (in thousands for better scale)
stock_volume = stock_df.copy()
stock_volume['Volume_K'] = stock_volume['Volume'] / 1000

companies = ['RELIANCE', 'TCS', 'INFY']
volume_subset = stock_volume[stock_volume['Company'].isin(companies)]

sns.violinplot(data=volume_subset, x='Company', y='Volume_K',
              palette='plasma', inner='quartile')

plt.title('Trading Volume Distribution\n(Thousands)', fontsize=14, fontweight='bold')
plt.xlabel('Company')
plt.ylabel('Volume (Thousands)')

plt.tight_layout()
plt.savefig('Day14/09_violin_plot_example.png', dpi=300, bbox_inches='tight')
plt.show()

# Create advanced violin plot combinations
plt.figure(figsize=(15, 10))

# 7. Violin + Strip Plot - Enhanced Distribution View
plt.subplot(2, 2, 1)

# Student attendance vs marks
student_sample = student_df.sample(200)  # Sample for clarity

sns.violinplot(data=student_sample, x='Grade', y='Marks', 
              palette='pastel', inner=None, alpha=0.6)
sns.stripplot(data=student_sample, x='Grade', y='Marks', 
             size=4, color='black', alpha=0.7)

plt.title('Marks Distribution with Individual Points\n(by Grade)', fontsize=12, fontweight='bold')
plt.xlabel('Grade')
plt.ylabel('Marks')

# 8. Violin Plot with Box Plot Overlay - Weather Analysis
plt.subplot(2, 2, 2)

# Rainfall distribution by city
rainfall_data = weather_df[weather_df['Rainfall'] > 0]  # Only rainy days
cities = ['Mumbai', 'Delhi', 'Chennai']
rainfall_subset = rainfall_data[rainfall_data['City'].isin(cities)]

sns.violinplot(data=rainfall_subset, x='City', y='Rainfall',
              palette='Blues', inner=None, alpha=0.6)
sns.boxplot(data=rainfall_subset, x='City', y='Rainfall',
           width=0.3, boxprops=dict(alpha=0.8))

plt.title('Rainfall Distribution on Rainy Days\n(Violin + Box Plot)', fontsize=12, fontweight='bold')
plt.xlabel('City')
plt.ylabel('Rainfall (mm)')

# 9. Comparative Violin Plot - Sales Performance Comparison
plt.subplot(2, 2, 3)

# Compare 2022 vs 2023 sales
sns.violinplot(data=sales_df, x='Year', y='Sales_Units',
              palette=['lightcoral', 'lightblue'], inner='quartile')

plt.title('Sales Distribution Comparison\n(2022 vs 2023)', fontsize=12, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Sales Units')

# Add statistical annotation
from scipy import stats
sales_2022 = sales_df[sales_df['Year'] == 2022]['Sales_Units']
sales_2023 = sales_df[sales_df['Year'] == 2023]['Sales_Units']
statistic, p_value = stats.mannwhitneyu(sales_2022, sales_2023)
plt.text(0.5, plt.ylim()[1]*0.9, f'p-value: {p_value:.4f}', 
         ha='center', fontsize=10, bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))

# 10. Nested Violin Plot - Regional Sales Analysis
plt.subplot(2, 2, 4)

# Revenue distribution by region
sns.violinplot(data=sales_df, x='Region', y='Revenue',
              palette='Set3', inner='box')

plt.title('Revenue Distribution by Region', fontsize=12, fontweight='bold')
plt.xlabel('Region')
plt.ylabel('Revenue (₹)')
plt.xticks(rotation=45)

# Format y-axis to show values in lakhs
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x/100000:.1f}L'))

plt.tight_layout()
plt.savefig('Day14/09b_advanced_violin_plots.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n📊 KEY LEARNING POINTS:")
print("• Violin plots show full distribution shape (density)")
print("• Wider sections indicate higher data density")
print("• Inner statistics (box, quartiles, points) add detail")
print("• Split violins compare two groups efficiently")
print("• Better than box plots for showing multimodal distributions")
print("• Combine with strip/swarm plots for individual data points")

# Statistical Analysis
print(f"\n📈 DISTRIBUTION INSIGHTS:")

# Stock returns distribution analysis
print("Stock Returns Distribution Analysis:")
for company in ['RELIANCE', 'TCS', 'INFY']:
    returns = stock_df[stock_df['Company'] == company]['Daily_Return']
    skewness = returns.skew()
    kurtosis = returns.kurtosis()
    distribution_shape = "Right-skewed" if skewness > 0.5 else "Left-skewed" if skewness < -0.5 else "Symmetric"
    
    print(f"  • {company}:")
    print(f"    - Distribution: {distribution_shape} (skew: {skewness:.3f})")
    print(f"    - Kurtosis: {kurtosis:.3f} ({'Heavy-tailed' if kurtosis > 3 else 'Light-tailed'})")

# Student performance distribution
print(f"\nStudent Performance Distribution:")
for subject in ['Math', 'Physics', 'Chemistry']:
    subject_marks = student_df[student_df['Subject'] == subject]['Marks']
    q1, q3 = subject_marks.quantile([0.25, 0.75])
    iqr = q3 - q1
    outliers = subject_marks[(subject_marks < (q1 - 1.5*iqr)) | (subject_marks > (q3 + 1.5*iqr))]
    
    print(f"  • {subject}: IQR={iqr:.1f}, Outliers={len(outliers)} ({len(outliers)/len(subject_marks)*100:.1f}%)")

# Weather distribution analysis
print(f"\nWeather Distribution Analysis:")
for city in ['Mumbai', 'Delhi', 'Bangalore']:
    city_temp = weather_df[weather_df['City'] == city]['Temperature']
    std_dev = city_temp.std()
    variability = "High" if std_dev > 5 else "Medium" if std_dev > 3 else "Low"
    
    print(f"  • {city}: Std Dev={std_dev:.1f}°C, Variability={variability}")

# Sales performance comparison
print(f"\nSales Year-over-Year Comparison:")
sales_2022_stats = sales_2022.describe()
sales_2023_stats = sales_2023.describe()
median_change = ((sales_2023_stats['50%'] - sales_2022_stats['50%']) / sales_2022_stats['50%']) * 100

print(f"  • 2022: Median={sales_2022_stats['50%']:.0f}, Std={sales_2022_stats['std']:.0f}")
print(f"  • 2023: Median={sales_2023_stats['50%']:.0f}, Std={sales_2023_stats['std']:.0f}")
print(f"  • Median change: {median_change:+.1f}%")
print(f"  • Statistical significance: {'Yes' if p_value < 0.05 else 'No'} (p={p_value:.4f})")

print(f"\n✓ Charts saved as: Day14/09_violin_plot_example.png & Day14/09b_advanced_violin_plots.png")