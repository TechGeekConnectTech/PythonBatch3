import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducible data
np.random.seed(42)
random.seed(42)

print("Creating Stock Market and Other Datasets for Visualization Examples...")
print("=" * 70)

# 1. STOCK MARKET DATA
print("\n1. Creating Stock Market Dataset...")

# Generate 2 years of daily stock data for 5 companies
start_date = datetime(2022, 1, 1)
end_date = datetime(2024, 1, 1)
date_range = pd.date_range(start=start_date, end=end_date, freq='D')
# Filter out weekends (stock markets closed)
business_days = [d for d in date_range if d.weekday() < 5]

companies = {
    'RELIANCE': {'initial_price': 2400, 'volatility': 0.02},
    'TCS': {'initial_price': 3200, 'volatility': 0.025},
    'INFY': {'initial_price': 1500, 'volatility': 0.03},
    'HDFC': {'initial_price': 2800, 'volatility': 0.022},
    'ICICI': {'initial_price': 800, 'volatility': 0.028}
}

stock_data = []

for company, params in companies.items():
    price = params['initial_price']
    vol = params['volatility']
    
    for date in business_days:
        # Simulate realistic stock price movement
        daily_return = np.random.normal(0.0005, vol)  # Small positive drift
        price = price * (1 + daily_return)
        
        # Create OHLC data
        open_price = price
        high_price = open_price * (1 + abs(np.random.normal(0, vol/2)))
        low_price = open_price * (1 - abs(np.random.normal(0, vol/2)))
        close_price = low_price + (high_price - low_price) * np.random.random()
        
        # Volume (higher volume on high volatility days)
        base_volume = np.random.randint(50000, 200000)
        volatility_multiplier = 1 + abs(daily_return) * 10
        volume = int(base_volume * volatility_multiplier)
        
        stock_data.append({
            'Date': date.strftime('%Y-%m-%d'),
            'Company': company,
            'Open': round(open_price, 2),
            'High': round(high_price, 2),
            'Low': round(low_price, 2),
            'Close': round(close_price, 2),
            'Volume': volume,
            'Daily_Return': round(daily_return * 100, 3)
        })
        
        price = close_price  # Update price for next day

# Save stock market data
stock_df = pd.DataFrame(stock_data)
stock_df.to_csv('Day14/stock_market_data.csv', index=False)
print(f"✓ Created stock_market_data.csv with {len(stock_df)} records")

# 2. SALES DATA
print("\n2. Creating Sales Dataset...")

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
products = ['Laptops', 'Smartphones', 'Tablets', 'Headphones', 'Watches']
regions = ['North', 'South', 'East', 'West', 'Central']
years = [2022, 2023]

sales_data = []
for year in years:
    for month in months:
        for product in products:
            for region in regions:
                # Seasonal trends
                seasonal_multiplier = 1.0
                if month in ['Nov', 'Dec']:  # Holiday season
                    seasonal_multiplier = 1.4
                elif month in ['Jun', 'Jul']:  # Summer
                    seasonal_multiplier = 0.8
                
                # Product popularity
                product_multiplier = {
                    'Smartphones': 1.5, 'Laptops': 1.2, 'Tablets': 0.8,
                    'Headphones': 1.0, 'Watches': 0.9
                }
                
                base_sales = np.random.randint(100, 500)
                sales = int(base_sales * seasonal_multiplier * product_multiplier[product])
                revenue = sales * np.random.randint(200, 1500)
                
                sales_data.append({
                    'Year': year,
                    'Month': month,
                    'Product': product,
                    'Region': region,
                    'Sales_Units': sales,
                    'Revenue': revenue,
                    'Profit_Margin': round(np.random.uniform(0.15, 0.35), 3)
                })

sales_df = pd.DataFrame(sales_data)
sales_df.to_csv('Day14/sales_data.csv', index=False)
print(f"✓ Created sales_data.csv with {len(sales_df)} records")

# 3. STUDENT GRADES DATA
print("\n3. Creating Student Grades Dataset...")

students_data = []
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History']
classes = ['10A', '10B', '11A', '11B', '12A', '12B']
genders = ['Male', 'Female']

student_id = 1000
for class_name in classes:
    for i in range(35):  # 35 students per class
        student_id += 1
        name = f"Student_{student_id}"
        gender = random.choice(genders)
        
        # Base performance level for student
        base_performance = np.random.normal(75, 15)  # Mean 75, std 15
        
        for subject in subjects:
            # Subject difficulty adjustment
            subject_adjustment = {
                'Math': -5, 'Physics': -3, 'Chemistry': -2,
                'Biology': 2, 'English': 3, 'History': 5
            }[subject]
            
            marks = base_performance + subject_adjustment + np.random.normal(0, 8)
            marks = max(35, min(100, marks))  # Clamp between 35-100
            
            students_data.append({
                'Student_ID': student_id,
                'Name': name,
                'Class': class_name,
                'Gender': gender,
                'Subject': subject,
                'Marks': round(marks, 1),
                'Grade': 'A' if marks >= 90 else 'B' if marks >= 75 else 'C' if marks >= 60 else 'D',
                'Attendance': round(np.random.uniform(0.7, 1.0), 3)
            })

students_df = pd.DataFrame(students_data)
students_df.to_csv('Day14/student_grades.csv', index=False)
print(f"✓ Created student_grades.csv with {len(students_df)} records")

# 4. WEATHER DATA
print("\n4. Creating Weather Dataset...")

cities = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Pune']
weather_data = []

for city in cities:
    # City-specific base temperatures
    base_temps = {
        'Mumbai': 28, 'Delhi': 25, 'Bangalore': 23,
        'Chennai': 30, 'Kolkata': 27, 'Pune': 25
    }
    
    base_temp = base_temps[city]
    
    for i in range(365):  # 1 year of data
        date = start_date + timedelta(days=i)
        
        # Seasonal temperature variation
        seasonal_factor = 5 * np.sin(2 * np.pi * i / 365)  # ±5°C seasonal variation
        daily_temp = base_temp + seasonal_factor + np.random.normal(0, 3)
        
        # Humidity (higher in coastal cities)
        base_humidity = 70 if city in ['Mumbai', 'Chennai', 'Kolkata'] else 60
        humidity = base_humidity + np.random.normal(0, 10)
        humidity = max(30, min(95, humidity))
        
        # Rainfall (monsoon season effect)
        rainfall = 0
        if 6 <= date.month <= 9:  # Monsoon months
            rainfall = max(0, np.random.exponential(2))
        else:
            rainfall = max(0, np.random.exponential(0.5))
        
        weather_data.append({
            'Date': date.strftime('%Y-%m-%d'),
            'City': city,
            'Temperature': round(daily_temp, 1),
            'Humidity': round(humidity, 1),
            'Rainfall': round(rainfall, 2),
            'Wind_Speed': round(np.random.uniform(5, 25), 1),
            'Pressure': round(np.random.uniform(1008, 1018), 1)
        })

weather_df = pd.DataFrame(weather_data)
weather_df.to_csv('Day14/weather_data.csv', index=False)
print(f"✓ Created weather_data.csv with {len(weather_df)} records")

# 5. DEMOGRAPHICS DATA
print("\n5. Creating Demographics Dataset...")

states = ['Maharashtra', 'Karnataka', 'Tamil Nadu', 'Delhi', 'Gujarat', 'Rajasthan', 
          'West Bengal', 'Uttar Pradesh', 'Kerala', 'Punjab']

demographics_data = []
for state in states:
    # Generate age group distribution
    age_groups = ['0-14', '15-29', '30-44', '45-59', '60+']
    total_population = np.random.randint(50000000, 200000000)
    
    # Age distribution percentages
    age_dist = [0.25, 0.30, 0.25, 0.15, 0.05]  # Typical developing country distribution
    age_dist = np.random.dirichlet(np.array(age_dist) * 10)  # Add some variation
    
    for i, age_group in enumerate(age_groups):
        population = int(total_population * age_dist[i])
        
        # Gender split (slightly more males in some age groups)
        male_ratio = 0.52 if age_group in ['0-14', '15-29'] else 0.50
        male_population = int(population * male_ratio)
        female_population = population - male_population
        
        demographics_data.extend([
            {
                'State': state,
                'Age_Group': age_group,
                'Gender': 'Male',
                'Population': male_population,
                'Literacy_Rate': round(np.random.uniform(0.65, 0.95), 3),
                'Employment_Rate': round(np.random.uniform(0.40, 0.75), 3)
            },
            {
                'State': state,
                'Age_Group': age_group,
                'Gender': 'Female',
                'Population': female_population,
                'Literacy_Rate': round(np.random.uniform(0.55, 0.90), 3),
                'Employment_Rate': round(np.random.uniform(0.25, 0.50), 3)
            }
        ])

demographics_df = pd.DataFrame(demographics_data)
demographics_df.to_csv('Day14/demographics_data.csv', index=False)
print(f"✓ Created demographics_data.csv with {len(demographics_df)} records")

# 6. E-COMMERCE DATA
print("\n6. Creating E-commerce Dataset...")

categories = ['Electronics', 'Clothing', 'Books', 'Home & Garden', 'Sports', 'Beauty']
customer_segments = ['Premium', 'Regular', 'Budget']

ecommerce_data = []
for i in range(5000):  # 5000 transactions
    transaction_id = f"TXN_{1000 + i}"
    date = start_date + timedelta(days=np.random.randint(0, 730))  # 2 years
    
    category = random.choice(categories)
    segment = random.choice(customer_segments)
    
    # Price based on category and segment
    base_prices = {
        'Electronics': 500, 'Clothing': 100, 'Books': 30,
        'Home & Garden': 150, 'Sports': 200, 'Beauty': 80
    }
    
    segment_multiplier = {'Premium': 2.0, 'Regular': 1.0, 'Budget': 0.6}
    
    base_price = base_prices[category]
    price = base_price * segment_multiplier[segment] * np.random.uniform(0.5, 2.0)
    
    quantity = np.random.randint(1, 5)
    total_amount = price * quantity
    
    # Customer satisfaction (higher for premium)
    base_satisfaction = {'Premium': 4.2, 'Regular': 3.8, 'Budget': 3.5}
    satisfaction = base_satisfaction[segment] + np.random.normal(0, 0.5)
    satisfaction = max(1, min(5, satisfaction))
    
    ecommerce_data.append({
        'Transaction_ID': transaction_id,
        'Date': date.strftime('%Y-%m-%d'),
        'Category': category,
        'Customer_Segment': segment,
        'Quantity': quantity,
        'Unit_Price': round(price, 2),
        'Total_Amount': round(total_amount, 2),
        'Customer_Satisfaction': round(satisfaction, 1),
        'Return_Status': 'Yes' if np.random.random() < 0.08 else 'No',  # 8% return rate
        'Payment_Method': random.choice(['Credit Card', 'Debit Card', 'UPI', 'Cash on Delivery'])
    })

ecommerce_df = pd.DataFrame(ecommerce_data)
ecommerce_df.to_csv('Day14/ecommerce_data.csv', index=False)
print(f"✓ Created ecommerce_data.csv with {len(ecommerce_df)} records")

print("\n" + "=" * 70)
print("DATASET CREATION COMPLETED!")
print("=" * 70)

datasets_created = [
    ('stock_market_data.csv', len(stock_df), 'OHLCV data for 5 companies over 2 years'),
    ('sales_data.csv', len(sales_df), 'Sales data by product, region, and time'),
    ('student_grades.csv', len(students_df), 'Student performance across subjects'),
    ('weather_data.csv', len(weather_df), 'Weather data for 6 Indian cities'),
    ('demographics_data.csv', len(demographics_df), 'Population demographics by state'),
    ('ecommerce_data.csv', len(ecommerce_df), 'E-commerce transactions and customer data')
]

for filename, records, description in datasets_created:
    print(f"✓ {filename}: {records:,} records - {description}")

print(f"\nAll datasets saved in Day14/ folder and ready for visualization examples!")