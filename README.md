# Week 3 - Python & Data Wrangling

## Overview

This project demonstrates basic Python data analysis and data wrangling using Pandas, along with data visualization using Matplotlib and Seaborn.

## Dataset

The dataset contains workout-related information such as:

- Duration
- Date
- Pulse
- Maximum Pulse
- Calories

## Tasks Performed

### 1. Data Loading
- Loaded the CSV dataset using Pandas.
- Inspected the dataset structure and information.

### 2. Data Cleaning
- Checked for missing values.
- Handled missing Date values.
- Filled missing Calories values using the mean.
- Removed duplicate records.
- Converted the Date column into a proper datetime format.

### 3. Data Filtering
Filtered workout records where the duration was greater than 50 minutes.

### 4. New Column Creation
Created a new column:

`Calories_Per_Minute`

This calculates the calories burned per minute of workout.

### 5. Data Analysis
Calculated:
- Average Duration
- Average Calories
- Maximum Calories
- Minimum Calories
- Average Pulse

### 6. Data Visualization

Created two visualizations:

- Duration vs Calories — Scatter Plot
- Calories Distribution — Box Plot

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn

## Files

- `data.csv` - Original dataset
- `cleaned_data.csv` - Cleaned dataset
- `task3.py` - Python script
- `visualizations/` - Generated charts

## Conclusion

The dataset was successfully cleaned and analyzed using Pandas. Missing values and duplicate records were handled, additional information was derived using a new column, and visualizations were created to understand the workout data.