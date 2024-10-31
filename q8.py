# Let's define leader_strength as followers / (1 + following). 
# Who are the top 5 in terms of leader_strength? List their login in order, comma-separated.

import pandas as pd

# Load the users.csv file
users_df = pd.read_csv('users.csv')

# Calculate leader_strength
users_df['leader_strength'] = users_df['followers'] / (1 + users_df['following'])

# Sort the DataFrame by leader_strength in descending order
top_leaders = users_df.sort_values(by='leader_strength', ascending=False).head(5)

# Extract the logins of the top 5 users
top_leader_logins = top_leaders['login'].tolist()

# Print the result as a comma-separated string
print(', '.join(top_leader_logins))
