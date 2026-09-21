# Student Productivity Analysis (Mini Project) - Python

## Overview
This project analyses a dataset of 10,000 students to understand which habits
and factors are linked to productivity and academic performance. It covers
data cleaning, descriptive statistics, group-wise analysis, correlation
analysis and data visualisation using Python.

## Dataset
- 10,000 students and 20 columns
- Columns include age, gender, study hours, sleep hours, screen time, social
  media hours, attendance, assignments completed, class participation,
  physical activity, stress level, motivation level, internet quality,
  part-time job, extracurricular involvement, AI tool usage, previous semester
  GPA, productivity score and performance category (Low / Medium / High)

## Project Workflow
1. **Data loading and exploration**: shape, column names, data types, info and summary statistics
2. **Duplicate check**: no duplicate rows were found
3. **Missing value treatment**: median for numerical columns, mode for categorical columns
4. **Data type conversion**: Age converted to integer
5. **Descriptive statistics**: mean, median, min, max and standard deviation using pandas and NumPy
6. **Category counts**: gender, internet quality, part-time job and performance category
7. **Group-by analysis**: productivity and study hours by gender, GPA by internet quality
8. **Correlation analysis**: correlation matrix of all numerical variables
9. **Visualisation**: 10 charts (see below)
10. **Export**: cleaned and final datasets saved as Excel files

## Visualisations
- Age distribution (histogram)
- Gender distribution (bar chart)
- Performance category (pie chart)
- Study hours vs productivity (scatter plot)
- Attendance distribution (histogram)
- Screen time vs productivity (scatter plot)
- Sleep hours per night (box plot)
- Average productivity by gender (bar chart)
- Stress level distribution (histogram)
- Correlation heatmap

## Key Findings
- Average productivity score is about 54.6 out of 100
- Sleep hours has the strongest positive correlation with productivity (about 0.33)
- Motivation, assignments completed and attendance each correlate at about 0.29 to 0.30
- Screen time (-0.22) and stress level (-0.21) correlate negatively with productivity
- AI tool usage shows almost no correlation with productivity
- Average productivity is nearly the same across genders (about 54.5 to 54.9)
- Performance categories: 50% Medium, 25% High, 25% Low

## Tools Used
Python, pandas, NumPy, Matplotlib, VS Code

## Project Structure
```
├── Student_Productivity_Analysis.py
├── Student_Productivity_Dataset.xlsx
├── Student_Productivity_Cleaned.xlsx
├── Student_Productivity_Final.xlsx
├── charts/
└── README.md
```

## How to Run
1. Install the libraries:
   `pip install pandas numpy matplotlib openpyxl`
2. Update the file paths in the script to match your folder.
3. Run:
   `python Student_Productivity_Analysis.py`
