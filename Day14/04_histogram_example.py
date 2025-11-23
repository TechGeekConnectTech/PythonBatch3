"""
HISTOGRAM EXAMPLE - Distribution Analysis
=========================================
Histograms show the distribution and frequency of continuous data.
Use cases: Grade distributions, income levels, age groups, measurement data, etc.
"""

import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for compatibility
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Set style for better looking plots
plt.style.use('default')
plt.rcParams['figure.facecolor'] = 'white'

# Load datasets
try:
    stock_df = pd.read_csv('Day14/stock_market_data.csv')
    student_df = pd.read_csv('Day14/student_grades.csv')
    weather_df = pd.read_csv('Day14/weather_data.csv')
    print("✓ All datasets loaded successfully")
except FileNotFoundError as e:
    print(f"❌ Error loading datasets: {e}")
    print("Make sure to run create_datasets.py first!")
    exit(1)

print("HISTOGRAM EXAMPLE: Distribution Analysis")
print("=" * 50)

# Create figure with multiple histogram types
plt.figure(figsize=(15, 12))

# 1. Basic Histogram - Stock Returns Distribution
plt.subplot(2, 3, 1)
reliance_returns = stock_df[stock_df['Company'] == 'RELIANCE']['Daily_Return']

n, bins, patches = plt.hist(reliance_returns, bins=30, alpha=0.7, color='skyblue', 
                           edgecolor='black', linewidth=0.7)
plt.title('RELIANCE Stock: Daily Returns Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Daily Return (%)')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)

# Add statistics
mean_return = reliance_returns.mean()
std_return = reliance_returns.std()
plt.axvline(mean_return, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_return:.3f}%')
plt.axvline(mean_return + std_return, color='orange', linestyle='--', alpha=0.7, label=f'+1 Std: {mean_return + std_return:.3f}%')
plt.axvline(mean_return - std_return, color='orange', linestyle='--', alpha=0.7, label=f'-1 Std: {mean_return - std_return:.3f}%')
plt.legend()

# 2. Multiple Histograms - Student Marks by Subject
plt.subplot(2, 3, 2)
subjects = ['Math', 'Physics', 'Chemistry']
colors = ['red', 'blue', 'green']

for subject, color in zip(subjects, colors):
    subject_marks = student_df[student_df['Subject'] == subject]['Marks']
    plt.hist(subject_marks, bins=20, alpha=0.6, label=subject, color=color, edgecolor='black', linewidth=0.5)

plt.title('Student Marks Distribution by Subject', fontsize=14, fontweight='bold')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True, alpha=0.3)

# 3. Normalized Histogram with Density Curve - Temperature Distribution
plt.subplot(2, 3, 3)
mumbai_temp = weather_df[weather_df['City'] == 'Mumbai']['Temperature']

# Plot histogram with density
n, bins, patches = plt.hist(mumbai_temp, bins=25, density=True, alpha=0.7, 
                           color='lightcoral', edgecolor='black', linewidth=0.7)

# Add normal distribution curve
mu, sigma = stats.norm.fit(mumbai_temp)
x = np.linspace(mumbai_temp.min(), mumbai_temp.max(), 100)
y = stats.norm.pdf(x, mu, sigma)
plt.plot(x, y, 'r-', linewidth=2, label=f'Normal Fit (μ={mu:.1f}°C, σ={sigma:.1f})')

plt.title('Mumbai Temperature Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Temperature (°C)')
plt.ylabel('Density')
plt.legend()
plt.grid(True, alpha=0.3)

# 4. Stacked Histogram - Gender Distribution of Grades
plt.subplot(2, 3, 4)
male_marks = student_df[student_df['Gender'] == 'Male']['Marks']
female_marks = student_df[student_df['Gender'] == 'Female']['Marks']

plt.hist([male_marks, female_marks], bins=20, label=['Male', 'Female'], 
         color=['lightblue', 'pink'], alpha=0.7, edgecolor='black', linewidth=0.5)

plt.title('Grade Distribution by Gender', fontsize=14, fontweight='bold')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True, alpha=0.3)

# 5. Cumulative Histogram - Stock Volume Analysis
plt.subplot(2, 3, 5)
all_volumes = stock_df['Volume'] / 1000  # Convert to thousands

n, bins, patches = plt.hist(all_volumes, bins=40, cumulative=True, alpha=0.7, 
                           color='green', edgecolor='black', linewidth=0.7)

plt.title('Cumulative Distribution: Trading Volume', fontsize=14, fontweight='bold')
plt.xlabel('Trading Volume (Thousands)')
plt.ylabel('Cumulative Frequency')
plt.grid(True, alpha=0.3)

# Add percentile lines
percentiles = [25, 50, 75, 90]
volume_percentiles = np.percentile(all_volumes, percentiles)
colors_perc = ['orange', 'red', 'blue', 'purple']

for p, vol, color in zip(percentiles, volume_percentiles, colors_perc):
    plt.axvline(vol, color=color, linestyle='--', alpha=0.8, 
                label=f'{p}th percentile: {vol:.0f}K')

plt.legend()

# 6. 2D Histogram (Hexbin) - Price vs Volume Relationship
plt.subplot(2, 3, 6)
reliance_data = stock_df[stock_df['Company'] == 'RELIANCE']

# Create 2D histogram using hexagonal binning
plt.hexbin(reliance_data['Volume']/1000, reliance_data['Close'], 
           gridsize=20, cmap='Blues', alpha=0.8)
plt.colorbar(label='Frequency')

plt.title('2D Histogram: Price vs Volume (RELIANCE)', fontsize=14, fontweight='bold')
plt.xlabel('Trading Volume (Thousands)')
plt.ylabel('Closing Price (₹)')

plt.tight_layout()
plt.savefig('Day14/04_histogram_example.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n📊 KEY LEARNING POINTS:")
print("• Histograms show data distribution and frequency")
print("• Bins determine the granularity of the distribution")
print("• Normal distribution creates a bell curve")
print("• Skewed distributions lean left or right")
print("• Cumulative histograms show percentile information")
print("• 2D histograms reveal density patterns")

# Statistical Analysis
print(f"\n📈 DISTRIBUTION INSIGHTS:")

# Stock returns analysis
print("Stock Returns Analysis:")
for company in ['RELIANCE', 'TCS', 'INFY']:
    returns = stock_df[stock_df['Company'] == company]['Daily_Return']
    print(f"  • {company}: Mean={returns.mean():.3f}%, Std={returns.std():.3f}%, Skew={returns.skew():.3f}")

# Student performance analysis
print(f"\nStudent Performance Analysis:")
overall_marks = student_df['Marks']
print(f"  • Overall Marks: Mean={overall_marks.mean():.1f}, Std={overall_marks.std():.1f}")
print(f"  • Grade A students (>=90): {(overall_marks >= 90).sum()} ({(overall_marks >= 90).mean()*100:.1f}%)")
print(f"  • Below average (<60): {(overall_marks < 60).sum()} ({(overall_marks < 60).mean()*100:.1f}%)")

# Temperature analysis
print(f"\nTemperature Analysis:")
for city in ['Mumbai', 'Delhi', 'Bangalore']:
    city_temp = weather_df[weather_df['City'] == city]['Temperature']
    print(f"  • {city}: Mean={city_temp.mean():.1f}°C, Range={city_temp.min():.1f}-{city_temp.max():.1f}°C")

# Check for normal distribution using Shapiro-Wilk test
try:
    reliance_returns_sample = reliance_returns.sample(min(5000, len(reliance_returns)))
    statistic, p_value = stats.shapiro(reliance_returns_sample)
    print(f"\nNormality Test (RELIANCE Returns):")
    print(f"  • Shapiro-Wilk p-value: {p_value:.6f}")
    print(f"  • Normal distribution: {'Yes' if p_value > 0.05 else 'No'} (p > 0.05)")
except Exception as e:
    print(f"\nNormality Test: Could not perform statistical test ({e})")

print(f"\n✓ Chart saved as: Day14/04_histogram_example.png")