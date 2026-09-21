# Student Productivity Analysis (Mini Project) - Python

## Overview
Analysis of a dataset of 10,000 students to understand which habits and
factors relate to productivity and academic performance.

## Dataset
- 10,000 rows and 20 columns
- Includes study hours, sleep, screen time, social media use, attendance,
  stress, motivation, AI tool usage, previous GPA, productivity score and
  performance category (Low / Medium / High)

## Steps Performed
1. Loaded and inspected the data (shape, data types, summary statistics)
2. Checked for duplicate rows (none found)
3. Handled missing values across 16 columns
4. Converted Age to integer and saved the cleaned dataset
5. Computed descriptive statistics (mean, median, min, max, std)
6. Analysed categorical distributions (gender, internet quality, part-time job)
7. Built a correlation matrix against Productivity Score

## Key Findings
- Sleep hours has the strongest positive correlation with productivity (~0.33)
- Motivation, assignments completed and attendance are each around 0.29-0.30
- Screen time (-0.22) and stress level (-0.21) correlate negatively
- AI tool usage shows almost no correlation with productivity (~0.00)
- Average productivity score is about 54.6 and is nearly identical across genders

## Tools Used
Python, pandas, NumPy, VS Code, Matplotlib

## How to Run
pip install pandas numpy
python Student_Productivity_Analysis.py
