# Ensure the virtual environment is activated
import os
import sys

venv_path = os.path.join(os.path.dirname(__file__), '.venv', 'bin', 'activate_this.py')
if os.path.exists(venv_path):
    with open(venv_path) as f:
        exec(f.read(), {'__file__': venv_path})
else:
    print("Virtual environment not found. Please create one using 'python -m venv .venv' and install the required packages.")

# Ensure required packages are installed
required_packages = ['sqlite3', 'collections', 'seaborn', 'pandas', 'matplotlib']
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"Package {package} not found. Please install it using 'pip install {package}'.")

import sqlite3
from collections import Counter
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

        # Create a swarm plot
        plt.figure(figsize=(10, 6))
        sns.swarmplot(x='difficulty', y='no_similar_questions', data=data)
        plt.title('Swarm Plot of Difficulty Levels vs. Number of Similar Questions')
        plt.xlabel('Difficulty Level')
        plt.ylabel('Number of Similar Questions')
        plt.show()

# Example of how to use cleaned_data
print(f"Cleaned data has {len(cleaned_data)} entries out of {len(rows)} total entries.")
# Close the connection
conn.close()
