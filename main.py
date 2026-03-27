import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("sales.csv")

# Convert Date column
data['Date'] = pd.to_datetime(data['Date'])

# Total sales
total_sales = data['Amount'].sum()
print("Total Sales:", total_sales)

# Top product
top_product = data.groupby('Product')['Amount'].sum().idxmax()
print("Top Product:", top_product)

# Monthly sales
data['Month'] = data['Date'].dt.month
monthly_sales = data.groupby('Month')['Amount'].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# Plot graph
monthly_sales.plot(kind='bar')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()