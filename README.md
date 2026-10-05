# Insurance Claims Data Analysis

A Python data analysis project exploring insurance customer and claims data to identify patterns in claim amounts, vehicle classes, coverage levels, premiums, locations, and time.

## Project Overview

This project analyzes a dataset containing 9,134 insurance customer records. The goal is to use Python data analysis and visualization techniques to identify factors associated with insurance claim amounts.

## Questions Explored

- Which vehicle classes have the highest average claim amounts?
- How do claim amounts differ between coverage levels?
- What is the relationship between monthly premiums and claim amounts?
- How do average claim amounts vary by location?
- How do average claim amounts change throughout the year?

## Tools & Technologies

- Python
- Pandas
- Matplotlib

## Data Preparation

The analysis includes:

- Checking for missing values
- Checking for duplicate records
- Converting date data into a usable datetime format
- Extracting month information for time-based analysis
- Creating an annual premium feature from monthly premiums

## Analysis

The project uses:

- Descriptive statistics
- Filtering and grouping
- Aggregation
- Correlation analysis
- Time-based analysis
- Data visualization

## Key Findings

- Monthly insurance premiums have a positive relationship with total claim amounts.
- Luxury vehicle classes have substantially higher average claim amounts than standard vehicle classes.
- Average claim amounts differ across insurance coverage levels.
- Claim amounts also vary by customer location.
- Monthly claim averages show some variation throughout the year.

Correlation describes an association between variables and does not establish causation.

## Visualizations

The project generates five charts:

- Average Claim Amount by Vehicle Class
- Average Claim Amount by Coverage Level
- Monthly Premium vs Total Claim Amount
- Average Claim Amount by Location
- Average Claim Amount by Month

Charts are saved automatically in the `charts/` directory.

## Project Structure

```text
InsuranceClaimsAnalysis/
├── charts/
│   ├── claims_by_vehicle.png
│   ├── claims_by_coverage.png
│   ├── premium_vs_claim.png
│   ├── claims_by_location.png
│   └── claims_by_month.png
├── data/
│   └── insurance_claims.csv
├── insurance_analysis.py
├── requirements.txt
└── README.md
```

## Running the Project

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the analysis:

```bash
python insurance_analysis.py
```