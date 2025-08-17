import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from sklearn.linear_model import LinearRegression

# Given data
experience = np.array([1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 15, 16, 18, 20])
education = np.array([0, 0, 1, 1, 0, 2, 1, 2, 1, 2, 0, 1, 2, 0, 1])  # 0=Bachelor,1=Master,2=PhD
location = np.array([0, 1, 1, 2, 0, 2, 2, 1, 1, 0, 2, 2, 1, 0, 1])  # 0=Remote,1=On-site,2=Hybrid
salary = np.array([48, 53, 60, 65, 68, 80, 78, 88, 90, 100, 92, 105, 108, 115, 120])

colors = ['blue', 'orange', 'green']  # Remote, On-site, Hybrid
markers = ['o', 's', '^']  # Bachelor, Master, PhD

def scatter_plot():
    plt.figure(figsize=(10, 6))
    for i in range(len(experience)):
        plt.scatter(
            experience[i], salary[i],
            color=colors[location[i]],
            marker=markers[education[i]],
            s=100,
            edgecolor='k'
        )

    plt.xlabel("Years of Experience")
    plt.ylabel("Salary (in $1000s)")
    plt.title("Experience vs Salary (Education & Location)")


scatter_plot()
#  Best Fit Lines per Location
loc_labels = ["Remote", "On-site", "Hybrid"]

for loc in np.unique(location):
    x_loc = experience[location == loc].reshape(-1, 1)
    y_loc = salary[location == loc]

    model = LinearRegression().fit(x_loc, y_loc)
    x_range = np.linspace(min(experience), max(experience), 100).reshape(-1, 1)
    y_pred = model.predict(x_range)

    plt.plot(x_range, y_pred, color=colors[loc], label=f"{loc_labels[loc]} Best Fit")

# Multiple Linear Regression Model
# Features: Experience, Experience^2, Education, Location
X = np.column_stack((experience, experience ** 2, education, location))
y = salary

reg = LinearRegression().fit(X, y)

print("Intercept:", reg.intercept_)
print("Coefficients:", reg.coef_)

# Predictions
pred1 = reg.predict([[9, 9 ** 2, 1, 0]])  # 9 yrs, Master's, Remote
pred2 = reg.predict([[14, 14 ** 2, 2, 2]])  # 14 yrs, PhD, Hybrid

print("Predicted Salary (9yrs, Master, Remote):", pred1[0])
print("Predicted Salary (14yrs, PhD, Hybrid):", pred2[0])

# Predicted points
plt.scatter(9, pred1[0], color='red', marker='*', s=200, label="Predicted (9yrs, Master, Remote)")
plt.scatter(14, pred2[0], color='purple', marker='*', s=200, label="Predicted (14yrs, PhD, Hybrid)")

plt.legend()
plt.show()
