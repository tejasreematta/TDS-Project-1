#What are the 3 most popular license among these users? Ignore missing licenses. 
#List the license_name in order, comma-separated.

import pandas as pd

# Load the repositories.csv file
repos_df = pd.read_csv('repositories.csv')

# Filter out rows with missing license names
filtered_repos = repos_df[repos_df['license_name'].notna()]

# Count occurrences of each license
license_counts = filtered_repos['license_name'].value_counts()

# Get the top 3 most popular licenses
top_licenses = license_counts.head(3)

# Print the result as a comma-separated string
popular_licenses = ','.join(top_licenses.index)
print(popular_licenses)
