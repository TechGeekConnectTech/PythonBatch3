import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Step 1: Create a realistic dataset with 200 employee records
print("=" * 60)
print("CREATING SAMPLE EMPLOYEE DATASET (200 RECORDS)")
print("=" * 60)

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Generate sample data with various data quality issues
departments = ['IT', 'HR', 'Finance', 'Marketing', 'Sales', 'Operations']
positions = ['Manager', 'Senior', 'Junior', 'Lead', 'Director', 'Analyst']
cities = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Pune', 'Hyderabad']

data = []
for i in range(200):
    # Introduce some data quality issues intentionally
    emp_id = f"EMP{1001 + i}"
    
    # Some names have extra spaces or inconsistent formatting
    first_names = ['Rahul', 'Priya', 'Amit', 'Sneha', 'Vikram', 'Anita', 'Ravi', 'Kavya']
    last_names = ['Sharma', 'Patel', 'Singh', 'Kumar', 'Gupta', 'Jain', 'Rao', 'Reddy']
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    if i % 15 == 0:  # Add extra spaces randomly
        name = f"  {name}  "
    
    # Age with some invalid entries
    age = np.random.randint(22, 65)
    if i % 25 == 0:  # Some missing ages
        age = None
    elif i % 30 == 0:  # Some invalid ages
        age = 0
        
    # Department with some inconsistent formatting
    dept = random.choice(departments)
    if i % 20 == 0:  # Some lowercase departments
        dept = dept.lower()
    
    # Position
    position = random.choice(positions)
    
    # Salary with some outliers and missing values
    base_salary = np.random.randint(30000, 150000)
    if dept == 'IT':
        base_salary += 20000
    if position in ['Manager', 'Director', 'Lead']:
        base_salary += 30000
    
    if i % 18 == 0:  # Some missing salaries
        salary = None
    elif i % 40 == 0:  # Some unrealistic salaries
        salary = 5000  # Too low
    else:
        salary = base_salary
    
    # Join date with some format inconsistencies
    start_date = datetime.now() - timedelta(days=np.random.randint(30, 2000))
    if i % 35 == 0:  # Some different date formats
        join_date = start_date.strftime("%d/%m/%Y")
    else:
        join_date = start_date.strftime("%Y-%m-%d")
    
    # City
    city = random.choice(cities)
    
    # Email with some formatting issues
    email = f"{name.replace(' ', '.').lower()}@company.com"
    if i % 22 == 0:  # Some missing emails
        email = None
    elif i % 28 == 0:  # Some invalid emails
        email = "invalid_email"
    
    # Performance rating (1-5)
    performance = np.random.randint(1, 6)
    if i % 33 == 0:  # Some missing ratings
        performance = None
    
    data.append([emp_id, name, age, dept, position, salary, join_date, city, email, performance])

# Create DataFrame
columns = ['Employee_ID', 'Name', 'Age', 'Department', 'Position', 'Salary', 'Join_Date', 'City', 'Email', 'Performance_Rating']
df = pd.DataFrame(data, columns=columns)

# Save original data
df.to_csv('d:/PythonBatch3/PythonBatch3/Day12/employee_data_raw.csv', index=False)
print(f"✓ Created dataset with {len(df)} employee records")
print("\nFirst 5 rows of raw data:")
print(df.head())

print("\n" + "=" * 60)
print("DATA QUALITY ASSESSMENT")
print("=" * 60)

# Step 2: Data Quality Assessment
print("\n1. BASIC INFORMATION:")
print(f"Dataset shape: {df.shape}")
print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")

print("\n2. DATA TYPES:")
print(df.dtypes)

print("\n3. MISSING VALUES:")
missing_data = df.isnull().sum()
missing_percentage = (missing_data / len(df)) * 100
missing_info = pd.DataFrame({
    'Missing_Count': missing_data,
    'Missing_Percentage': missing_percentage
})
print(missing_info[missing_info['Missing_Count'] > 0])

print("\n4. DUPLICATE RECORDS:")
duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

print("\n5. DATA RANGE ANALYSIS:")
print(df.describe())

print("\n" + "=" * 60)
print("DATA CLEANING PROCESS")
print("=" * 60)

# Step 3: Data Cleaning
df_clean = df.copy()

print("\n1. CLEANING NAME COLUMN:")
# Remove extra spaces from names
df_clean['Name'] = df_clean['Name'].str.strip()
print("✓ Removed extra spaces from names")

print("\n2. CLEANING DEPARTMENT COLUMN:")
# Standardize department names
df_clean['Department'] = df_clean['Department'].str.title()
print("✓ Standardized department names")

print("\n3. HANDLING MISSING AND INVALID AGES:")
# Fill missing ages with median age by department
age_by_dept = df_clean.groupby('Department')['Age'].median()
df_clean['Age'] = df_clean['Age'].replace(0, np.nan)  # Replace 0 with NaN
for dept in df_clean['Department'].unique():
    mask = (df_clean['Department'] == dept) & (df_clean['Age'].isnull())
    df_clean.loc[mask, 'Age'] = age_by_dept[dept]
print("✓ Filled missing ages with department median")

print("\n4. HANDLING SALARY ISSUES:")
# Remove unrealistic low salaries and fill missing values
df_clean.loc[df_clean['Salary'] < 15000, 'Salary'] = np.nan
salary_by_position = df_clean.groupby(['Department', 'Position'])['Salary'].median()

for (dept, pos) in salary_by_position.index:
    mask = (df_clean['Department'] == dept) & (df_clean['Position'] == pos) & (df_clean['Salary'].isnull())
    if mask.sum() > 0:
        df_clean.loc[mask, 'Salary'] = salary_by_position[(dept, pos)]
print("✓ Fixed salary issues and filled missing values")

print("\n5. STANDARDIZING DATE FORMAT:")
# Convert all dates to standard format
def parse_date(date_str):
    try:
        if '/' in str(date_str):
            return pd.to_datetime(date_str, format='%d/%m/%Y')
        else:
            return pd.to_datetime(date_str, format='%Y-%m-%d')
    except:
        return pd.NaT

df_clean['Join_Date'] = df_clean['Join_Date'].apply(parse_date)
print("✓ Standardized date formats")

print("\n6. CLEANING EMAIL ADDRESSES:")
# Remove invalid emails and generate missing ones
valid_email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
invalid_emails = ~df_clean['Email'].str.contains(valid_email_pattern, na=True)
df_clean.loc[invalid_emails, 'Email'] = np.nan

# Generate emails for missing values
missing_email_mask = df_clean['Email'].isnull()
for idx in df_clean[missing_email_mask].index:
    name = df_clean.loc[idx, 'Name'].replace(' ', '.').lower()
    df_clean.loc[idx, 'Email'] = f"{name}@company.com"
print("✓ Fixed and generated email addresses")

print("\n7. HANDLING MISSING PERFORMANCE RATINGS:")
# Fill missing performance ratings with department average
perf_by_dept = df_clean.groupby('Department')['Performance_Rating'].mean()
for dept in df_clean['Department'].unique():
    mask = (df_clean['Department'] == dept) & (df_clean['Performance_Rating'].isnull())
    df_clean.loc[mask, 'Performance_Rating'] = round(perf_by_dept[dept])
print("✓ Filled missing performance ratings")

print("\n" + "=" * 60)
print("DATA MANIPULATION AND ANALYSIS")
print("=" * 60)

# Step 4: Data Manipulation and Analysis
print("\n1. CREATING DERIVED COLUMNS:")

# Calculate years of experience
df_clean['Years_Experience'] = ((datetime.now() - df_clean['Join_Date']).dt.days / 365.25).round(1)

# Create salary bands
def salary_band(salary):
    if salary < 50000:
        return 'Entry Level'
    elif salary < 80000:
        return 'Mid Level'
    elif salary < 120000:
        return 'Senior Level'
    else:
        return 'Executive Level'

df_clean['Salary_Band'] = df_clean['Salary'].apply(salary_band)

# Create age groups
def age_group(age):
    if age < 30:
        return '20-29'
    elif age < 40:
        return '30-39'
    elif age < 50:
        return '40-49'
    else:
        return '50+'

df_clean['Age_Group'] = df_clean['Age'].apply(age_group)

print("✓ Created derived columns: Years_Experience, Salary_Band, Age_Group")

print("\n2. DEPARTMENT WISE ANALYSIS:")
dept_analysis = df_clean.groupby('Department').agg({
    'Salary': ['mean', 'median', 'min', 'max'],
    'Age': 'mean',
    'Years_Experience': 'mean',
    'Performance_Rating': 'mean',
    'Employee_ID': 'count'
}).round(2)

dept_analysis.columns = ['Avg_Salary', 'Median_Salary', 'Min_Salary', 'Max_Salary', 
                        'Avg_Age', 'Avg_Experience', 'Avg_Performance', 'Employee_Count']
print(dept_analysis)

print("\n3. SALARY DISTRIBUTION BY EXPERIENCE:")
salary_exp = df_clean.groupby('Salary_Band').agg({
    'Years_Experience': ['mean', 'min', 'max'],
    'Employee_ID': 'count'
}).round(2)
salary_exp.columns = ['Avg_Experience', 'Min_Experience', 'Max_Experience', 'Count']
print(salary_exp)

print("\n4. CITY WISE EMPLOYEE DISTRIBUTION:")
city_dist = df_clean['City'].value_counts()
city_percentage = (city_dist / len(df_clean) * 100).round(2)
city_analysis = pd.DataFrame({
    'Employee_Count': city_dist,
    'Percentage': city_percentage
})
print(city_analysis)

print("\n5. PERFORMANCE ANALYSIS:")
perf_analysis = df_clean.groupby('Performance_Rating').agg({
    'Salary': 'mean',
    'Years_Experience': 'mean',
    'Employee_ID': 'count'
}).round(2)
perf_analysis.columns = ['Avg_Salary', 'Avg_Experience', 'Employee_Count']
print(perf_analysis)

print("\n" + "=" * 60)
print("ADVANCED DATA OPERATIONS")
print("=" * 60)

print("\n1. TOP PERFORMERS BY DEPARTMENT:")
top_performers = df_clean[df_clean['Performance_Rating'] >= 4].groupby('Department').agg({
    'Employee_ID': 'count',
    'Salary': 'mean'
}).round(2)
top_performers.columns = ['High_Performers', 'Avg_Salary_High_Performers']
print(top_performers)

print("\n2. SALARY OUTLIERS DETECTION:")
Q1 = df_clean['Salary'].quantile(0.25)
Q3 = df_clean['Salary'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df_clean[(df_clean['Salary'] < lower_bound) | (df_clean['Salary'] > upper_bound)]
print(f"Found {len(outliers)} salary outliers")
if len(outliers) > 0:
    print("Outliers:")
    print(outliers[['Employee_ID', 'Name', 'Department', 'Position', 'Salary']].head())

print("\n3. EMPLOYEES DUE FOR PROMOTION (High performance + experience):")
promotion_candidates = df_clean[
    (df_clean['Performance_Rating'] >= 4) & 
    (df_clean['Years_Experience'] >= 2) &
    (df_clean['Position'].isin(['Junior', 'Analyst']))
]
print(f"Found {len(promotion_candidates)} promotion candidates")
if len(promotion_candidates) > 0:
    print("Candidates:")
    print(promotion_candidates[['Employee_ID', 'Name', 'Department', 'Position', 
                               'Years_Experience', 'Performance_Rating']].head())

print("\n4. DEPARTMENT WISE RETENTION ANALYSIS:")
avg_experience_by_dept = df_clean.groupby('Department')['Years_Experience'].mean().sort_values(ascending=False)
print("Average experience by department (indicates retention):")
print(avg_experience_by_dept.round(2))

# Step 5: Save cleaned and analyzed data
print("\n" + "=" * 60)
print("SAVING RESULTS")
print("=" * 60)

# Save cleaned data
df_clean.to_csv('d:/PythonBatch3/PythonBatch3/Day12/employee_data_cleaned.csv', index=False)
print("✓ Saved cleaned dataset")

# Save analysis results
with pd.ExcelWriter('d:/PythonBatch3/PythonBatch3/Day12/employee_analysis_results.xlsx') as writer:
    df_clean.to_excel(writer, sheet_name='Cleaned_Data', index=False)
    dept_analysis.to_excel(writer, sheet_name='Department_Analysis')
    city_analysis.to_excel(writer, sheet_name='City_Analysis')
    perf_analysis.to_excel(writer, sheet_name='Performance_Analysis')
    if len(promotion_candidates) > 0:
        promotion_candidates.to_excel(writer, sheet_name='Promotion_Candidates', index=False)

print("✓ Saved analysis results to Excel file")

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"✓ Successfully processed {len(df)} employee records")
print(f"✓ Cleaned and standardized all data fields")
print(f"✓ Created {len(df_clean.columns) - len(df.columns)} new derived columns")
print(f"✓ Generated comprehensive analysis across multiple dimensions")
print(f"✓ Identified {len(promotion_candidates)} promotion candidates")
print(f"✓ Detected {len(outliers)} salary outliers")
print("✓ All results saved to CSV and Excel files")

print("\nCleaned data shape:", df_clean.shape)
print("Missing values after cleaning:", df_clean.isnull().sum().sum())