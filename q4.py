#Which company do the majority of these developers work at?

import pandas as pd

# Load the users.csv file
users_df = pd.read_csv('users.csv')

# Clean up the company names
users_df['company'] = users_df['company'].str.strip()  # Remove leading/trailing whitespace
users_df['company'] = users_df['company'].str.lstrip('@')  # Remove leading '@' symbol
users_df['company'] = users_df['company'].str.upper()  # Convert to uppercase

# Count occurrences of each company
company_counts = users_df['company'].value_counts()

# Identify the most common company
most_common_company = company_counts.idxmax()
print(most_common_company)
