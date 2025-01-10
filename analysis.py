import sqlite3
from collections import Counter
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('database.db')

# Create a cursor object
cur = conn.cursor()

# Example query to test the connection
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Print the list of tables
cur.execute("SELECT title FROM leetcode WHERE difficulty = 'Hard';")
hard_titles = cur.fetchall()
cur.execute("SELECT topic_tags FROM leetcode WHERE difficulty = 'Hard';")
hard_tags = cur.fetchall()

# Fetch all titles and tags from the query result
titles = [row[0] for row in hard_titles]
tags = [row[0] for row in hard_tags]

# Split titles into words and count the occurrences
word_counts = Counter(word for title in titles for word in title.split())

# Split tags into individual tags and count occurrences, ignoring None values
tag_counts = Counter(tag.strip("' ") for row in hard_tags if row[0] is not None for tag in row[0].split(','))

# List of common English words to exclude
common_words = {'the', 'and', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'with', 'by', 'of', 'from', 'as', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'that', 'which', 'who', 'whom', 'this', 'these', 'those', 'it', 'its', 'he', 'she', 'they', 'them', 'his', 'her', 'their', 'there', 'here', 'when', 'where', 'why', 'how', 'what', 'all', 'any', 'some', 'no', 'not', 'but', 'or', 'if', 'then', 'else', 'than', 'so', 'such', 'too', 'very', 'can', 'could', 'will', 'would', 'should', 'may', 'might', 'must', 'shall'}

# Filter out common words from the word counts
filtered_word_counts = Counter({word: count for word, count in word_counts.items() if word.lower() not in common_words})

# Replace the original word_counts with the filtered one
word_counts = filtered_word_counts

# Get the top 20 most common words and tags
top_20_words = word_counts.most_common(20)
top_20_tags = tag_counts.most_common(20)


# Separate the words, tags and their counts
words, word_counts = zip(*top_20_words)
tags, tag_counts = zip(*top_20_tags)

# Create a horizontal bar chart with different colors for each bar
plt.figure(figsize=(14, 10))

# Plot top 20 words
plt.subplot(1, 2, 1)
colors = plt.cm.viridis(range(len(words)))  # Use a colormap to generate different colors
plt.barh(words, word_counts, color=colors)
plt.xlabel('Count')
plt.ylabel('Words')
plt.title('Top 20 Words in Hard Leetcode Questions')
plt.gca().invert_yaxis()  # Invert y-axis to have the highest count at the top

# Plot top 20 tags
plt.subplot(1, 2, 2)
colors = plt.cm.plasma(range(len(tags)))  # Use a different colormap for tags
plt.barh(tags, tag_counts, color=colors)
plt.xlabel('Count')
plt.ylabel('Tags')
plt.title('Top 20 Tags in Hard Leetcode Questions')
plt.gca().invert_yaxis()  # Invert y-axis to have the highest count at the top

plt.tight_layout()
plt.show()
# Close the connection
conn.close()
