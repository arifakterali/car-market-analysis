import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 

CHARTS_DIR = 'charts/'

df = pd.read_csv('cleaned_car_data.csv')


df['Selling_Price'].hist(bins=15)
plt.title('Distribution of Selling Price')
plt.xlabel('Selling Price in Lakhs')
plt.ylabel('No. of cars')
plt.savefig(CHARTS_DIR + '01_selling_price_hist.png')
plt.close()

df['Present_Price'].hist(bins=15)
plt.title('Distribution of Present Price')
plt.xlabel('Present Price in Lakhs')
plt.ylabel('No. of cars')
plt.savefig(CHARTS_DIR + '02_present_price_hist.png')
plt.close()

df['Kms_Driven'].hist(bins=15)
plt.title('Distribution of Kms Driven')
plt.xlabel('Kms Driven')
plt.ylabel('No. of cars')
plt.savefig(CHARTS_DIR + '03_kms_driven_hist.png')
plt.close()

df['Age'].hist(bins=15)
plt.title('Distribution of Car Age')
plt.xlabel('Age in Years')
plt.ylabel('No. of cars')
plt.savefig(CHARTS_DIR + '04_car_age_hist.png')
plt.close()

df['Fuel_Type'].value_counts().plot(kind='bar')
plt.title('Fuel Type Distribution')
plt.ylabel('No. of Cars')
plt.xticks(rotation=0)
plt.savefig(CHARTS_DIR + '05_fuel_type_bargraph.png')
plt.close()

df['Seller_Type'].value_counts().plot(kind='bar')
plt.title('Seller Type Distribution')
plt.ylabel('No. of Cars')
plt.xticks(rotation=0)
plt.savefig(CHARTS_DIR + '06_seller_type_bargraph.png')
plt.close()

df['Transmission'].value_counts().plot(kind='bar')
plt.title('Transmission Distribution')
plt.ylabel('No. of Cars')
plt.xticks(rotation=0)
plt.savefig(CHARTS_DIR + '07_transmission_bargraph.png')
plt.close()

plt.scatter(df['Present_Price'], df['Selling_Price'], alpha=0.6)
plt.title('Selling Price vs Present Price ')
plt.xlabel('Present Price in Lakhs')
plt.ylabel('Selling Price in Lakhs')
plt.savefig(CHARTS_DIR + '08_price_vs_presentprice_scatter.png')
plt.close()

plt.scatter(df['Age'], df['Selling_Price'], alpha=0.6)
plt.title('Selling Price vs Age')
plt.xlabel('Age in Years')
plt.ylabel('Selling Price in Lakhs')
plt.savefig(CHARTS_DIR + '09_price_vs_age_scatter.png')
plt.close()

plt.scatter(df['Kms_Driven'], df['Selling_Price'], alpha=0.6)
plt.title('Selling Price vs Kms Driven')
plt.xlabel('Kmd Driven')
plt.ylabel('Selling Price in Lakhs')
plt.savefig(CHARTS_DIR + '10_price_vs_kms_driven_scatter.png')
plt.close()

sns.boxplot(x='Fuel_Type', y='Selling_Price', data=df)
plt.title('Selling Price by Fuel Type')
plt.savefig(CHARTS_DIR + '11_price_by_fuel_type_boxplot.png')
plt.close()

sns.boxplot(x='Seller_Type', y='Selling_Price', data=df)
plt.title('Selling Price by Seller Type')
plt.savefig(CHARTS_DIR + '12_price_by_seller_type_boxplot.png')
plt.close()

sns.boxplot(x='Transmission', y='Selling_Price', data=df)
plt.title('Selling Price by Transmission')
plt.savefig(CHARTS_DIR + '13_price_by_transmission_boxplot.png')
plt.close()
