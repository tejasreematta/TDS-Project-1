# Do people typically enable projects and wikis together? 
# What is the correlation between a repo having projects enabled and having wiki enabled?
# Correlation between projects and wiki enabled (to 3 decimal places, e.g. 0.123 or -0.123)

import pandas as pd

# Load the repositories.csv file
repos_df = pd.read_csv('repositories.csv')

# Convert has_projects and has_wiki to integers (1 for True, 0 for False)
repos_df['has_projects'] = repos_df['has_projects'].astype(int)
repos_df['has_wiki'] = repos_df['has_wiki'].astype(int)

# Calculate the correlation between having projects enabled and having wiki enabled
correlation = repos_df['has_projects'].corr(repos_df['has_wiki'])

# Print the result rounded to 3 decimal places
print(f"{correlation:.3f}")
