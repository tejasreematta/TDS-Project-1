# Let's assume that the last word in a user's name is their surname (ignore missing names, trim and split by whitespace.) 
# What's the most common surname? (If there's a tie, list them all, comma-separated, alphabetically)
# Most common surname(s)

import pandas as pd

# Load the users.csv file
users_df = pd.read_csv('users.csv')

# Drop rows where name is missing
users_df = users_df[users_df['name'].notna()]

# Extract surnames by splitting the name and taking the last word
users_df['surname'] = users_df['name'].str.strip().str.split().str[-1]

# Count occurrences of each surname
surname_counts = users_df['surname'].value_counts()

# Identify the maximum count
max_count = surname_counts.max()

# Get the most common surnames (those with the maximum count)
most_common_surnames = surname_counts[surname_counts == max_count].index.tolist()

# Sort the surnames alphabetically
most_common_surnames.sort()

# Print the result as a comma-separated string
print(', '.join(most_common_surnames))
