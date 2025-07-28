# Banking Dashboard (Power BI)

Interactive banking dashboard built in Power BI using the [Bank Statements Dataset](https://www.kaggle.com/datasets/abutalhadmaniyar/bank-statements-dataset).

## Features

- Visualize banking transactions by date, amount, category, etc.
- Analyze spending patterns and income trends.
- Interactive filtering and drill-downs.

## Project Structure

- `data/`: Raw and cleaned data CSVs (not tracked in Git)
- `pbix/`: Power BI `.pbix` files (dashboard project)
- `scripts/`: Data cleaning scripts (optional)
- `docs/`: Screenshots, documentation

## Usage

1. **Download the data:**
   - [Get the dataset from Kaggle](https://www.kaggle.com/datasets/abutalhadmaniyar/bank-statements-dataset)
   - Place it in the `data/` folder as `bank_statements.csv`

2. **(Optional) Clean the data:**
   - Use the Python script in `scripts/` if you want reproducible cleaning.
   - Place cleaned output in `data/bank_statements_cleaned.csv`

3. **Open the Power BI dashboard:**
   - Open `pbix/banking_dashboard.pbix` in Power BI Desktop
   - Update data source paths if prompted

4. **Explore the dashboard:**
   - Interact with visuals, slicers, and filters as desired

## Requirements

- [Power BI Desktop](https://powerbi.microsoft.com/desktop/)
- (Optional) Python 3.x and pandas if you run scripts

## License

MIT
