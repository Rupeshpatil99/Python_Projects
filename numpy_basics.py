import numpy as np


# ==========================================
# Day 2 - NumPy Fundamentals
# ==========================================

# 1. Create a NumPy array
numbers = np.array([10, 20, 30, 40, 50])

print("Array:", numbers)
print("Data Type:", numbers.dtype)
print("Shape:", numbers.shape)


# 2. Indexing
print("\n--- Indexing ---")
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Third element:", numbers[2])


# 3. Slicing
print("\n--- Slicing ---")
print("First three elements:", numbers[:3])
print("Last three elements:", numbers[-3:])


# 4. Mathematical operations
print("\n--- Mathematical Operations ---")
print("Add 10:", numbers + 10)
print("Multiply by 2:", numbers * 2)
print("Square:", numbers ** 2)


# 5. Statistical operations
print("\n--- Statistics ---")
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Median:", np.median(numbers))
print("Minimum:", np.min(numbers))
print("Maximum:", np.max(numbers))
print("Standard Deviation:", np.std(numbers))


# 6. Sales analysis example
sales = np.array([1200, 1500, 1100, 1800, 2000, 1750, 1600])

print("\n--- Sales Analysis ---")
print("Daily Sales:", sales)
print("Total Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Highest Sales:", np.max(sales))
print("Lowest Sales:", np.min(sales))
print("Sales Standard Deviation:", np.std(sales))


# 7. Filtering
high_sales = sales[sales > 1500]

print("\n--- Sales Above 1500 ---")
print(high_sales)
