
🏥Patient-Treatment-Analytics-Dashboard

🛠️Tools Used: SQL · Python (Pandas) · Power BI

🎯 Project Objective:

This project analyzes a simulated dataset of 100 international patients seeking treatments in India. Using SQL and Python for data processing and Power BI for visualization, I derived insights about:
.Booking trends
.Patient demographics
.Treatment cost distribution
.Hospital popularity and patient ratings

📁 Dataset Overview

Column Name::Description

Patient_ID::Unique ID for each patient

Country::Patient's country of origin

Treatment_Type::	Type of medical treatment required

Treatment_Cost::	Cost of the treatment

Hospital_Name::	Hospital assigned for the treatment

Booking_Date::	Date when treatment was booked

Status	Status of booking:: Booked, Completed, Cancelled

Patient_Rating::	Patient feedback on a scale of 1 to 5 (optional)


📊 Dashboard Insights<img width="1913" height="1016" alt="Screenshot 2025-08-02 074635" src="https://github.com/user-attachments/assets/b13052ae-d459-4e09-8d81-ba75531e1c43" />

1-Booking Status Distribution
37% Completed
15% Cancelled
48% Booked

2-Average Treatment Cost by Type
Highest: Liver Transplant
Lowest: Dental Implants

3-Patients by Country
Majority from India, followed by USA and Bangladesh

4-Hospital Bookings & Ratings
Most visited: Medanta Gurgaon & Apollo Hospitals
High-rated: Tata Memorial & Artemis Gurgaon


⚙ Code Highlights:

Python: Used to clean missing values and analyze average ratings and cost per treatment(Pandas,matplotlib).

SQL: Queried booking status counts and treatment averages.

Power BI: Created a dashboard combining all metrics into visual tiles.


📌 How to Run
1.Load the medtour_data.csv file into Python.
2.Use the SQL scripts to extract and preprocess insights.
3.Load cleaned data into Power BI to replicate the dashboard.



📂 Files in This Repo

medtour_data.csv — Raw dataset
analysis_script.py — Python data analysis code
queries.sql — SQL queries used for summarization
mdtour_project.pdf — Final Power BI dashboard
demo_video.mp4--data analysis on vs code


🧠 Key Learnings
-Creating ETL pipelines across tools
-Understanding how to combine structured SQL logic with Python flexibility
-Data visualization principles in Power BI





