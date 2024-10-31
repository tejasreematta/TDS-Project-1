#Who are the 5 earliest registered GitHub users in Seattle? 
#List their login in ascending order of created_at, comma-separated.

import pandas as pd

# Load the users.csv file
users_df = pd.read_csv('users.csv')

# Convert the created_at column to datetime
users_df['created_at'] = pd.to_datetime(users_df['created_at'])

# Sort the DataFrame by created_at in ascending order
earliest_users = users_df.sort_values(by='created_at').head(5)

# Extract the logins of the earliest users
earliest_user_logins = earliest_users['login'].tolist()

# Print the result as a comma-separated string
print(','.join(earliest_user_logins))
