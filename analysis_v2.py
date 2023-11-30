import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Function to calculate word count
def word_count(text):
    return len(str(text).split())

# Function to generate word clouds
def generate_word_clouds(category, column_name, title):
    text = " ".join(df[df['Category'] == category][column_name].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f'Word Cloud for {title} in {category}')
    plt.axis('off')
    plt.show()

# Load the CSV file
df = pd.read_csv('/Users/aw/Documents/GitHub/on-device-llm-privacy-analysis/On-Device-score.csv')

# Calculate word counts for each response
df['Length 180B Falcon'] = df['180B Falcon Response'].apply(word_count)
df['Length On-Device Falcon'] = df['On-Device Falcon Response'].apply(word_count)

# Calculate average scores and lengths by category
category_scores = df.groupby('Category').agg({
    'Accuracy Score 180B Falcon': 'mean',
    'Accuracy Score On-Device Falcon': 'mean',
    'Helpfulness Score 180B Falcon': 'mean',
    'Helpfulness Score On-Device Falcon': 'mean',
    'Length 180B Falcon': 'mean',
    'Length On-Device Falcon': 'mean'
}).reset_index()

# Save the summary table to a text file
category_scores.to_csv('/Users/aw/Documents/GitHub/on-device-llm-privacy-analysis/Category_Scores_Summary.txt', sep='\t', index=False)

# Generate word clouds for each model and category
# for category in df['Category'].unique():
#     generate_word_clouds(category, '180B Falcon Response', '180B Falcon')
#     generate_word_clouds(category, 'On-Device Falcon Response', 'On-Device Falcon')

# Identifying responses with low accuracy scores (3, 2, or 1)
low_accuracy = df[(df['Accuracy Score 180B Falcon'] <= 3) | (df['Accuracy Score On-Device Falcon'] <= 3)]

# Creating a table of responses with low accuracy
low_accuracy_table = low_accuracy[['Category', 
                                   'Question', 
                                   '180B Falcon Response', 
                                   'Accuracy Score 180B Falcon', 
                                   'On-Device Falcon Response', 
                                   'Accuracy Score On-Device Falcon']]

# Save the low accuracy table to a text file
low_accuracy_table.to_csv('/Users/aw/Documents/GitHub/on-device-llm-privacy-analysis/Low_Accuracy_Summary.txt', sep='\t', index=False)
print(f'Number of low accuracy responses: {len(low_accuracy_table)}')

# Print the low accuracy table for console output
print(low_accuracy_table)
