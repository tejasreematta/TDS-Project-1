#Which language has the highest average number of stars per repository?

import pandas as pd

# Load the repositories.csv file
repos_df = pd.read_csv('repositories.csv')

# Group by language and calculate the average number of stars
average_stars = repos_df.groupby('language')['stargazers_count'].mean()

# Identify the language with the highest average number of stars
highest_average_language = average_stars.idxmax()
highest_average_value = average_stars.max()

print(f"Language: {highest_average_language}, Average Stars: {highest_average_value:.2f}")
