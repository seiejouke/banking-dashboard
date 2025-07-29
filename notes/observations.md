Info from kaggle; 

Description of the Dataset: A Comprehensive Record of Personal Savings Account Transactions

This dataset provides a detailed record of an individual's savings bank account transactions spanning the years 2022 and 2023.
It encompasses a total of 10 columns, consisting of 6 primary columns and 4 secondary columns.

The 6 Primary Columns Are:

Date:                   This column records the date of each transaction.
Debit or Credit:        It signifies whether each transaction involves a debit (money withdrawn) or a credit (money deposited).
Amount:                 This column documents the monetary value associated with each transaction.
Balance:                It records the account balance after each transaction.
Method of Transaction:  This column specifies the method or channel through which the transaction was executed.
Name of Person:         It identifies the person involved in the transaction.

In addition to these primary columns, there is an essential secondary column:
i.e., Tday (Transaction Day): This column is designed to highlight specific days with multiple transactions.
It indicates the occurrence of multiple transactions on the same date, providing valuable information about account activity.

This dataset comprises a total of 509 transactions, and within these transactions, there are 313 unique transaction dates.
This unique date count underscores that the dataset includes days with multiple transactions, and the 'Tday' column is utilized to distinguish and track such instances.

Refer the data for more insights.
You will also be able to see Pareto distribution (Find it out!!)
-----------------------------------------------------------------------------------------------------
notebook workflow, see notebook_workflow.py for actual code;
-----------------------------------------------------------------------------------------------------

CSV Data Cleaning Workflow Overview
Load & Preview Data
df = pd.read_csv("path/to/file.csv")
df.info()
df.describe()
df.head()

Clean & Standardize
df['name'] = df['name'].fillna('Unknown')
df['DrCr'] = df['DrCr'].str.strip().str.upper().map({'DB': 'debit', 'CR': 'credit'})

Rename Columns for Clarity
df = df.rename(columns={
'DrCr': 'transaction_type',
'mode': 'transaction_method',
'Tday': 'transaction_order_on_date'
})

Create Transaction Order
df['transaction_order_on_date'] = df.groupby('date').cumcount() + 1

Reduce Redundancy
df = df.drop(columns=['Day', 'Month', 'Year'])

Quality Checks
df = df.drop_duplicates()
print(df.isnull().sum())
print(df.dtypes)

Export Cleaned Data
df.to_csv("data/clean/bankstatements_cleaned.csv", index=False, encoding='utf-8')

