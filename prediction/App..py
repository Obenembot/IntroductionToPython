# ==============================
# Transaction Prediction Script (Final Fixed Version)
# ==============================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# Step 1: Load the dataset
# ----------------------------
file_path = "predictCustomer.xlsx"  # <-- Replace with your file path
df = pd.read_excel(file_path)

# ----------------------------
# Step 2: Preprocess the data
# ----------------------------
# Convert to datetime
df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])

# Sort transactions by HpId and TransactionDate
df_sorted = df.sort_values(by=["HpId", "TransactionDate"]).copy()

# Calculate difference in days between transactions
df_sorted["DaysSinceLast"] = df_sorted.groupby("HpId")["TransactionDate"].diff().dt.days

# ----------------------------
# Step 3: Aggregate everything in one step
# ----------------------------
# Count total transactions, find last transaction date, and average gap
prediction_df = (
    df_sorted.groupby("HpId")
    .agg(
        TotalTransactions=("TransactionDate", "count"),
        LastTransactionDate=("TransactionDate", "max"),
        AvgTransactionGap=("DaysSinceLast", "mean")
    )
    .reset_index()
)

# Predict next transaction date
prediction_df["PredictedNextTransaction"] = (
        prediction_df["LastTransactionDate"]
        + pd.to_timedelta(prediction_df["AvgTransactionGap"], unit="d")
)

# Sort by predicted date
prediction_df = prediction_df.sort_values(by="PredictedNextTransaction")

# ----------------------------
# Step 4: Visualization
# ----------------------------
plt.figure(figsize=(10, 6))
sns.histplot(prediction_df["AvgTransactionGap"].dropna(), bins=10, kde=True)
plt.title("Distribution of Average Transaction Gaps per Customer")
plt.xlabel("Average Transaction Gap (Days)")
plt.ylabel("Number of Customers")
plt.grid(axis="y")
plt.tight_layout()
plt.show()

# ----------------------------
# Step 5: Show final predictions
# ----------------------------
print("\n========= CUSTOMER TRANSACTION PREDICTIONS =========\n")
print(prediction_df)

# ----------------------------
# Step 6: Export results to Excel
# ----------------------------
prediction_df.to_excel("predicted_transactions.xlsx", index=False)
print("\n✅ Predictions saved to: predicted_transactions.xlsx")
