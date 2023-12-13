import csv
from decimal import Decimal

# Specify the file path and the column index (0-based) you want to analyze
file_path = "banknifty_1min.csv"  # Replace with your file path
column_index =2  # Replace with the desired column index

# Read data from the CSV file
with open(file_path, 'r') as file:
    csv_reader = csv.reader(file , delimiter=',')
    next(csv_reader)  # Skip header if present

    # Extract the specified column values
    column_values = [int(row[column_index]) for row in csv_reader]

# Find the highest and lowest values
highest_value = max(column_values)
lowest_value = min(column_values)

# Print the results
print(f"Highest value in column {column_index}: {highest_value}")
print(f"Lowest value in column {column_index}: {lowest_value}")
