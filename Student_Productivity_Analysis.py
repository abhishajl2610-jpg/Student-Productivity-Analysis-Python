import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------------------------------------------

df = pd.read_excel("C:/Users/abish/Desktop/DA GenAI/Project/Student Productivity Analysis (Mini Project) - Python/Student_Productivity_Dataset.xlsx")
print("Dataset Loaded Successfully!")

# ----------------------------------------------------------------------------------------------------------------

print(df.head())
print(df.tail())
print("Shape of Dataset:", df.shape)
print(df.columns)
print(df.dtypes)
df.info()
print(df.describe())

# ----------------------------------------------------------------------------------------------------------------

print("Duplicate Rows:", df.duplicated().sum())
df = df.drop_duplicates()
print("Duplicate Rows:", df.duplicated().sum())

# ----------------------------------------------------------------------------------------------------------------

print(df.isnull().sum())
print("Missing Values Before Cleaning")
print(df.isnull().sum())
numerical_columns = [
    "Age",
    "Study_Hours_Per_Day",
    "Sleep_Hours_Per_Night",
    "Screen_Time_Hours",
    "Social_Media_Hours",
    "Attendance_Percentage",
    "Assignments_Completed",
    "Class_Participation_Score",
    "Physical_Activity_Hours_Per_Week",
    "Stress_Level",
    "Motivation_Level",
    "Extracurricular_Involvement",
    "AI_Tool_Usage_Hours_Per_Week",
    "Previous_Semester_GPA"
]

for col in numerical_columns:
    df[col] = df[col].fillna(df[col].median())

categorical_columns = [
    "Gender",
    "Internet_Quality",
    "Part_Time_Job"
]

for col in categorical_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

print("Missing Values After Cleaning")
print(df.isnull().sum())

# ----------------------------------------------------------------------------------------------------------------

df["Age"] = df["Age"].astype(int)

print(df.dtypes)

# ----------------------------------------------------------------------------------------------------------------

df.to_excel(
    "C:/Users/abish/Desktop/DA GenAI/Project/Student Productivity Analysis (Mini Project) - Python/Student_Productivity_Cleaned.xlsx",
    index=False
)

print("Cleaned Dataset Saved Successfully!")

# ----------------------------------------------------------------------------------------------------------------

#Total Number of Students
print("Total Number of Students :", len(df))

#Age Analysis
print("Average Age :", df["Age"].mean())
print("Median Age :", df["Age"].median())
print("Minimum Age :", df["Age"].min())
print("Maximum Age :", df["Age"].max())
print("Standard Deviation :", df["Age"].std())

# Study Hours Analysis
print("Average Study Hours :", df["Study_Hours_Per_Day"].mean())
print("Maximum Study Hours :", df["Study_Hours_Per_Day"].max())
print("Minimum Study Hours :", df["Study_Hours_Per_Day"].min())

# Sleep Hours Analysis
print("Average Sleep Hours :", df["Sleep_Hours_Per_Night"].mean())
print("Maximum Sleep Hours :", df["Sleep_Hours_Per_Night"].max())
print("Minimum Sleep Hours :", df["Sleep_Hours_Per_Night"].min())

# Attendance Analysis
print("Average Attendance :", df["Attendance_Percentage"].mean())
print("Highest Attendance :", df["Attendance_Percentage"].max())
print("Lowest Attendance :", df["Attendance_Percentage"].min())

# Productivity Score Analysis
print("Average Productivity Score :", df["Productivity_Score"].mean())
print("Highest Productivity Score :", df["Productivity_Score"].max())
print("Lowest Productivity Score :", df["Productivity_Score"].min())

# Previous Semester GPA
print("Average GPA :", df["Previous_Semester_GPA"].mean())
print("Highest GPA :", df["Previous_Semester_GPA"].max())
print("Lowest GPA :", df["Previous_Semester_GPA"].min())

# NumPy Calculations
# Converting the Age column to a NumPy array
age = np.array(df["Age"])

print("Average Age :", np.mean(age))
print("Median Age :", np.median(age))
print("Maximum Age :", np.max(age))
print("Minimum Age :", np.min(age))
print("Standard Deviation :", np.std(age))

# Gender Count
print(df["Gender"].value_counts())

# Internet Quality Count
print(df["Internet_Quality"].value_counts())

# Part-Time Job Count
print(df["Part_Time_Job"].value_counts())

# Performance Category Count
print(df["Performance_Category"].value_counts())

# Group By Analysis
# Average Productivity by Gender
print(df.groupby("Gender")["Productivity_Score"].mean())

# Average Study Hours by Gender
print(df.groupby("Gender")["Study_Hours_Per_Day"].mean())

# Average GPA by Internet Quality
print(df.groupby("Internet_Quality")["Previous_Semester_GPA"].mean())

# Correlation Matrix
correlation = df.select_dtypes(include="number").corr()
print(correlation)

df.to_excel(
    "C:/Users/abish/Desktop/DA GenAI/Project/Student Productivity Analysis (Mini Project) - Python/Student_Productivity_Final.xlsx",
    index=False
)

print("Final Dataset Saved Successfully!")

# ----------------------------------------------------------------------------------------------------------------

# Age Distribution (Histogram)
plt.figure(figsize=(8,5))
plt.hist(df["Age"], bins=15, edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Students")
plt.grid(True)
plt.show()

# Gender Distribution (Bar Chart)
gender = df["Gender"].value_counts()

plt.figure(figsize=(6,5))
plt.bar(gender.index, gender.values)
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# Performance Category (Pie Chart)
performance = df["Performance_Category"].value_counts()

plt.figure(figsize=(7,7))
plt.pie(performance.values,
        labels=performance.index,
        autopct="%1.1f%%",
        startangle=90)

plt.title("Performance Category")
plt.show()

# Study Hours vs Productivity (Scatter Plot)
plt.figure(figsize=(8,5))
plt.scatter(df["Study_Hours_Per_Day"],
            df["Productivity_Score"])

plt.title("Study Hours vs Productivity")
plt.xlabel("Study Hours Per Day")
plt.ylabel("Productivity Score")
plt.show()

# Attendance Distribution
plt.figure(figsize=(8,5))
plt.hist(df["Attendance_Percentage"],
         bins=15,
         edgecolor="black")

plt.title("Attendance Percentage")
plt.xlabel("Attendance")
plt.ylabel("Students")
plt.show()

# Screen Time vs Productivity
plt.figure(figsize=(8,5))
plt.scatter(df["Screen_Time_Hours"],
            df["Productivity_Score"])

plt.title("Screen Time vs Productivity")
plt.xlabel("Screen Time")
plt.ylabel("Productivity")
plt.show()

# Sleep Hours (Box Plot)
plt.figure(figsize=(6,5))
plt.boxplot(df["Sleep_Hours_Per_Night"])

plt.title("Sleep Hours Per Night")
plt.ylabel("Hours")
plt.show()

# Average Productivity by Gender
gender_productivity = df.groupby("Gender")["Productivity_Score"].mean()

plt.figure(figsize=(6,5))
plt.bar(gender_productivity.index,
        gender_productivity.values)

plt.title("Average Productivity by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Productivity")
plt.show()

# Stress Level Distribution
plt.figure(figsize=(8,5))
plt.hist(df["Stress_Level"],
         bins=10,
         edgecolor="black")

plt.title("Stress Level Distribution")
plt.xlabel("Stress Level")
plt.ylabel("Students")
plt.show()

# Correlation Heatmap (without Seaborn)

correlation = df.select_dtypes(include="number").corr()

plt.figure(figsize=(12,8))
plt.imshow(correlation, cmap="coolwarm", aspect="auto")

plt.colorbar()

plt.xticks(range(len(correlation.columns)),
           correlation.columns,
           rotation=90)

plt.yticks(range(len(correlation.columns)),
           correlation.columns)

plt.title("Correlation Matrix")

plt.show()

# ----------------------------------------------------------------------------------------------------------------

df.to_excel(
    "C:/Users/abish/Desktop/DA GenAI/Project/Student Productivity Analysis (Mini Project) - Python/Student_Productivity_Final.xlsx",
    index=False
)

print("Project Completed Successfully!")

# ----------------------------------------------------------------------------------------------------------------
