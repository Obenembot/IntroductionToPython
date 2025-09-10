import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5,6]
y = [2, 4, 6, 8, 10,20]
# ---------------------------
# 1. LINE PLOT
# ---------------------------
plt.figure(figsize=(6, 4))
plt.plot(x, y, marker='o', color='blue', linestyle='-', label="Line")
plt.title("Line Plot Example")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()
plt.grid()
plt.show()


# ---------------------------
# 2. BAR CHART
# ---------------------------
categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 5, 12, 9]
plt.figure(figsize=(6, 4))
plt.bar(categories, values, color='green')
plt.title("Bar Chart Example")
plt.xlabel("X-Categories")
plt.ylabel("Y-Values")
# plt.grid()
plt.show()



# # ---------------------------
# # 3. HISTOGRAM
# # ---------------------------

data = [5, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 10]
plt.figure(figsize=(6, 4))
plt.hist(data, bins=5, color='purple', edgecolor='black')
plt.title("Histogram Example")
plt.xlabel("Data Range")
plt.ylabel("Frequency")
plt.show()
#
# # ---------------------------
# # 4. SCATTER PLOT
# ---------------------------
plt.figure(figsize=(6, 4))
plt.scatter(x, y, color='red', marker='o')
plt.title("Scatter Plot Example")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
