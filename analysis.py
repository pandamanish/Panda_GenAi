
import pandas as pd

# Load the dataset
file_path = 'HDFC.xlsx'
data = pd.read_excel(file_path)

# Convert 'Date' and 'Value Dt' columns to datetime
data['Date'] = pd.to_datetime(data['Date'])
data['Value Dt'] = pd.to_datetime(data['Value Dt'])

# Fill NaN values with 0 for numerical calculations
data['Withdrawal Amt.'] = data['Withdrawal Amt.'].fillna(0)
data['Deposit Amt.'] = data['Deposit Amt.'].fillna(0)

# Group by 'Date' and calculate the required statistics
day_wise_stats = data.groupby(data['Date'].dt.date).agg({
    'Narration': 'count',
    'Withdrawal Amt.': 'sum',
    'Deposit Amt.': 'sum',
    'Closing Balance': 'last'
}).rename(columns={
    'Narration': 'Total Transactions',
    'Withdrawal Amt.': 'Total Withdrawal Amt.',
    'Deposit Amt.': 'Total Deposit Amt.',
    'Closing Balance': 'Closing Balance'
})

day_wise_stats.reset_index(inplace=True)
day_wise_stats.columns = ['Date', 'Total Transactions', 'Total Withdrawal Amt.', 'Total Deposit Amt.', 'Closing Balance']

# Display the first few rows of the result
print(day_wise_stats.head())

# Save the results to a new Excel file
#day_wise_stats.to_excel('day_wise_statistics.xlsx', index=False)
