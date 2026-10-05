import pandas as pd
import matplotlib.pyplot as plt

# ===== LOAD DATA =====

df = pd.read_csv("data/insurance_claims.csv")


# ===== DATA PREPARATION =====

# Convert the date column from text to datetime
df["Effective To Date"] = pd.to_datetime(
    df["Effective To Date"],
    format="mixed"
)

# Create useful columns for analysis
df["Month"] = df["Effective To Date"].dt.month
df["Annual Premium"] = df["Monthly Premium Auto"] * 12


# ===== DATASET OVERVIEW =====

print("===== DATASET INFORMATION =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())


# ===== CLAIM ANALYSIS =====

print("\n===== CLAIM ANALYSIS =====")

average_claim = df["Total Claim Amount"].mean()
highest_claim = df["Total Claim Amount"].max()
total_claims = df["Total Claim Amount"].sum()

print(f"Average Claim Amount: ${average_claim:,.2f}")
print(f"Highest Claim Amount: ${highest_claim:,.2f}")
print(f"Total Claim Amount: ${total_claims:,.2f}")


# ===== VEHICLE CLASS ANALYSIS =====

claims_by_vehicle = (
    df.groupby("Vehicle Class")["Total Claim Amount"]
    .mean()
    .sort_values(ascending=False)
)

print("\n===== AVERAGE CLAIM BY VEHICLE CLASS =====")
print(claims_by_vehicle)


# ===== COVERAGE ANALYSIS =====

claims_by_coverage = (
    df.groupby("Coverage")["Total Claim Amount"]
    .mean()
    .sort_values(ascending=False)
)

print("\n===== AVERAGE CLAIM BY COVERAGE =====")
print(claims_by_coverage)


# ===== LOCATION ANALYSIS =====

claims_by_location = (
    df.groupby("Location Code")["Total Claim Amount"]
    .mean()
    .sort_values(ascending=False)
)

print("\n===== AVERAGE CLAIM BY LOCATION =====")
print(claims_by_location)


# ===== MONTHLY ANALYSIS =====

claims_by_month = (
    df.groupby("Month")["Total Claim Amount"]
    .mean()
)

print("\n===== AVERAGE CLAIM BY MONTH =====")
print(claims_by_month)


# ===== CORRELATION ANALYSIS =====

print("\n===== CORRELATION ANALYSIS =====")

correlations = df[
    [
        "Total Claim Amount",
        "Monthly Premium Auto",
        "Income",
        "Customer Lifetime Value",
        "Months Since Last Claim"
    ]
].corr()

print(
    correlations["Total Claim Amount"]
    .sort_values(ascending=False)
)

premium_correlation = df["Monthly Premium Auto"].corr(
    df["Total Claim Amount"]
)

income_correlation = df["Income"].corr(
    df["Total Claim Amount"]
)

print(f"\nPremium vs Claim Correlation: {premium_correlation:.3f}")
print(f"Income vs Claim Correlation: {income_correlation:.3f}")


# ===== VISUALIZATIONS =====

# Average claim by vehicle class
plt.figure(figsize=(10, 6))
claims_by_vehicle.plot(kind="bar")

plt.title("Average Claim Amount by Vehicle Class")
plt.xlabel("Vehicle Class")
plt.ylabel("Average Claim Amount ($)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("charts/claims_by_vehicle.png")
plt.close()


# Average claim by coverage
plt.figure(figsize=(8, 5))
claims_by_coverage.plot(kind="bar")

plt.title("Average Claim Amount by Coverage Level")
plt.xlabel("Coverage")
plt.ylabel("Average Claim Amount ($)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("charts/claims_by_coverage.png")
plt.close()


# Monthly premium vs claim amount
plt.figure(figsize=(8, 6))

plt.scatter(
    df["Monthly Premium Auto"],
    df["Total Claim Amount"],
    alpha=0.3
)

plt.title("Monthly Premium vs Total Claim Amount")
plt.xlabel("Monthly Premium ($)")
plt.ylabel("Total Claim Amount ($)")
plt.tight_layout()

plt.savefig("charts/premium_vs_claim.png")
plt.close()


# Average claim by location
plt.figure(figsize=(8, 5))
claims_by_location.plot(kind="bar")

plt.title("Average Claim Amount by Location")
plt.xlabel("Location")
plt.ylabel("Average Claim Amount ($)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("charts/claims_by_location.png")
plt.close()


# Average claim by month
plt.figure(figsize=(10, 5))
claims_by_month.plot(kind="line", marker="o")

plt.title("Average Claim Amount by Month")
plt.xlabel("Month")
plt.ylabel("Average Claim Amount ($)")
plt.xticks(range(1, 13))
plt.tight_layout()

plt.savefig("charts/claims_by_month.png")
plt.close()


print("\nCharts successfully saved to the charts folder.")