
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("data.csv")



print(df)

print(df.info())

# print(df.head(5))

total_sales_revenue = df[['Total Price']].sum()
print(f"the  total sales revenue of month is {total_sales_revenue}")


Avg= df.groupby('Product')['Unit Price'].mean().reset_index()
Avg.rename(columns={'Unit Price': 'Avarage Price'}, inplace=True)


Avg_sale = df.groupby('Product')['Unit Sold'].mean().reset_index()
Avg_sale.rename(columns={'Unit Sold': 'Avarage unit Sale'}, inplace=True)

#how to combine the Avg price and Avg sale in one table
print("average price of product and average sale of unit is:")

# print(Avg)





merged_df = pd.merge(Avg, Avg_sale, on='Product')
print(merged_df)

#not on ascending order

product_sales = df.groupby('Product')['Unit Sold'].sum().reset_index()
print("Top-selling products based on total units sold:")
print(product_sales)


df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
daily_sales = df.groupby('Date')['Total Price'].sum().reset_index()

print('the per day sales is:')
print(daily_sales)



df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')


data_grouped = df.groupby('Date')['Total Price'].sum().reset_index()

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(data_grouped['Date'], data_grouped['Total Price'], marker='o', linestyle='-', color='b')


plt.title('Total Price by Date')
plt.xlabel('Date')
plt.ylabel('Total Price')


plt.xticks(rotation=45)


plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
