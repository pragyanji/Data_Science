import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv('Titanic.csv')
# print(data.head(20))
# print(data.shape)
# print(data.info())
# print(data['Age'].describe())

# Fill missing values in the 'Age' column with the mean age

# print(f'Null values in Age column: {data['Age'].isnull().sum()}')

# print(f'Mean age: {mean_age}')
#way 1
data['Age'] = data['Age'].fillna(data['Age'].mean())
# print(f'Null values in Age column after filling: {data["Age"].isnull().sum()}')

#way 2
# data.fillna({'Age': data['Age'].mean()}, inplace=True)
# print(f'Null values in Age column after filling: {data["Age"].isnull().sum()}')

data.drop(columns=['Cabin','Ticket'], inplace=True)
# print(data)

# Convert 'Sex' column to numerical values (0 for male, 1 for female)
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data.rename(columns={'Sex': 'Gender'}, inplace=True)
# print(data)

# Exploratory Data Analysis
female_business_class = data[(data['Gender'] == 1) & (data['Pclass'] == 1)]
# print(f'Number of female passengers in business class: {len(female_business_class)}')

survived_passengers_in_business_class = data[(data['Survived'] == 1) & (data['Pclass'] == 1)]
# print(f'Number of survived passengers in business class: {len(survived_passengers_in_business_class)}')

# Group by 'Pclass' and calculate the mean survival rate for each class
survival_rate_by_class = data.groupby('Pclass')['Survived'].mean()
# print('Survival rate by class:')
# print(survival_rate_by_class)

# Filtering using loc
filtered_data = data.loc[data['Age'] > 30, ['Name', 'Age', 'Fare']]
# print('Passengers older than 30:')
# print(filtered_data)

# Create a new column 'Family_Size' by summing 'SibSp' and 'Parch'
data['Family_Size'] = data['SibSp'] + data['Parch'] + 1
# print(data[['Name', 'SibSp', 'Parch', 'Family_Size']])

# print(data[data['Family_Size'] > 5][['Name', 'Family_Size']])

# print(data.groupby(data['Family_Size'] > 2)['Survived'].mean())

data['Title'] = data['Name'].str.split(',').str[1].str.split('.').str[0].str.strip()

print(data[['Title','Name']].head(50))