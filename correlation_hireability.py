import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the users.csv file
users_df = pd.read_csv('users.csv')

# Fill empty cells in the hireable column with False
users_df['hireable'] = users_df['hireable'].fillna(False)

# Select relevant columns for analysis
activity_metrics = users_df[['hireable', 'public_repos', 'followers', 'following']]

# Calculate correlations
correlations = activity_metrics.corr()

# Print the correlation matrix
print(correlations)

# Set up the matplotlib figure
plt.figure(figsize=(8, 6))

# Create a heatmap with annotations
sns.heatmap(correlations, annot=True, cmap='coolwarm', fmt=".2f", square=True, cbar_kws={"shrink": .8})

# Set title and labels
plt.title('Correlation Matrix of GitHub Users in Seattle')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
