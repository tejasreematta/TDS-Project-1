# Do people who are hireable share their email addresses more often?
# [fraction of users with email when hireable=true] minus [fraction of users with email for the rest] (to 3 decimal places, e.g. 0.123 or -0.123)

import pandas as pd

# Load the users.csv file
users_df = pd.read_csv('users.csv')

# Fill empty cells in the hireable column with False
users_df['hireable'] = users_df['hireable'].fillna(False)

# Calculate the total number of users for hireable and non-hireable
total_hireable = users_df[users_df['hireable'] == True].shape[0]
total_non_hireable = users_df[users_df['hireable'] == False].shape[0]

# Calculate the number of users with emails
emails_hireable = users_df[users_df['hireable'] == True]['email'].notna().sum()
emails_non_hireable = users_df[users_df['hireable'] == False]['email'].notna().sum()

# Calculate the fractions
fraction_hireable = emails_hireable / total_hireable if total_hireable > 0 else 0
fraction_non_hireable = emails_non_hireable / total_non_hireable if total_non_hireable > 0 else 0

# Compute the difference
email_difference = fraction_hireable - fraction_non_hireable

# Print the result rounded to 3 decimal places
print(f"{email_difference:.3f}")
