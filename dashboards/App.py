import streamlit as st
import pandas as pd

# Sample data
students = [
    {"name": "Alice", "age": 20, "modules": [{"name": "Math", "marks": 85, "grade": "A"}]},
    {"name": "Bob", "age": 21, "modules": [{"name": "Science", "marks": 78, "grade": "B"}]}
]

# Convert to DataFrame for easy display
data = []
for student in students:
    for m in student["modules"]:
        data.append({"Student": student["name"], "Age": student["age"], "Module": m["name"], "Marks": m["marks"], "Grade": m["grade"]})
df = pd.DataFrame(data)

# Sidebar for menu
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Student Performance", "Grades Summary"])

# Dashboards
if page == "Overview":
    st.title("Overview Dashboard")
    st.dataframe(df)
elif page == "Student Performance":
    st.title("📈 Student Performance Dashboard")
    st.bar_chart(df.set_index("Student")["Marks"])
elif page == "Grades Summary":
    st.title("🏅 Grades Summary")
    st.write(df.groupby("Grade").size())
