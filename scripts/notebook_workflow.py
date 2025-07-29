# %%
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns

# %%
df = pd.read_csv("../data/raw/bankstatements.csv")

# %%
#df.head()
df.info()
df[['amount', 'balance']].describe()

# %%
df['name'] = df['name'].fillna('Unknown') #Change NaN to unknown

# %%
df.info() # confirm changes

# %%
df['DrCr'] = df['DrCr'].str.strip().str.upper().map({'DB': 'debit', 'CR': 'credit'})

# Improve table readability

# %%
df.head()

# %%
df = df.rename(columns={'DrCr': 'transaction_type'})
#Improve column readability


# %%
df.head()

# %%
df = df.rename(columns={'Tday': 'transaction_order_on_date'}) # Improve column clarity

# %%
df.head()

# %%
df['transaction_order_on_date'] = df.groupby('date').cumcount() +1

# %%
df.head()

# %%
df = df.rename(columns={'mode': 'transaction_method'}) # Improving clarity

# %%
df.head() 

# %%
print(df.columns)

# %%
df = df.drop(columns=['Day', 'Month', 'Year']) # Improve clarity by reducing redundancy

# %%
df.head()

# %%
print(df.duplicated().sum()) # Check

# %%
print(df.isnull().sum()) # Check


# %%
print(df.dtypes) # Check, good to go

# %%
df.to_csv('../data/clean/bankstatements_cleaned.csv', index=False, encoding='utf-8' ) # encoding check


