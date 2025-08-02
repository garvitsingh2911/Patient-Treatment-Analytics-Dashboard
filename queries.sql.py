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
