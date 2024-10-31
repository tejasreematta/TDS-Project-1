#Which programming language is the second most popular among users who joined after 2020?

import pandas as pd

# Load the users.csv file
users_df = pd.read_csv('users.csv')

# Convert the created_at column to datetime
users_df['created_at'] = pd.to_datetime(users_df['created_at'])

# Filter users who joined after 2020
recent_users = users_df[users_df['created_at'] > '2020-01-01']

# Load the repositories.csv file
repos_df = pd.read_csv('repositories.csv')

# Merge the two DataFrames on the 'login' field
merged_df = recent_users.merge(repos_df, on='login')

# Count occurrences of each programming language among recent users
language_counts = merged_df['language'].value_counts()

# Get the second most popular programming language
second_most_popular_language = language_counts.nlargest(2).idxmin()
print(second_most_popular_language)
