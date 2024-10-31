# TDS-Project-1

# GitHub User Analysis in Seattle

- This project analyzes GitHub users in Seattle with over 200 followers, focusing on their repositories and activity.
- One surprising finding is that though there is a correlation between followers and public repositories, it is only 0.203, indicating other factors influence follower counts.
- Developers should consider enhancing their profiles and engaging more with the community, as follower counts are not solely dependent on repository numbers.

## Data Scraping Explanation
The data was scraped using the GitHub API, specifically targeting users in Seattle with more than 200 followers. User information and repository details were stored in two CSV files: `users.csv` and `repositories.csv`. Data cleaning and processing were performed using Python with Pandas.

## Interesting Findings
1. **Top Users**: The top five users in Seattle by followers are vczh, bradfitz, munificent, tenderlove, and ahmetb.
2. **Earliest Users**: The five earliest registered users include topfunky, nex3, beccasaurus, eric, and grantr.
3. **Popular Licenses**: The three most common licenses among users are MIT, Apache-2.0, and other.
4. **Most Common Company**: The majority of these developers work at MICROSOFT.
5. **Language Popularity**: JavaScript is the most popular programming language among these users.
6. **Correlation Analysis**: 
   - There is a weak positive correlation (0.1009) between being hireable and the number of public repositories.
   - A very weak negative correlation (-0.0377) exists between being hireable and follower count, indicating hireable users do not necessarily have more followers.
   - The moderate correlation (0.2034) between public repositories and followers suggests that users with more repositories tend to have more followers.
   - Overall, being hireable does not significantly correlate with activity metrics.

## Recommendations
Developers should optimize their GitHub profiles by clearly articulating their skills and contributions. Engaging with the community through meaningful interactions and maintaining an active presence can significantly impact follower growth, even beyond the quantity of repositories created.
