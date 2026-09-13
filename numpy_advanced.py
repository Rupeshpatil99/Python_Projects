import numpy as np

# ==========================================
# Day 3 - NumPy Advanced Practice
# ==========================================

print("=" * 50)
print("DAY 3 - NUMPY ADVANCED")
print("=" * 50)


# ------------------------------------------------
# 1. Reshape Array
# ------------------------------------------------

arr = np.arange(1, 21)

print("\n1. Original Array:")
print(arr)

matrix = arr.reshape(4, 5)

print("\nReshaped Array (4 x 5):")
print(matrix)

print("\nShape:")
print(matrix.shape)


# ------------------------------------------------
# 2. Flatten Array
# ------------------------------------------------

flat_array = matrix.flatten()

print("\n2. Flattened Array:")
print(flat_array)


# ------------------------------------------------
# 3. Sales Filtering
# ------------------------------------------------

sales = np.array([1200, 1500, 1100, 1800, 2000, 1750, 1600])

print("\n3. Sales Data:")
print(sales)

# Sales greater than 1500
high_sales = sales[sales > 1500]

print("\nSales greater than 1500:")
print(high_sales)

# Sales less than 1500
low_sales = sales[sales < 1500]

print("\nSales less than 1500:")
print(low_sales)

# Sales between 1200 and 1800
medium_sales = sales[(sales >= 1200) & (sales <= 1800)]

print("\nSales between 1200 and 1800:")
print(medium_sales)


# ------------------------------------------------
# 4. np.where()
# ------------------------------------------------

positions = np.where(sales > 1700)

print("\n4. Positions where sales are greater than 1700:")
print(positions)

sales_category = np.where(sales > 1500, "High", "Low")

print("\nSales Category:")
print(sales_category)


# ------------------------------------------------
# 5. Sales Matrix
# ------------------------------------------------

sales_matrix = np.array([
    [1200, 1500, 1800],
    [1100, 2000, 1750],
    [1600, 1400, 1900]
])

print("\n5. Sales Matrix:")
print(sales_matrix)


# Total sales
total_sales = np.sum(sales_matrix)

print("\nTotal Sales:")
print(total_sales)


# Column-wise sales
column_sales = np.sum(sales_matrix, axis=0)

print("\nSales for Each Column:")
print(column_sales)


# Row-wise sales
row_sales = np.sum(sales_matrix, axis=1)

print("\nSales for Each Row:")
print(row_sales)


# Maximum sales
maximum_sales = np.max(sales_matrix)

print("\nMaximum Sales:")
print(maximum_sales)


# Minimum sales
minimum_sales = np.min(sales_matrix)

print("\nMinimum Sales:")
print(minimum_sales)


# ------------------------------------------------
# 6. Sales Greater Than 1700
# ------------------------------------------------

high_matrix_sales = sales_matrix[sales_matrix > 1700]

print("\n6. Sales Greater Than 1700:")
print(high_matrix_sales)


# ------------------------------------------------
# 7. Statistics
# ------------------------------------------------

print("\n7. Statistical Analysis:")

print("Mean Sales:", np.mean(sales_matrix))
print("Median Sales:", np.median(sales_matrix))
print("Standard Deviation:", np.std(sales_matrix))
print("Variance:", np.var(sales_matrix))


print("\n" + "=" * 50)
print("DAY 3 COMPLETED")
print("=" * 50)
