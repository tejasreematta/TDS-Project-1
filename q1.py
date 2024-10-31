#Who are the top 5 users in Seattle with the highest number of followers? 
#List their login in order, comma-separated.

import pandas as pd

# Load the users.csv file
users_df = pd.read_csv('users.csv')

# Sort the DataFrame by followers in descending order
top_users = users_df.sort_values(by='followers', ascending=False).head(5)

# Extract the logins of the top 5 users
top_user_logins = top_users['login'].tolist()

# Print the result as a comma-separated string

print(','.join(top_user_logins))
