import pandas as pd

# Load the coffee shop Excel data
data = pd.read_excel("Coffee Shop Sales.xlsx")

# 1. Define shop name and store values in variables first
shop_name = "Astoria"

# Keep only Astoria sales using the shop_name variable
astoria = data[data["store_location"] == shop_name]

# Define drinks as Coffee and Tea
astoria_drinks = astoria[astoria["product_category"].isin(["Coffee", "Tea"])]
number_of_drinks_sold = astoria_drinks["transaction_qty"].sum()
price_per_drink = astoria_drinks["unit_price"].mean()

# Define pastries as Bakery items, Scones, Pastries, or Biscotti based on your data categories
astoria_pastries = astoria[astoria["product_category"].isin(["Bakery", "Scone", "Pastry", "Biscotti"])]
number_of_pastries_sold = astoria_pastries["transaction_qty"].sum()
price_per_pastry = astoria_pastries["unit_price"].mean()

# Print variables
print("Shop Name:", shop_name)
print("Number of drinks sold:", number_of_drinks_sold)
print("Average price per drink:", round(price_per_drink, 2))
print("Number of pastries sold:", number_of_pastries_sold)
print("Average price per pastry:", round(price_per_pastry, 2))

# 2. Calculate drink and pastry revenue
drink_revenue = number_of_drinks_sold * price_per_drink
pastry_revenue = number_of_pastries_sold * price_per_pastry
total_revenue = drink_revenue + pastry_revenue

print("Drink Revenue:", round(drink_revenue, 2))
print("Pastry Revenue:", round(pastry_revenue, 2))
print("Total Revenue:", round(total_revenue, 2))

# 3. Use an if/else statement to check if total revenue is at least $500
if total_revenue >= 500:
    print("Total revenue is at least $500.")
else:
    print("Total revenue is under $500.")

# 4. Print the written .txt file report
print("\n--- Written Report ---")
try:
    report_file = open("assignment1_report.txt", "r")
    print(report_file.read())
    report_file.close()
except FileNotFoundError:
    print("Note: assignment1_report.txt file not found yet.")