import pandas as pd

# Load the dataset
df = pd.read_csv("data.csv")

# Display first 5 rows
print(df.head())

# Check dataset information
print(df.info())

# Check basic statistics
print(df.describe())


# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Show rows with missing values
print("\nRows with missing values:")
print(df[df.isnull().any(axis=1)])

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"], format="mixed")

# Fill missing Date using interpolation
df["Date"] = df["Date"].interpolate()

# Calculate mean Calories
calories_mean = df["Calories"].mean()

# Fill missing Calories with mean
df["Calories"] = df["Calories"].fillna(calories_mean)

# Display cleaned missing-value count
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Check for duplicate rows
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# Display duplicate rows
print("\nDuplicate row:")
print(df[df.duplicated()])

# Remove duplicate rows
df = df.drop_duplicates()

# Check duplicates again
print("\nDuplicates after cleaning:")
print(df.duplicated().sum())

# Filter records where Duration is greater than 50 minutes
filtered_data = df[df["Duration"] > 50]

print("\nRecords with Duration greater than 50 minutes:")
print(filtered_data)

# Create a new column: Calories per Minute
df["Calories_Per_Minute"] = df["Calories"] / df["Duration"]

# Display the new column
print("\nCalories burned per minute:")
print(df[["Duration", "Calories", "Calories_Per_Minute"]].head())

# Basic data analysis

print("\nAverage Duration:")
print(df["Duration"].mean())

print("\nAverage Calories:")
print(df["Calories"].mean())

print("\nMaximum Calories:")
print(df["Calories"].max())

print("\nMinimum Calories:")
print(df["Calories"].min())

print("\nAverage Pulse:")
print(df["Pulse"].mean())

import matplotlib.pyplot as plt
import os

# Create visualizations folder
os.makedirs("visualizations", exist_ok=True)

# Create scatter plot
plt.scatter(df["Duration"], df["Calories"])

# Add labels and title
plt.xlabel("Duration (minutes)")
plt.ylabel("Calories Burned")
plt.title("Duration vs Calories")

# Save the chart
plt.savefig("visualizations/duration_vs_calories.png", dpi=300, bbox_inches="tight")

# Display the chart
plt.show()

# Close the plot
plt.close()

import seaborn as sns
import matplotlib.pyplot as plt

# Create Seaborn box plot
sns.boxplot(y=df["Calories"])

plt.title("Distribution of Calories Burned")
plt.ylabel("Calories")

# Save the chart
plt.savefig(
    "visualizations/calories_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

# Display the chart
plt.show()

# Close the plot
plt.close()

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned dataset saved successfully!")