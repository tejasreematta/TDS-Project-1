#What is the correlation between the number of followers and the number of public repositories among users in Seattle?
#Correlation between followers and repos (to 3 decimal places, e.g. 0.123 or -0.123)

import pandas as pd

# Load the users.csv file
users_df = pd.read_csv('users.csv')

# Calculate the correlation between followers and public_repos
correlation = users_df['followers'].corr(users_df['public_repos'])

# Print the result rounded to 3 decimal places
print(f"{correlation:.3f}")
