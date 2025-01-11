import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from CSV file
try:
    df = pd.read_csv('/Users/soumyajit/Documents/Programming/data_binge_team2/leetcode.csv')
except FileNotFoundError as e:
    print(f"An error occurred: {e}")
    df = pd.DataFrame()

# Clean the data
cleaned_data = df.dropna(subset=['difficulty', 'no_similar_questions'])

# Ensure 'difficulty' and 'no_similar_questions' columns exist before performing groupby operation
if 'difficulty' in cleaned_data.columns and 'no_similar_questions' in cleaned_data.columns:
    # Calculate mean, median, and standard deviation for each difficulty level
    stats = cleaned_data.groupby('difficulty')['no_similar_questions'].agg(['mean', 'median', 'std']).reset_index()
else:
    print("The required columns do not exist in the DataFrame.")
    stats = pd.DataFrame()

# Ensure 'difficulty', 'mean', 'median', and 'std' columns exist before plotting
if not stats.empty and all(col in stats.columns for col in ['difficulty', 'mean', 'median', 'std']):
    # Plot the statistics
    stats_melted = stats.melt(id_vars='difficulty', value_vars=['mean', 'median', 'std'], var_name='statistic', value_name='value')
    sns.barplot(x='difficulty', y='value', hue='statistic', data=stats_melted)
    plt.title('Statistics of No. of Similar Questions by Difficulty Level')
    plt.show()
else:
    print("The required columns for plotting do not exist in the DataFrame.")
