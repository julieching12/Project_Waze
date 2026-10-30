"""
The purpose of this project is to investigate and understand the data provided. This activity has three parts:
1: Understand the situation
2: Understand the data
3: Understand the variables

The goal is to use a dataframe contructed within Python, perform a cursory inspection of the provided dataset, and
inform team members of your findings.

NOTE: below codes are run in Jupyter Notebook environment.
"""

# Import packages for data manipulation
import pandas as pd
import numpy as np

# Load dataset into dataframe
df = pd.read_csv('waze_dataset.csv')

# Display and examine the first ten rows of the dataframe
df.head(10)

# Get summary info
df.info()

# Isolate rows with null values
null_data = df[df['label'].isnull()]
# Display summary stats of rows with null values
null_data.describe()

# Isolate rows without null values
#not_null_data = df[df['label'].notna()]
not_null_data = df[~df['label'].isnull()]
# Display summary stats of rows without null values
not_null_data.describe()

# Get count of null values by device
null_data['device'].value_counts()

# Calculate % of iPhone nulls and Android nulls
#null_data['device'].value_counts(normalize=True)*100
null_data['device'].value_counts(normalize=True)

# Calculate % of iPhone users and Android users in full dataset
#df['device'].value_counts(normalize=True)*100
df['device'].value_counts(normalize=True)

# Calculate counts of churned vs. retained
#df.groupby(['label']).count()[['ID']]   #count() counts for all columns, while value_counts() only count by categoried values
#df['label'].value_counts(normalize=True)*100

print(df['label'].value_counts())
print(df['label'].value_counts(normalize=True))

# Calculate median values of all columns for churned and retained users
#df.groupby(['label']).median()
df.groupby('label').median(numeric_only=True)

# Add a column to df called `km_per_drive`
df['km_per_drive'] = df['driven_km_drives'] / df['drives']
# Group by `label`, calculate the median, and isolate for km per drive
#df.groupby(['label'])[['km_per_drive']].median()
df.groupby('label').median(numeric_only=True)[['km_per_drive']]

# Add a column to df called `km_per_driving_day`
df['km_per_driving_day'] = df['driven_km_drives'] / df['driving_days']
# Group by `label`, calculate the median, and isolate for km per driving day
#df.groupby(['label'])[['km_per_driving_day']].median()
median_km_per_driving_day = df.groupby('label').median(numeric_only=True)[['km_per_driving_day']]
median_km_per_driving_day

# Add a column to df called `drives_per_driving_day`
df['drives_per_driving_day'] = df['drives'] / df['driving_days']
# Group by `label`, calculate the median, and isolate for drives per driving day
#df.groupby(['label'])[['drives_per_driving_day']].median()
median_drives_per_driving_day = df.groupby('label').median(numeric_only=True)[['drives_per_driving_day']]
median_drives_per_driving_day

# For each label, calculate the number of Android users and iPhone users
#df.groupby(['label'])['device'].value_counts()
df.groupby(['label', 'device']).size()

# For each label, calculate the percentage of Android users and iPhone users
#df.groupby(['label'])['device'].value_counts(normalize=True)*100
df.groupby('label')['device'].value_counts(normalize=True)