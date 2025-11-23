"""
PIE CHART EXAMPLE - Composition Analysis
========================================
Pie charts show parts of a whole (percentages/proportions).
Use cases: Market share, budget allocation, survey responses, demographics, etc.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load datasets
sales_df = pd.read_csv('Day14/sales_data.csv')
student_df = pd.read_csv('Day14/student_grades.csv')
ecommerce_df = pd.read_csv('Day14/ecommerce_data.csv')

print("PIE CHART EXAMPLE: Composition Analysis")
print("=" * 50)

# Create figure with multiple pie chart types
plt.figure(figsize=(15, 12))

# 1. Basic Pie Chart - Market Share by Product
plt.subplot(2, 3, 1)
product_sales = sales_df.groupby('Product')['Sales_Units'].sum().sort_values(ascending=False)

colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57']
plt.pie(product_sales.values, labels=product_sales.index, autopct='%1.1f%%', 
        colors=colors, startangle=90, textprops={'fontsize': 10, 'fontweight': 'bold'})
plt.title('Market Share by Product\n(Based on Sales Units)', fontsize=14, fontweight='bold', pad=20)

# 2. Exploded Pie Chart - Regional Revenue Distribution
plt.subplot(2, 3, 2)
region_revenue = sales_df.groupby('Region')['Revenue'].sum().sort_values(ascending=False)

# Explode the largest segment
explode = [0.1 if i == 0 else 0 for i in range(len(region_revenue))]

wedges, texts, autotexts = plt.pie(region_revenue.values, labels=region_revenue.index, 
                                  autopct='%1.1f%%', explode=explode, colors=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF99CC'],
                                  startangle=45, shadow=True, textprops={'fontsize': 10})

# Beautify text
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

plt.title('Revenue Distribution by Region\n(Top Region Highlighted)', fontsize=14, fontweight='bold', pad=20)

# 3. Donut Chart - Student Grade Distribution
plt.subplot(2, 3, 3)
grade_counts = student_df['Grade'].value_counts()

colors = ['#2E8B57', '#4169E1', '#FFD700', '#FF6347']  # Green, Blue, Gold, Red
wedges, texts, autotexts = plt.pie(grade_counts.values, labels=grade_counts.index, 
                                  autopct='%1.1f%%', colors=colors, startangle=90,
                                  textprops={'fontsize': 11, 'fontweight': 'bold'})

# Create donut by adding a white circle in center
centre_circle = plt.Circle((0,0), 0.50, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Add center text
plt.text(0, 0, f'Total\nStudents\n{len(student_df)}', ha='center', va='center', 
         fontsize=12, fontweight='bold')

plt.title('Student Grade Distribution\n(Donut Chart)', fontsize=14, fontweight='bold', pad=20)

# 4. Nested Pie Chart - Sales by Product and Year
plt.subplot(2, 3, 4)

# Outer ring - Products
product_sales_total = sales_df.groupby('Product')['Sales_Units'].sum()
size_outer = 0.6

# Inner ring - Years within products
year_product_sales = sales_df.groupby(['Year', 'Product'])['Sales_Units'].sum()

# Create outer pie (products)
colors_outer = plt.cm.Set3(np.linspace(0, 1, len(product_sales_total)))
wedges_outer, texts_outer = plt.pie(product_sales_total.values, 
                                   labels=product_sales_total.index,
                                   radius=1, colors=colors_outer, 
                                   textprops={'fontsize': 9, 'fontweight': 'bold'},
                                   wedgeprops=dict(width=size_outer, edgecolor='white'))

# Create inner pie (years)
year_sales = sales_df.groupby('Year')['Sales_Units'].sum()
colors_inner = ['lightcoral', 'lightskyblue']
wedges_inner, texts_inner, autotexts_inner = plt.pie(year_sales.values,
                                                     radius=1-size_outer,
                                                     colors=colors_inner,
                                                     autopct='%1.0f%%',
                                                     textprops={'fontsize': 10, 'fontweight': 'bold'})

plt.title('Sales Distribution\n(Product & Year)', fontsize=14, fontweight='bold', pad=20)

# Add legend for years
plt.legend(wedges_inner, ['2022', '2023'], title="Years", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# 5. Multiple Pie Charts - E-commerce Analysis by Customer Segment
fig2 = plt.gcf()
gs = fig2.add_gridspec(2, 2, hspace=0.4, wspace=0.3)
ax5 = fig2.add_subplot(gs[1, 0])

segments = ecommerce_df['Customer_Segment'].unique()
colors_segment = ['gold', 'lightblue', 'lightcoral']

segment_counts = ecommerce_df['Customer_Segment'].value_counts()

plt.pie(segment_counts.values, labels=segment_counts.index, autopct='%1.1f%%',
        colors=colors_segment, startangle=90, textprops={'fontsize': 11, 'fontweight': 'bold'})
plt.title('Customer Segment Distribution', fontsize=14, fontweight='bold')

# 6. Pie Chart with Custom Legend - Payment Methods
ax6 = fig2.add_subplot(gs[1, 1])

payment_counts = ecommerce_df['Payment_Method'].value_counts()
colors_payment = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FECA57']

wedges, texts, autotexts = plt.pie(payment_counts.values, autopct='%1.1f%%',
                                  colors=colors_payment, startangle=90,
                                  textprops={'fontsize': 10, 'fontweight': 'bold'})

# Custom legend
plt.legend(wedges, payment_counts.index, title="Payment Methods", loc="center left", 
          bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

plt.title('Payment Method Preferences', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('Day14/05_pie_chart_example.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n📊 KEY LEARNING POINTS:")
print("• Pie charts show parts of a whole (percentages)")
print("• Use when you have categorical data that sums to 100%")
print("• Limit to 5-7 categories for clarity")
print("• Explode slices to emphasize important segments")
print("• Donut charts add space for central information")
print("• Avoid 3D pie charts - they can be misleading")

# Detailed Analysis
print(f"\n📈 COMPOSITION INSIGHTS:")

# Product market share analysis
total_units = product_sales.sum()
print("Product Market Share Analysis:")
for product, units in product_sales.items():
    percentage = (units / total_units) * 100
    print(f"  • {product}: {units:,} units ({percentage:.1f}%)")

# Regional revenue analysis
total_revenue = region_revenue.sum()
print(f"\nRegional Revenue Analysis (Total: ₹{total_revenue/1000000:.1f}M):")
for region, revenue in region_revenue.items():
    percentage = (revenue / total_revenue) * 100
    print(f"  • {region}: ₹{revenue/1000000:.1f}M ({percentage:.1f}%)")

# Grade distribution analysis
total_students = len(student_df)
print(f"\nGrade Distribution Analysis ({total_students} students):")
for grade in ['A', 'B', 'C', 'D']:
    count = (student_df['Grade'] == grade).sum()
    percentage = (count / total_students) * 100
    print(f"  • Grade {grade}: {count} students ({percentage:.1f}%)")

# Customer segment analysis
print(f"\nCustomer Segment Analysis:")
segment_revenue = ecommerce_df.groupby('Customer_Segment')['Total_Amount'].sum()
total_ecom_revenue = segment_revenue.sum()

for segment in segment_counts.index:
    count = segment_counts[segment]
    revenue = segment_revenue[segment]
    count_pct = (count / len(ecommerce_df)) * 100
    revenue_pct = (revenue / total_ecom_revenue) * 100
    avg_order = revenue / count
    print(f"  • {segment}: {count} customers ({count_pct:.1f}%), ₹{revenue/1000000:.1f}M revenue ({revenue_pct:.1f}%), Avg order: ₹{avg_order:.0f}")

print(f"\n✓ Chart saved as: Day14/05_pie_chart_example.png")