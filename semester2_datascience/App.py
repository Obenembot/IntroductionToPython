import pandas as pd
import matplotlib.pyplot as plt



def import_file():
    df = pd.read_csv("adult.csv")
    print("Initial Shape:", df.shape)
    print(df.head())
    return df
df = import_file()


df.replace("?", pd.NA, inplace=True)

def apply_computing():
    print("Missing values per column:")
    print(df.isna().sum())

    for column in df.columns:
        if df[column].dtype == "object":  # categorical
            mode_val = df[column].mode()[0]
            df[column] = df[column].fillna(mode_val)
        else:# numerical
            median_val = df[column].median()
            df[column] = df[column].fillna(median_val)

apply_computing()


def remove_duplicates():
    df.drop_duplicates(inplace=True)
    print("\nCleaned Shape:", df.shape)
    print("Duplicates removed. Missing values handled.")
    print("\nMissing values after cleaning:")
    print(df.isna().sum())

remove_duplicates()

print("============ Part 2 Data Visualization========")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
plt.subplots_adjust(hspace=0.4, wspace=0.3)

def top_left_stacked_bar_chart():
    gender_income = df.groupby(["sex", "income"]).size().unstack()

    gender_income.plot(
        kind="bar",
        stacked=True,
        ax=axes[0, 0],
        color=["#6baed6", "#fd8d3c"]
    )
    axes[0, 0].set_title("Income Distribution by Gender")
    axes[0, 0].set_xlabel("Gender")
    axes[0, 0].set_ylabel("Count")
    axes[0, 0].legend(title="Income")

def top_right_stacked_bar_chart():
    age_hours = df.groupby(["age", "income"])["hours.per.week"].mean().unstack()

    age_hours.plot(
        ax=axes[0, 1],
        linewidth=2
    )
    axes[0, 1].set_title("Age vs Average Weekly Work Hours")
    axes[0, 1].set_xlabel("Age (years)")
    axes[0, 1].set_ylabel("Avg Hours per Week")
    axes[0, 1].legend(title="Income Bracket")


def bottom_left_bar_chart():
    df[df["income"] == "<=50K"]["hours.per.week"].plot(
        kind="hist",
        ax=axes[1, 0],
        bins=20,
        alpha=0.6,
        color="blue",
        label="<=50K"
    )
    df[df["income"] == ">50K"]["hours.per.week"].plot(
        kind="hist",
        ax=axes[1, 0],
        bins=20,
        alpha=0.6,
        color="orange",
        label=">50K"
    )

    axes[1, 0].set_title("Work Hours Distribution by Income Group")
    axes[1, 0].set_xlabel("Hours per Week")
    axes[1, 0].set_ylabel("Frequency")
    axes[1, 0].legend()

def bottom_right_bar_chart():
    edu_occ = df.groupby(["occupation", "income"])["education.num"].mean().unstack()

    edu_occ.plot(
        kind="bar",
        ax=axes[1, 1],
        width=0.8,
        color=["#3182bd", "#e6550d"]
    )
    axes[1, 1].set_title("Average Education Level by Occupation & Income")
    axes[1, 1].set_xlabel("Occupation")
    axes[1, 1].set_ylabel("Average Education.num")
    axes[1, 1].legend(title="Income Bracket")
    axes[1, 1].tick_params(axis='x', rotation=45)


# Top-Left: Stacked Bar Chart
top_left_stacked_bar_chart()
top_right_stacked_bar_chart()
bottom_left_bar_chart()
bottom_right_bar_chart()
plt.tight_layout()
plt.show()