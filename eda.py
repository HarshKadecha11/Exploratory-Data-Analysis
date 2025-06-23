# Titanic Dataset - Data Cleaning and Exploratory Data Analysis

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Set up plotting parameters
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 8)

# Load the dataset
df = pd.read_csv('/Users/harsh_kadecha/Documents/Work/Internships /Prodigy/Task 2/train.csv')

print("=== INITIAL DATA EXPLORATION ===")
print(f"Dataset shape: {df.shape}")
print(f"\nColumn names: {list(df.columns)}")
print(f"\nData types:\n{df.dtypes}")
print(f"\nFirst 5 rows:")
print(df.head())

print("\n=== DATA QUALITY ASSESSMENT ===")
print("Missing values per column:")
missing_data = df.isnull().sum()
missing_percent = (missing_data / len(df)) * 100
missing_df = pd.DataFrame({
    'Missing Count': missing_data,
    'Missing Percentage': missing_percent
}).sort_values('Missing Count', ascending=False)
print(missing_df[missing_df['Missing Count'] > 0])

print(f"\nDuplicate records: {df.duplicated().sum()}")
print(f"\nBasic statistics:")
print(df.describe())

# Data Cleaning
print("\n=== DATA CLEANING ===")

# Handle missing values
# Age: Fill with median grouped by Pclass and Sex
df['Age'] = df.groupby(['Pclass', 'Sex'])['Age'].transform(
    lambda x: x.fillna(x.median())
)

# Embarked: Fill with mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Cabin: Create indicator for missing cabin
df['Cabin_Known'] = df['Cabin'].notna().astype(int)
df['Cabin'] = df['Cabin'].fillna('Unknown')

# Feature Engineering
# Extract titles from names
df['Title'] = df['Name'].str.extract('([A-Za-z]+)\.', expand=False)
title_mapping = {
    'Mr': 'Mr', 'Miss': 'Miss', 'Mrs': 'Mrs', 'Master': 'Master',
    'Dr': 'Rare', 'Rev': 'Rare', 'Col': 'Rare', 'Major': 'Rare',
    'Mlle': 'Miss', 'Countess': 'Rare', 'Ms': 'Miss', 'Lady': 'Rare',
    'Jonkheer': 'Rare', 'Don': 'Rare', 'Dona': 'Rare', 'Mme': 'Mrs',
    'Capt': 'Rare', 'Sir': 'Rare'
}
df['Title'] = df['Title'].map(title_mapping)

# Create family size feature
df['Family_Size'] = df['SibSp'] + df['Parch'] + 1
df['Is_Alone'] = (df['Family_Size'] == 1).astype(int)

# Create age groups
df['Age_Group'] = pd.cut(df['Age'],
                        bins=[0, 12, 18, 35, 60, 100],
                        labels=['Child', 'Teen', 'Adult', 'Middle_Age', 'Senior'])

# Create fare bins
df['Fare_Bin'] = pd.qcut(df['Fare'], 4, labels=['Low', 'Medium', 'High', 'Very_High'])

print("Data cleaning completed!")
print(f"Remaining missing values:\n{df.isnull().sum()[df.isnull().sum() > 0]}")

# EXPLORATORY DATA ANALYSIS

print("\n=== SURVIVAL ANALYSIS OVERVIEW ===")
survival_rate = df['Survived'].mean()
print(f"Overall survival rate: {survival_rate:.2%}")

# Create visualizations
fig, axes = plt.subplots(2, 3, figsize=(20, 12))

# 1. Survival distribution
survival_counts = df['Survived'].value_counts()
axes[0,0].pie(survival_counts.values, labels=['Died', 'Survived'], autopct='%1.1f%%')
axes[0,0].set_title('Survival Distribution')

# 2. Age distribution
axes[0,1].hist(df['Age'], bins=30, alpha=0.7, edgecolor='black')
axes[0,1].set_title('Age Distribution')
axes[0,1].set_xlabel('Age')

# 3. Fare distribution
axes[0,2].hist(df['Fare'], bins=30, alpha=0.7, edgecolor='black')
axes[0,2].set_title('Fare Distribution')
axes[0,2].set_xlabel('Fare')

# 4. Passenger class distribution
df['Pclass'].value_counts().sort_index().plot(kind='bar', ax=axes[1,0])
axes[1,0].set_title('Passenger Class Distribution')
axes[1,0].set_xlabel('Passenger Class')

# 5. Gender distribution
df['Sex'].value_counts().plot(kind='bar', ax=axes[1,1])
axes[1,1].set_title('Gender Distribution')
axes[1,1].set_xlabel('Gender')

# 6. Embarkation port distribution
df['Embarked'].value_counts().plot(kind='bar', ax=axes[1,2])
axes[1,2].set_title('Embarkation Port Distribution')
axes[1,2].set_xlabel('Port')

plt.tight_layout()
plt.show()

print("\n=== BIVARIATE ANALYSIS - SURVIVAL RATES ===")

# Survival by gender
print("Survival by Gender:")
gender_survival = pd.crosstab(df['Sex'], df['Survived'], normalize='index')
print(gender_survival)

# Survival by class
print("\nSurvival by Passenger Class:")
class_survival = pd.crosstab(df['Pclass'], df['Survived'], normalize='index')
print(class_survival)

# Survival by embarkation
print("\nSurvival by Embarkation Port:")
embarked_survival = pd.crosstab(df['Embarked'], df['Survived'], normalize='index')
print(embarked_survival)

# Create survival analysis plots
fig, axes = plt.subplots(2, 3, figsize=(20, 12))

# Survival by gender
sns.countplot(data=df, x='Sex', hue='Survived', ax=axes[0,0])
axes[0,0].set_title('Survival by Gender')

# Survival by class
sns.countplot(data=df, x='Pclass', hue='Survived', ax=axes[0,1])
axes[0,1].set_title('Survival by Passenger Class')

# Survival by embarkation
sns.countplot(data=df, x='Embarked', hue='Survived', ax=axes[0,2])
axes[0,2].set_title('Survival by Embarkation Port')

# Age distribution by survival
df[df['Survived']==0]['Age'].hist(alpha=0.5, bins=30, label='Died', ax=axes[1,0])
df[df['Survived']==1]['Age'].hist(alpha=0.5, bins=30, label='Survived', ax=axes[1,0])
axes[1,0].legend()
axes[1,0].set_title('Age Distribution by Survival')
axes[1,0].set_xlabel('Age')

# Fare distribution by survival
df[df['Survived']==0]['Fare'].hist(alpha=0.5, bins=30, label='Died', ax=axes[1,1])
df[df['Survived']==1]['Fare'].hist(alpha=0.5, bins=30, label='Survived', ax=axes[1,1])
axes[1,1].legend()
axes[1,1].set_title('Fare Distribution by Survival')
axes[1,1].set_xlabel('Fare')

# Family size vs survival
sns.countplot(data=df, x='Family_Size', hue='Survived', ax=axes[1,2])
axes[1,2].set_title('Survival by Family Size')

plt.tight_layout()
plt.show()

print("\n=== CORRELATION ANALYSIS ===")
# Select numerical columns for correlation
numerical_cols = ['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Family_Size']
correlation_matrix = df[numerical_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
            square=True, fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

print("Correlation with Survival:")
print(correlation_matrix['Survived'].sort_values(ascending=False))

print("\n=== ADVANCED ANALYSIS ===")

# Survival by title
print("Survival by Title:")
title_survival = pd.crosstab(df['Title'], df['Survived'], normalize='index')
print(title_survival)

# Survival by age group
print("\nSurvival by Age Group:")
age_group_survival = pd.crosstab(df['Age_Group'], df['Survived'], normalize='index')
print(age_group_survival)

# Combined analysis: Class and Gender
print("\nSurvival by Class and Gender:")
class_gender_survival = df.groupby(['Pclass', 'Sex'])['Survived'].agg(['count', 'mean'])
print(class_gender_survival)

# Statistical tests
print("\n=== STATISTICAL TESTS ===")

# T-test for age difference between survivors and non-survivors
survived_ages = df[df['Survived'] == 1]['Age']
died_ages = df[df['Survived'] == 0]['Age']
t_stat, p_value = stats.ttest_ind(survived_ages, died_ages)
print(f"T-test for age difference: t-statistic = {t_stat:.3f}, p-value = {p_value:.3f}")

# Chi-square test for gender and survival
chi2, p_chi2, dof, expected = stats.chi2_contingency(pd.crosstab(df['Sex'], df['Survived']))
print(f"Chi-square test for gender-survival association: χ² = {chi2:.3f}, p-value = {p_chi2:.3f}")

print("\n=== KEY FINDINGS ===")
print("1. Overall survival rate: {:.1%}".format(df['Survived'].mean()))
print("2. Female survival rate: {:.1%}".format(df[df['Sex']=='female']['Survived'].mean()))
print("3. Male survival rate: {:.1%}".format(df[df['Sex']=='male']['Survived'].mean()))
print("4. First class survival rate: {:.1%}".format(df[df['Pclass']==1]['Survived'].mean()))
print("5. Third class survival rate: {:.1%}".format(df[df['Pclass']==3]['Survived'].mean()))
print("6. Average age of survivors: {:.1f}".format(df[df['Survived']==1]['Age'].mean()))
print("7. Average age of non-survivors: {:.1f}".format(df[df['Survived']==0]['Age'].mean()))

print("\n=== FINAL DATASET SUMMARY ===")
print(f"Final dataset shape: {df.shape}")
print(f"Missing values remaining: {df.isnull().sum().sum()}")
print("Data cleaning and EDA completed successfully!")

