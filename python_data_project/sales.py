# Step 1: Import the libraries we need
import pandas as pd           # For handling data tables
import matplotlib.pyplot as plt  # For making charts

# Step 2: Create our sales data
# We have Products, their Prices, and how many were sold (Quantity)
data = {
    'Product': ['Phone', 'Laptop', 'Phone', 'Tablet', 'Laptop'],
    'Price': [500, 1200, 500, 300, 1200],
    'Quantity': [2, 1, 3, 4, 2]
}

# Step 3: Put the data into a table (DataFrame)
df = pd.DataFrame(data)

# Step 4: Calculate Total Sales for each row
# Total Sales = Price * Quantity
df['Total Sales'] = df['Price'] * df['Quantity']

# Step 5: Print the full table
print("=== Full Sales Table ===")
print(df)
print("\n")  # Blank line for readability

# Step 6: Calculate total sales for all products
total_sales = df['Total Sales'].sum()
print(f"Total Sales of all products: ${total_sales}")
print("\n")

# Step 7: Calculate total quantity sold for each product
quantity_per_product = df.groupby('Product')['Quantity'].sum()
print("=== Total Quantity Sold Per Product ===")
print(quantity_per_product)
print("\n")

# Step 8: Make a bar chart to visualize total quantities
# Each bar represents a product, height = total quantity sold
quantity_per_product.plot(kind='bar', color='lightgreen')
plt.title('Product Sales')
plt.xlabel('Product')
plt.ylabel('Quantity Sold')
plt.show()
