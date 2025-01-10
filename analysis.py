import sqlite3
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('database.db')

# Create a cursor object
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Example query to test the connection
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch data from the table
cur.execute("SELECT * FROM leetcode;")
rows = cur.fetchall()

# Clean the data
cleaned_data = []
for row in rows:
    if row['difficulty'] is not None and row['no_similar_questions'] is not None:
        cleaned_data.append(row)

# Extract difficulty levels and number of similar questions
difficulty_levels = [row['difficulty'] for row in cleaned_data]
no_similar_questions = [row['no_similar_questions'] for row in cleaned_data]

# Create a DataFrame for plotting
data = pd.DataFrame({
    'difficulty': difficulty_levels,
    'no_similar_questions': no_similar_questions
})

# Ensure 'difficulty' is treated as an ordered categorical variable
#difficulty_order = ['Easy', 'Medium', 'Hard']  # Adjust as necessary based on your dataset
#data['difficulty'] = pd.Categorical(data['difficulty'], categories=difficulty_order, ordered=True)

# Create a swarm plot with different colors for difficulty levels
plt.figure(figsize=(12, 6))  # Make the plot larger
sns.swarmplot(x='difficulty', y='no_similar_questions', data=data, size=1)
plt.title('Swarm Plot of Number of Similar Questions vs. Difficulty Levels')
plt.xlabel('Difficulty Level')
plt.ylabel('Number of Similar Questions')
plt.show()

# Close the connection
conn.close()
