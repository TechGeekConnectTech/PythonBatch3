"""
BOX PLOT EXAMPLE - Statistical Distribution Analysis
====================================================
Box plots show statistical distribution: median, quartiles, outliers.
Use cases: Performance comparison, salary analysis, test scores, etc.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load datasets
stock_df = pd.read_csv('Day14/stock_market_data.csv')
student_df = pd.read_csv('Day14/student_grades.csv')
weather_df = pd.read_csv('Day14/weather_data.csv')
sales_df = pd.read_csv('Day14/sales_data.csv')

print("BOX PLOT EXAMPLE: Statistical Distribution Analysis")
print("=" * 50)

# Create figure with multiple box plot types
plt.figure(figsize=(15, 12))

# 1. Basic Box Plot - Stock Returns by Company
plt.subplot(2, 3, 1)
companies = ['RELIANCE', 'TCS', 'INFY', 'HDFC', 'ICICI']
returns_data = []

for company in companies:
    company_returns = stock_df[stock_df['Company'] == company]['Daily_Return']
    returns_data.append(company_returns)

box_plot = plt.boxplot(returns_data, labels=companies, patch_artist=True, 
                      notch=True, showmeans=True)

# Color the boxes
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 'lightpink']
for patch, color in zip(box_plot['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

plt.title('Daily Returns Distribution by Company', fontsize=14, fontweight='bold')
plt.xlabel('Company')
plt.ylabel('Daily Return (%)')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)

# 2. Horizontal Box Plot - Student Marks by Subject
plt.subplot(2, 3, 2)
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']
marks_data = []

for subject in subjects:
    subject_marks = student_df[student_df['Subject'] == subject]['Marks']
    marks_data.append(subject_marks)

box_plot = plt.boxplot(marks_data, labels=subjects, vert=False, patch_artist=True,
                      showmeans=True, meanline=True)

# Color the boxes with gradient
colors = plt.cm.viridis(np.linspace(0, 1, len(subjects)))
for patch, color in zip(box_plot['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.8)

plt.title('Student Marks Distribution by Subject', fontsize=14, fontweight='bold')
plt.xlabel('Marks')
plt.ylabel('Subject')
plt.grid(True, alpha=0.3)

# 3. Grouped Box Plot - Temperature by City and Season
plt.subplot(2, 3, 3)

# Create season column
weather_df['Date'] = pd.to_datetime(weather_df['Date'])
weather_df['Month'] = weather_df['Date'].dt.month

def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Autumn'

weather_df['Season'] = weather_df['Month'].apply(get_season)

# Focus on 3 cities for clarity
cities = ['Mumbai', 'Delhi', 'Bangalore']
seasons = ['Winter', 'Spring', 'Summer', 'Autumn']

# Prepare data for grouped box plot
temp_data_grouped = []
labels_grouped = []

for season in seasons:
    for city in cities:
        city_season_temp = weather_df[(weather_df['City'] == city) & 
                                     (weather_df['Season'] == season)]['Temperature']
        if len(city_season_temp) > 0:
            temp_data_grouped.append(city_season_temp)
            labels_grouped.append(f'{city}\n{season}')

box_plot = plt.boxplot(temp_data_grouped, patch_artist=True, showmeans=True)

# Color by city
city_colors = {'Mumbai': 'lightcoral', 'Delhi': 'lightblue', 'Bangalore': 'lightgreen'}
for i, label in enumerate(labels_grouped):
    city = label.split('\n')[0]
    box_plot['boxes'][i].set_facecolor(city_colors[city])
    box_plot['boxes'][i].set_alpha(0.7)

plt.title('Temperature Distribution\n(City & Season)', fontsize=14, fontweight='bold')
plt.xlabel('City - Season')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

# 4. Box Plot with Outlier Analysis - Sales Performance
plt.subplot(2, 3, 4)
products = sales_df['Product'].unique()
sales_data = []

for product in products:
    product_sales = sales_df[sales_df['Product'] == product]['Sales_Units']
    sales_data.append(product_sales)

box_plot = plt.boxplot(sales_data, labels=products, patch_artist=True,
                      showfliers=True, flierprops=dict(marker='o', markersize=8, 
                      markerfacecolor='red', alpha=0.7))

# Highlight outliers
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57']
for patch, color in zip(box_plot['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.8)

plt.title('Sales Distribution by Product\n(Outliers Highlighted)', fontsize=14, fontweight='bold')
plt.xlabel('Product')
plt.ylabel('Sales Units')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

# 5. Box Plot with Violin Overlay - Student Performance by Class
plt.subplot(2, 3, 5)

classes = ['10A', '10B', '11A', '11B', '12A', '12B']
class_marks = []

for class_name in classes:
    marks = student_df[student_df['Class'] == class_name]['Marks']
    class_marks.append(marks)

# Create violin plot first (background)
parts = plt.violinplot(class_marks, positions=range(1, len(classes)+1), 
                      showmeans=False, showmedians=False, alpha=0.6)

for pc, color in zip(parts['bodies'], plt.cm.Set3(np.linspace(0, 1, len(classes)))):
    pc.set_facecolor(color)

# Overlay box plot
box_plot = plt.boxplot(class_marks, positions=range(1, len(classes)+1),
                      patch_artist=False, widths=0.3, 
                      boxprops=dict(color='black', linewidth=2),
                      whiskerprops=dict(color='black', linewidth=2),
                      capprops=dict(color='black', linewidth=2),
                      medianprops=dict(color='red', linewidth=2))

plt.title('Student Performance Distribution\n(Violin + Box Plot)', fontsize=14, fontweight='bold')
plt.xlabel('Class')
plt.ylabel('Marks')
plt.xticks(range(1, len(classes)+1), classes)
plt.grid(True, alpha=0.3)

# 6. Multiple Box Plots Comparison - Stock Volatility
plt.subplot(2, 3, 6)

# Calculate volatility (rolling standard deviation)
volatility_data = []
companies_vol = ['RELIANCE', 'TCS', 'INFY']

for company in companies_vol:
    company_data = stock_df[stock_df['Company'] == company].sort_values('Date')
    company_data['Date'] = pd.to_datetime(company_data['Date'])
    
    # Calculate 30-day rolling volatility
    company_data['Volatility'] = company_data['Daily_Return'].rolling(window=30).std()
    volatility_data.append(company_data['Volatility'].dropna())

# Create side-by-side box plots
positions = [1, 2, 3]
box_plot = plt.boxplot(volatility_data, positions=positions, patch_artist=True,
                      widths=0.6, showmeans=True)

colors = ['lightblue', 'lightgreen', 'lightcoral']
for patch, color in zip(box_plot['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.8)

plt.title('Stock Volatility Comparison\n(30-Day Rolling)', fontsize=14, fontweight='bold')
plt.xlabel('Company')
plt.ylabel('Volatility (% Std Dev)')
plt.xticks(positions, companies_vol)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('Day14/06_box_plot_example.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n📊 KEY LEARNING POINTS:")
print("• Box plots show statistical distribution summary")
print("• Box shows Q1, median (Q2), and Q3")
print("• Whiskers extend to min/max within 1.5*IQR")
print("• Dots beyond whiskers are outliers")
print("• Notched boxes show confidence interval around median")
print("• Compare distributions across categories")

# Statistical Analysis
print(f"\n📈 STATISTICAL INSIGHTS:")

# Stock returns analysis
print("Stock Returns Statistics:")
for company in ['RELIANCE', 'TCS', 'INFY']:
    returns = stock_df[stock_df['Company'] == company]['Daily_Return']
    q1, median, q3 = returns.quantile([0.25, 0.5, 0.75])
    iqr = q3 - q1
    outliers = returns[(returns < (q1 - 1.5*iqr)) | (returns > (q3 + 1.5*iqr))]
    
    print(f"  • {company}:")
    print(f"    - Median: {median:.3f}%, IQR: {iqr:.3f}%")
    print(f"    - Outliers: {len(outliers)} ({len(outliers)/len(returns)*100:.1f}%)")

# Subject difficulty analysis
print(f"\nSubject Difficulty Analysis (Based on Marks):")
for subject in ['Math', 'Physics', 'Chemistry']:
    marks = student_df[student_df['Subject'] == subject]['Marks']
    median_marks = marks.median()
    difficulty = "Hard" if median_marks < 70 else "Medium" if median_marks < 80 else "Easy"
    print(f"  • {subject}: Median={median_marks:.1f}, Difficulty={difficulty}")

# City temperature analysis
print(f"\nCity Temperature Characteristics:")
for city in ['Mumbai', 'Delhi', 'Bangalore']:
    city_temp = weather_df[weather_df['City'] == city]['Temperature']
    temp_range = city_temp.max() - city_temp.min()
    print(f"  • {city}: Median={city_temp.median():.1f}°C, Range={temp_range:.1f}°C")

print(f"\n✓ Chart saved as: Day14/06_box_plot_example.png")