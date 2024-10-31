# Who created the most repositories on weekends (UTC)? 
# List the top 5 users' login in order, comma-separated
# Users login

import pandas as pd

# Load the repositories.csv file
repos_df = pd.read_csv('repositories.csv')

# Convert created_at to datetime
repos_df['created_at'] = pd.to_datetime(repos_df['created_at'])

# Filter for weekend days (Saturday and Sunday)
repos_df['day_of_week'] = repos_df['created_at'].dt.dayofweek
weekend_repos = repos_df[repos_df['day_of_week'].isin([5, 6])]  # 5 = Saturday, 6 = Sunday

# Group by user login and count repositories
repo_counts = weekend_repos.groupby('login').size().reset_index(name='count')

# Sort by count and select the top 5 users
top_users = repo_counts.sort_values(by='count', ascending=False).head(5)

# Extract the logins of the top users
top_user_logins = top_users['login'].tolist()

# Print the result as a comma-separated string
print(', '.join(top_user_logins))
