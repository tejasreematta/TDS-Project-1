# Do hireable users follow more people than those who are not hireable?
# Average of following per user for hireable=true minus the average following for the rest (to 3 decimal places, e.g. 12.345 or -12.345)

import pandas as pd

# Load the users.csv file
users_df = pd.read_csv('users.csv')

# Fill empty cells in the hireable column with False
users_df['hireable'] = users_df['hireable'].fillna(False)

# Convert the hireable column to boolean
users_df['hireable'] = users_df['hireable'].map({True: True, False: False})

# Calculate the average following for hireable users
average_following_hireable = users_df[users_df['hireable'] == True]['following'].mean()

# Calculate the average following for non-hireable users
average_following_non_hireable = users_df[users_df['hireable'] == False]['following'].mean()

# Compute the difference
following_difference = average_following_hireable - average_following_non_hireable

# Print the result rounded to 3 decimal places
print(f"{following_difference:.3f}")
