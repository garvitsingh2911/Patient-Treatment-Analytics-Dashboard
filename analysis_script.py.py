import pandas as pd
import matplotlib.pyplot as plt
import sqlite3 #for fetching data we use it

# Step 1: Load the CSV
df = pd.read_csv('medtour_data.csv')

# Step 2: Explore the data
print(df.head())
print(df.info())
print(df.describe())
print(df['Status'].value_counts())

# Step 3: Clean the data
# Fill missing ratings with 0 or NaN (based on your preference)
df['Patient_Rating'] = pd.to_numeric(df['Patient_Rating'], errors='coerce')

# Step 4: Insights

# 1. Average treatment cost
avg_cost = df['Treatment_Cost'].mean()
print(f"\nAverage Treatment Cost: ₹{avg_cost:.2f}")

# 2. Treatments with highest average cost
print("\nAverage Cost by Treatment Type:")
print(df.groupby('Treatment_Type')['Treatment_Cost'].mean().sort_values(ascending=False))

# 3. Most popular hospitals
print("\nMost Popular Hospitals:")
print(df['Hospital_Name'].value_counts())

# 4. Status distribution pie chart
df['Status'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, title='Booking Status Distribution')
plt.ylabel('')
plt.show()

# 5. Country-wise treatment count
df['Country'].value_counts().plot(kind='bar', color='skyblue', title='Patients by Country')
plt.xlabel('Country')
plt.ylabel('Number of Patients')
plt.show()
 



# ######################sql part


import sqlite3

# Load CSV
df = pd.read_csv('medtour_data.csv')

# Connect to SQLite and upload data
conn = sqlite3.connect('medtour_project.db')
df.to_sql('medtour', conn, if_exists='replace', index=False)

# Query examples
query1 = "SELECT Country, COUNT(*) AS Patient_Count FROM medtour GROUP BY Country ORDER BY Patient_Count DESC;"
query2 = "SELECT Treatment_Type, AVG(Treatment_Cost) AS Avg_Cost FROM medtour GROUP BY Treatment_Type ORDER BY Avg_Cost DESC;"
query3 = "SELECT Hospital_Name, COUNT(*) AS Total_Patients FROM medtour GROUP BY Hospital_Name ORDER BY Total_Patients DESC;"
query4 = "SELECT Status, COUNT(*) AS Status_Count FROM medtour GROUP BY Status;"
query5 = "SELECT AVG(Patient_Rating) AS Avg_Rating FROM medtour WHERE Status = 'Completed';"

# Run and print results
for q in [query1, query2, query3, query4, query5]:
    print(pd.read_sql_query(q, conn))
