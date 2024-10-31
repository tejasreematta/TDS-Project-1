#Which programming language is most popular among these users?

import pandas as pd

# Load the repositories.csv file
repos_df = pd.read_csv('repositories.csv')

# Count occurrences of each programming language, ignoring missing values
language_counts = repos_df['language'].value_counts()

# Identify the most popular programming language
most_popular_language = language_counts.idxmax()
print(most_popular_language)
