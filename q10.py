# Does creating more repos help users get more followers? 
# Using regression, estimate how many additional followers a user gets per additional public repository.
# Regression slope of followers on repos (to 3 decimal places, e.g. 0.123 or -0.123)

import pandas as pd
import statsmodels.api as sm

# Load the users.csv file
users_df = pd.read_csv('users.csv')

# Define the independent variable (X) and dependent variable (Y)
X = users_df['public_repos']
Y = users_df['followers']

# Add a constant to the independent variable
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(Y, X).fit()

# Get the slope (coefficient) for public_repos
slope = model.params['public_repos']

# Print the slope rounded to 3 decimal places
print(f"{slope:.3f}")
