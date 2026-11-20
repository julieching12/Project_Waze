"""
The purpose of this project is to investigate and understand the data provided. This activity has three parts:
1: Understand the situation
2: Understand the data
3: Understand the variables

The goal is to use a dataframe contructed within Python, perform a cursory inspection of the provided dataset, and
inform team members of your findings.

NOTE: below codes are run in Jupyter Notebook environment.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset into a dataframe
df = pd.read_csv('waze_dataset.csv')

df.head()
df.size
df.describe()
df.info()

# Box plot
plt.figure(figsize=(6,2))
sns.boxplot(df['sessions'], fliersize=1) #can add showfliers=True
plt.title('Sessions box plot')

# Histogram
plt.figure(figsize=(6,2))
sns.histplot(x=df['sessions']) #without bins=range(), shows histogram automatically
plt.title('Sessions histogram')
median=df['sessions'].median()
plt.axvline(median, color='red', linestyle='--')
plt.text(75,1200,'median='+str(median), color='red')

# Box plot
plt.figure(figsize=(6,2))
sns.boxplot(df['drives'], fliersize=1)
plt.title('drives box plot')

# Histogram
plt.figure(figsize=(6,2))
sns.histplot(x=df['drives']) #without bins=range(), shows histogram automatically
plt.title('drives histogram')
median=df['drives'].median()
plt.axvline(median, color='red', linestyle='--')
plt.text(60,800,'median='+str(median), color='red')

# Box plot
# plt.figure(figsize=(6,2))
# sns.boxplot(df['total_sessions'], fliersize=1)
# plt.title('total_sessions box plot')
# Use helper function to plot boxplot based on the previous format
def boxplotter(column_str, **kwargs):
    plt.figure(figsize=(5,1))
    sns.boxplot(df[column_str], fliersize=1)
    plt.title(f'{column_str} box plot')
boxplotter('total_sessions')

# Histogram
# plt.figure(figsize=(6,2))
# sns.histplot(x=df['total_sessions']) #without bins=range(), shows histogram automatically
# plt.title('total_sessions histogram')
# median=df['total_sessions'].median()
# plt.axvline(median, color='red', linestyle='--')
# plt.text(200,700,'median='+str(median), color='red')
# Use helper function to plot histograms based on the previous format
def histogrammer(column_str, median_text=True, **kwargs):  #**kwargs = any keyword arguments for sns.histplot() function
    median=round(df[column_str].median(),1)
    plt.figure(figsize=(6,2))
    #sns.histplot(x=df[column_str], **kwargs)
    ax = sns.histplot(x=df[column_str], **kwargs)
    plt.axvline(median, color='red', linestyle='--')  #we want this line, so it's not a True or False option
    if median_text==True:
        #plt.text(200,700, f'median={median}', color='red')
        ax.text(0.25,0.85, f'median={median}', color='red',
                ha='left', va='top', transform=ax.transAxes)
    else:
        print('Median:', median)
    plt.title(f'{column_str} histogram')
histogrammer('total_sessions')
#histogrammer('total_sessions', binrange=(0,1000), binwidth=20, color='#4285F4', alpha=1)

# Box plot
boxplotter('n_days_after_onboarding')

# Histogram
histogrammer('n_days_after_onboarding', median_text=True)

# Box plot
boxplotter('driven_km_drives')

# Histogram
histogrammer('driven_km_drives', median_text=True)

# Box plot
boxplotter('duration_minutes_drives')

# Histogram
histogrammer('duration_minutes_drives', median_text=True)

# Box plot
boxplotter('activity_days')

# Histogram
histogrammer('activity_days', median_text=True, discrete=True)

# Box plot
boxplotter('driving_days')

# Histogram
histogrammer('driving_days', median_text=True, discrete=True)

# Pie chart
plt.figure(figsize=(3,3))
data=df['device'].value_counts()
plt.pie(data,
       labels=[f'{data.index[0]}:{data.values[0]}',f'{data.index[1]}:{data.values[1]}'],
       autopct='%1.1f%%')
plt.title('Users by device')

# Pie chart
plt.figure(figsize=(3,3))
data=df['label'].value_counts()
plt.pie(data,
       labels=[f'{data.index[0]}:{data.values[0]}',f'{data.index[1]}:{data.values[1]}'],
       autopct='%1.1f%%')
plt.title('Count of retained vs. churned')

# Histogram
#data=[df['driving_days'],df['activity_days']] #a python list that contains two seperate pandas series as its elements.
plt.figure(figsize=(12,4))
plt.hist([df['driving_days'],df['activity_days']], bins=range(0,33),  #set 33 instead of 32 can see number of days of the month are not sync
         #discrete=True, #AttributeError: 'Rectangle' object has no property 'discrete'
         label=['driving days', 'activity days'])
plt.legend()
plt.title('driving_days vs activity_days')

max_days = [df['driving_days'].max(), df['activity_days'].max()]
#max_days

# Scatter plot
sns.scatterplot(x=df['driving_days'], y=df['activity_days'])
plt.title('driving_days vs. activity_days')
plt.plot([0,31],[0,31],color='red',linestyle='--')

# Histogram
plt.figure(figsize=(5,4))
sns.histplot(x=df['device'], hue=df['label'], multiple='dodge', shrink=0.9)
plt.title('Retention by device histogram')

# 1. Create `km_per_driving_day` column
df['km_per_driving_day'] = df['driven_km_drives'] / df['driving_days']

# 2. Call `describe()` on the new column
df['km_per_driving_day'].describe()

# 1. Convert infinite values to zero
df.loc[df['km_per_driving_day']==np.inf, 'km_per_driving_day'] = 0

# 2. Confirm that it worked
df['km_per_driving_day'].describe()

# Histogram
plt.figure(figsize=(12,5))
data=df[df['km_per_driving_day'] <=1200]
sns.histplot(data, x='km_per_driving_day', bins=range(0,1201,20), hue='label', multiple='fill')
plt.title('km per driving day histogram')

# Histogram
plt.figure(figsize=(12,5))
sns.histplot(data=df, x='driving_days', bins=range(1,32), hue='label', multiple='fill')
plt.title('Churn rate per driving day')

df['percent_sessioins_in_last'] = df['sessions'] / df['total_sessions']

df['percent_sessioins_in_last'].median()

# Histogram
histogrammer('percent_sessioins_in_last',hue=df['label'],multiple='layer',median_text=True)

df['n_days_after_onboarding'].median()

# Histogram
plt.figure(figsize=(6,3))
sns.histplot(df.loc[df['percent_sessioins_in_last']>=0.4], x='n_days_after_onboarding')
plt.title('Num. days after onboarding for users with >=40% sessions in last month')

#Handling outliers
def outlier_imputer(column_name, percentile):
    # calculate threshold
    threshold = df[column_name].quantile(percentile)
    # impute threshold for values greater than threshold
    df.loc[df[column_name] > threshold, column_name] = threshold

    print('{:>25} | percentage: {} | threshold: {}'.format(column_name, percentile, threshold))

for column in ['sessions','drives','total_sessions','driven_km_drives','duration_minutes_drives']:
    outlier_imputer(column, 0.95)

df.describe()

df['last_month_drives_per_session_ratio'] = (df['drives']/df['sessions'])
df.head(20)