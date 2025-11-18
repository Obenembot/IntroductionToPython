import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.array([-2, 1, 2, 3, 4, 5])
y = np.array([-2, 2, 1, 3, 2, 4])

# Create the plot
plt.plot(x,y)


# Add labels and a title
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Simple Line Plot")

# plt.legend()
# Display the plot
plt.show()