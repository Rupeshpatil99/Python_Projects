import numpy as np

# ============================================================
# NUMPY DAY 3 - ADVANCED PRACTICE
# ============================================================

print("=" * 60)
print("NUMPY DAY 3 - ADVANCED PRACTICE")
print("=" * 60)


# ------------------------------------------------------------
# 1. np.arange()
# ------------------------------------------------------------

numbers = np.arange(1, 11)

print("\n1. np.arange()")
print("Numbers:", numbers)


# ------------------------------------------------------------
# 2. Reshape
# ------------------------------------------------------------

numbers_2d = numbers.reshape(2, 5)

print("\n2. reshape()")
print(numbers_2d)
print("Shape:", numbers_2d.shape)


# ------------------------------------------------------------
# 3. Flatten
# ------------------------------------------------------------

flattened = numbers_2d.flatten()

print("\n3. flatten()")
print("Flattened:", flattened)


# ------------------------------------------------------------
# 4. Boolean Masking
# ------------------------------------------------------------

numbers = np.arange(1, 21)

even_numbers = numbers[numbers % 2 == 0]

print("\n4. Boolean Masking")
print("Original:", numbers)
print("Even numbers:", even_numbers)


# ------------------------------------------------------------
# 5. np.where()
# ------------------------------------------------------------

numbers = np.arange(1, 11)

result = np.where(numbers >= 5, "High", "Low")

print("\n5. np.where()")
print("Numbers:", numbers)
print("Category:", result)


# ------------------------------------------------------------
# 6. Axis Operations
# ------------------------------------------------------------

sales = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [200, 300, 400]
])

print("\n6. Axis Operations")
print("Sales Data:")
print(sales)

print("\nColumn-wise Sum (axis=0):")
print(sales.sum(axis=0))

print("\nRow-wise Sum (axis=1):")
print(sales.sum(axis=1))


# ------------------------------------------------------------
# 7. Sum, Mean, Median
# ------------------------------------------------------------

sales_values = np.array([100, 250, 300, 450, 500, 650, 700])

print("\n7. Statistical Operations")

print("Sales:", sales_values)
print("Sum:", np.sum(sales_values))
print("Mean:", np.mean(sales_values))
print("Median:", np.median(sales_values))


# ------------------------------------------------------------
# 8. Standard Deviation and Variance
# ------------------------------------------------------------

print("\n8. Standard Deviation and Variance")

print("Standard Deviation:", np.std(sales_values))
print("Variance:", np.var(sales_values))


# ------------------------------------------------------------
# 9. Maximum and Minimum
# ------------------------------------------------------------

print("\n9. Maximum and Minimum")

print("Maximum Sales:", np.max(sales_values))
print("Minimum Sales:", np.min(sales_values))


# ------------------------------------------------------------
# 10. Conditional Filtering
# ------------------------------------------------------------

sales_values = np.array([
    1200, 4500, 2300, 6700, 8900,
    1500, 3200, 7500, 9100, 2800
])

high_sales = sales_values[sales_values > 5000]

print("\n10. Conditional Filtering")
print("All Sales:", sales_values)
print("Sales above 5000:", high_sales)


# ------------------------------------------------------------
# 11. Multiple Conditions
# ------------------------------------------------------------

medium_sales = sales_values[
    (sales_values >= 3000) & (sales_values <= 7000)
]

print("\n11. Multiple Conditions")
print("Sales between 3000 and 7000:", medium_sales)


# ------------------------------------------------------------
# 12. np.where() for Sales Classification
# ------------------------------------------------------------

sales_category = np.where(
    sales_values >= 5000,
    "High Sales",
    "Low Sales"
)

print("\n12. Sales Classification")
print("Sales:", sales_values)
print("Category:", sales_category)


# ------------------------------------------------------------
# 13. 2D Sales Analysis
# ------------------------------------------------------------

monthly_sales = np.array([
    [1200, 1500, 1800, 2100],
    [2000, 2200, 2500, 2700],
    [3000, 3200, 3500, 3800]
])

print("\n13. 2D Sales Analysis")
print("Monthly Sales:")
print(monthly_sales)

print("\nTotal Sales:")
print(np.sum(monthly_sales))

print("\nAverage Sales:")
print(np.mean(monthly_sales))

print("\nMaximum Sales:")
print(np.max(monthly_sales))

print("\nMinimum Sales:")
print(np.min(monthly_sales))


# ------------------------------------------------------------
# 14. Row-wise Analysis
# ------------------------------------------------------------

row_total = monthly_sales.sum(axis=1)

print("\n14. Row-wise Total")
print("Row totals:", row_total)


# ------------------------------------------------------------
# 15. Column-wise Analysis
# ------------------------------------------------------------

column_total = monthly_sales.sum(axis=0)

print("\n15. Column-wise Total")
print("Column totals:", column_total)


# ------------------------------------------------------------
# 16. Highest and Lowest Sales
# ------------------------------------------------------------

highest_sales = np.max(monthly_sales)
lowest_sales = np.min(monthly_sales)

print("\n16. Highest and Lowest Sales")
print("Highest:", highest_sales)
print("Lowest:", lowest_sales)


# ------------------------------------------------------------
# 17. Flatten 2D Sales Data
# ------------------------------------------------------------

flat_sales = monthly_sales.flatten()

print("\n17. Flatten Sales Data")
print(flat_sales)


# ------------------------------------------------------------
# 18. Sales Above Average
# ------------------------------------------------------------

average_sales = np.mean(flat_sales)

above_average = flat_sales[flat_sales > average_sales]

print("\n18. Sales Above Average")
print("Average Sales:", average_sales)
print("Above Average:", above_average)


# ------------------------------------------------------------
# 19. Sales Performance Classification
# ------------------------------------------------------------

performance = np.where(
    flat_sales >= average_sales,
    "Above Average",
    "Below Average"
)

print("\n19. Sales Performance")
print(performance)


# ------------------------------------------------------------
# 20. Final Summary
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("FINAL SALES SUMMARY")
print("=" * 60)

print("Total Sales:", np.sum(flat_sales))
print("Average Sales:", np.mean(flat_sales))
print("Median Sales:", np.median(flat_sales))
print("Maximum Sales:", np.max(flat_sales))
print("Minimum Sales:", np.min(flat_sales))
print("Standard Deviation:", np.std(flat_sales))
print("Variance:", np.var(flat_sales))

print("\n" + "=" * 60)
print("NUMPY DAY 3 COMPLETED")
print("=" * 60)

# ------------------------------------------------------------
# 21. Real-World Sales Performance Analysis
# ------------------------------------------------------------

sales = np.array([
    1200, 4500, 2300, 6700, 8900,
    1500, 3200, 7500, 9100, 2800
])

average_sales = np.mean(sales)

above_average = sales[sales > average_sales]

print("\nReal-World Sales Analysis")
print("Average Sales:", average_sales)
print("Above Average Sales:", above_average)
print("Highest Sales:", np.max(sales))
print("Lowest Sales:", np.min(sales))