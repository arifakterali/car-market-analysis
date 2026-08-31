import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

CURRENT_YEAR = 2019

df = pd.read_csv("./1776311302-P3-Car Market Trends Analysis with Car Dekho Data.csv")

# print(df[df.duplicated(keep=False)])
# print("Before:", df.shape)
df = df.drop_duplicates()
# print("After:", df.shape )

# print(df['Year'].min(), df['Year'].max())
# print(df['Kms_Driven'].min(), df['Kms_Driven'].max())
# print(df['Owner'].value_counts())
# print(df['Fuel_Type'].value_counts())
# print(df['Seller_Type'].value_counts())
# print(df['Transmission'].value_counts())

# sns.boxplot(y='Selling_Price', data=df)
# plt.savefig('boxplot_selling_price.png')
# plt.close()
#
# sns.boxplot(y='Present_Price', data=df)
# plt.savefig('boxplot_present_price.png')
# plt.close()
#
# sns.boxplot(y='Kms_Driven', data=df)
# plt.savefig('boxplot_kms_driven.png')
# plt.close()

price_outliers = df[df['Selling_Price'] > 13]
# print(price_outliers[['Car_Name', 'Year', 'Selling_Price', 'Present_Price', 'Kms_Driven']])

kms_outlier = df[df['Kms_Driven'] > 100000]
# print(kms_outlier[['Car_Name', 'Year', 'Selling_Price', 'Present_Price', 'Kms_Driven']])

df['Age'] = CURRENT_YEAR - df['Year']
df['Kms_per_year'] = df['Kms_Driven'] / df['Age']
# print(df[['Car_Name', 'Year', 'Kms_Driven', 'Age', 'Kms_per_year']].sort_values('Kms_per_year', ascending=False).head(10))


df = df[df['Kms_Driven'] < 300000]
# print(df.shape)

# print(df['Car_Name'].nunique())
# print(df['Car_Name'].unique())

# print(df['Car_Name'].str[0].str.isupper().value_counts())

car_group = df[df['Car_Name'].str[0].str.isupper() == False]['Car_Name'].unique()
bike_group = df[df['Car_Name'].str[0].str.isupper() == True]['Car_Name'].unique()
# print(car_group)
# print(bike_group)

df = df[df['Car_Name'].str[0].str.isupper() == False]
# print(df.shape)

df.to_csv('cleaned_car_data.csv', index=False)
