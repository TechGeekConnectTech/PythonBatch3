import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

print("=" * 70)
print("NUMPY REAL-TIME EXAMPLES FOR STUDENTS")
print("=" * 70)

# Example 1: Student Grade Analysis System
print("\n1. STUDENT GRADE ANALYSIS SYSTEM")
print("=" * 50)

# Create student data (5 students, 4 subjects)
np.random.seed(42)
students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
subjects = ['Math', 'Physics', 'Chemistry', 'Biology']

# Generate random grades (0-100)
grades = np.random.randint(60, 100, size=(5, 4))
print("Original Grades Matrix:")
print("Students:", students)
print("Subjects:", subjects)
print("Grades:\n", grades)

# Calculate statistics using NumPy
print("\nGRADE ANALYSIS:")
print(f"Average grade per student: {np.mean(grades, axis=1).round(2)}")
print(f"Average grade per subject: {np.mean(grades, axis=0).round(2)}")
print(f"Highest grade: {np.max(grades)}")
print(f"Lowest grade: {np.min(grades)}")
print(f"Overall class average: {np.mean(grades):.2f}")

# Find top performers
top_students = np.argmax(np.mean(grades, axis=1))
print(f"Top performing student: {students[top_students]}")

# Subject difficulty analysis
subject_difficulty = np.mean(grades, axis=0)
easiest_subject = np.argmax(subject_difficulty)
hardest_subject = np.argmin(subject_difficulty)
print(f"Easiest subject: {subjects[easiest_subject]} (avg: {subject_difficulty[easiest_subject]:.1f})")
print(f"Hardest subject: {subjects[hardest_subject]} (avg: {subject_difficulty[hardest_subject]:.1f})")

# Example 2: Library Book Management System
print("\n\n2. LIBRARY BOOK MANAGEMENT SYSTEM")
print("=" * 50)

# Book data: [Book_ID, Pages, Rating, Price]
books_data = np.array([
    [101, 250, 4.2, 15.99],
    [102, 180, 3.8, 12.50],
    [103, 320, 4.7, 22.00],
    [104, 150, 3.5, 9.99],
    [105, 400, 4.9, 28.50],
    [106, 200, 4.0, 16.75],
    [107, 275, 4.3, 19.25],
    [108, 350, 4.6, 25.00]
])

book_ids = books_data[:, 0].astype(int)
pages = books_data[:, 1]
ratings = books_data[:, 2]
prices = books_data[:, 3]

print("LIBRARY STATISTICS:")
print(f"Total books: {len(books_data)}")
print(f"Average pages: {np.mean(pages):.0f}")
print(f"Average rating: {np.mean(ratings):.2f}")
print(f"Average price: ${np.mean(prices):.2f}")

# Find books based on criteria
high_rated = books_data[ratings >= 4.5]
print(f"\nHigh-rated books (>=4.5): {len(high_rated)} books")
print("Book IDs:", high_rated[:, 0].astype(int))

affordable_books = books_data[prices <= 20.00]
print(f"Affordable books (<=20$): {len(affordable_books)} books")

# Best value books (high rating, reasonable price)
value_score = ratings / (prices / 10)  # Rating per $10
best_value_idx = np.argmax(value_score)
print(f"Best value book ID: {int(book_ids[best_value_idx])}")

# Example 3: Student Attendance Tracking
print("\n\n3. STUDENT ATTENDANCE TRACKING SYSTEM")
print("=" * 50)

# 30 days of attendance for 20 students (1=present, 0=absent)
np.random.seed(123)
attendance = np.random.choice([0, 1], size=(20, 30), p=[0.15, 0.85])  # 15% absence rate

print("Attendance Matrix Shape:", attendance.shape)
print("Sample attendance (first 5 students, first 10 days):")
print(attendance[:5, :10])

# Calculate attendance statistics
attendance_percentage = (np.sum(attendance, axis=1) / 30) * 100
print(f"\nAttendance Statistics:")
print(f"Class average attendance: {np.mean(attendance_percentage):.1f}%")
print(f"Best attendance: {np.max(attendance_percentage):.1f}%")
print(f"Worst attendance: {np.min(attendance_percentage):.1f}%")

# Students with low attendance (< 75%)
low_attendance = np.where(attendance_percentage < 75)[0]
print(f"Students with low attendance: {len(low_attendance)} students")
print(f"Student IDs: {low_attendance + 1}")  # +1 for 1-based indexing

# Daily attendance rates
daily_rates = (np.sum(attendance, axis=0) / 20) * 100
worst_day = np.argmin(daily_rates)
best_day = np.argmax(daily_rates)
print(f"Worst attendance day: Day {worst_day + 1} ({daily_rates[worst_day]:.1f}%)")
print(f"Best attendance day: Day {best_day + 1} ({daily_rates[best_day]:.1f}%)")

# Example 4: Sports Team Performance Analysis
print("\n\n4. SPORTS TEAM PERFORMANCE ANALYSIS")
print("=" * 50)

# Basketball team stats: [Points, Rebounds, Assists, Steals]
players = ['Player1', 'Player2', 'Player3', 'Player4', 'Player5']
np.random.seed(456)

# Generate 10 games worth of data
games = 10
team_stats = np.random.randint(0, 30, size=(5, 4, games))  # 5 players, 4 stats, 10 games

print("Team Performance Analysis (10 games):")

# Calculate season averages for each player
season_averages = np.mean(team_stats, axis=2)
print("\nSeason Averages per player:")
stat_names = ['Points', 'Rebounds', 'Assists', 'Steals']
for i, player in enumerate(players):
    print(f"{player}: {dict(zip(stat_names, season_averages[i].round(1)))}")

# Team totals per game
team_totals = np.sum(team_stats, axis=0)
print(f"\nTeam averages per game:")
for i, stat in enumerate(stat_names):
    print(f"{stat}: {np.mean(team_totals[i]):.1f}")

# Find MVP (Most Valuable Player) based on total contribution
player_total_contribution = np.sum(season_averages, axis=1)
mvp_idx = np.argmax(player_total_contribution)
print(f"\nMVP: {players[mvp_idx]} (Total avg: {player_total_contribution[mvp_idx]:.1f})")

# Example 5: School Cafeteria Menu Optimization
print("\n\n5. SCHOOL CAFETERIA MENU OPTIMIZATION")
print("=" * 50)

# Food items: [Calories, Protein(g), Cost($), Student_Rating(1-5)]
menu_items = np.array([
    [350, 15, 3.50, 4.2],  # Burger
    [180, 8, 2.25, 3.8],   # Salad
    [420, 12, 4.00, 4.5],  # Pizza
    [280, 20, 3.75, 4.0],  # Chicken wrap
    [150, 5, 1.50, 3.2],   # Fruit cup
    [320, 10, 2.80, 3.9],  # Pasta
    [200, 6, 2.00, 3.5],   # Soup
    [380, 18, 4.25, 4.3]   # Fish sandwich
])

food_names = ['Burger', 'Salad', 'Pizza', 'Chicken Wrap', 'Fruit Cup', 'Pasta', 'Soup', 'Fish Sandwich']

calories = menu_items[:, 0]
protein = menu_items[:, 1]
cost = menu_items[:, 2]
rating = menu_items[:, 3]

print("CAFETERIA MENU ANALYSIS:")
print(f"Average calories: {np.mean(calories):.0f}")
print(f"Average protein: {np.mean(protein):.1f}g")
print(f"Average cost: ${np.mean(cost):.2f}")
print(f"Average rating: {np.mean(rating):.2f}")

# Find healthy options (high protein, reasonable calories)
protein_per_calorie = protein / calories
healthy_threshold = np.percentile(protein_per_calorie, 75)  # Top 25%
healthy_options = np.where(protein_per_calorie >= healthy_threshold)[0]

print(f"\nHealthy options (high protein/calorie ratio):")
for idx in healthy_options:
    print(f"- {food_names[idx]} (Protein/Cal: {protein_per_calorie[idx]:.3f})")

# Budget-friendly high-rated items
value_items = np.where((cost <= np.mean(cost)) & (rating >= 4.0))[0]
print(f"\nBest value items (affordable + high rating):")
for idx in value_items:
    print(f"- {food_names[idx]} (${cost[idx]}, Rating: {rating[idx]})")

# Example 6: University Enrollment Prediction
print("\n\n6. UNIVERSITY ENROLLMENT TRENDS")
print("=" * 50)

# Historical enrollment data (last 10 years)
years = np.arange(2014, 2024)
np.random.seed(789)

# Base enrollment with growth trend and random variation
base_enrollment = 5000
growth_rate = 0.03  # 3% annual growth
enrollment = base_enrollment * (1 + growth_rate) ** (years - 2014)
# Add some random variation
enrollment = enrollment + np.random.normal(0, 100, len(years))
enrollment = enrollment.astype(int)

print("Historical Enrollment Data:")
for year, enroll in zip(years, enrollment):
    print(f"{year}: {enroll:,} students")

# Calculate statistics
avg_growth = np.mean(np.diff(enrollment))
total_growth = enrollment[-1] - enrollment[0]
growth_percentage = (total_growth / enrollment[0]) * 100

print(f"\nEnrollment Analysis:")
print(f"Average annual growth: {avg_growth:.0f} students")
print(f"Total growth (10 years): {total_growth:,} students ({growth_percentage:.1f}%)")
print(f"Peak enrollment: {np.max(enrollment):,} in {years[np.argmax(enrollment)]}")

# Predict next 3 years using linear trend
recent_trend = np.mean(np.diff(enrollment[-3:]))  # Last 3 years trend
future_years = np.array([2024, 2025, 2026])
predicted_enrollment = enrollment[-1] + recent_trend * np.arange(1, 4)

print(f"\nPredicted Enrollment:")
for year, pred in zip(future_years, predicted_enrollment):
    print(f"{year}: {int(pred):,} students (predicted)")

# Example 7: Student Survey Analysis
print("\n\n7. STUDENT SATISFACTION SURVEY")
print("=" * 50)

# Survey responses: [Teaching Quality, Campus Facilities, Food Quality, Overall Satisfaction]
# Scale: 1-5 (1=Poor, 5=Excellent)
np.random.seed(101112)
num_responses = 200
survey_data = np.random.randint(1, 6, size=(num_responses, 4))

categories = ['Teaching Quality', 'Campus Facilities', 'Food Quality', 'Overall Satisfaction']
print(f"Survey Analysis ({num_responses} responses):")

# Calculate averages and satisfaction levels
averages = np.mean(survey_data, axis=0)
for i, category in enumerate(categories):
    satisfaction_level = "Excellent" if averages[i] >= 4.5 else \
                        "Good" if averages[i] >= 4.0 else \
                        "Average" if averages[i] >= 3.0 else \
                        "Poor"
    print(f"{category}: {averages[i]:.2f} ({satisfaction_level})")

# Find correlation between categories
correlation_matrix = np.corrcoef(survey_data.T)
print(f"\nHighest correlation pairs:")
for i in range(len(categories)):
    for j in range(i+1, len(categories)):
        corr = correlation_matrix[i, j]
        print(f"{categories[i]} - {categories[j]}: {corr:.3f}")

# Calculate satisfaction distribution
overall_satisfaction = survey_data[:, 3]
satisfaction_counts = np.bincount(overall_satisfaction, minlength=6)[1:]  # Exclude 0
satisfaction_percentages = (satisfaction_counts / num_responses) * 100

print(f"\nOverall Satisfaction Distribution:")
ratings = ['Poor(1)', 'Fair(2)', 'Good(3)', 'Very Good(4)', 'Excellent(5)']
for rating, percentage in zip(ratings, satisfaction_percentages):
    print(f"{rating}: {percentage:.1f}%")

print("\n" + "=" * 70)
print("SUMMARY: WHY NUMPY IS POWERFUL FOR STUDENTS")
print("=" * 70)

advantages = [
    "1. FAST CALCULATIONS: NumPy operations are 10-100x faster than pure Python",
    "2. EASY STATISTICS: Built-in functions for mean, median, std, min, max",
    "3. MATRIX OPERATIONS: Perfect for handling grades, attendance, survey data",
    "4. DATA ANALYSIS: Foundation for pandas, matplotlib, and machine learning",
    "5. MEMORY EFFICIENT: Uses less memory than Python lists",
    "6. SCIENTIFIC COMPUTING: Used in physics, engineering, data science",
    "7. REAL WORLD APPLICATIONS: Used by Netflix, Google, NASA, universities"
]

for advantage in advantages:
    print(advantage)

print(f"\n✓ These examples show how NumPy helps analyze real student data efficiently!")
print("✓ NumPy is essential for any data science or engineering career!")