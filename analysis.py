import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('/Users/aw/Documents/GitHub/on-device-llm-privacy-analysis/On-Device-score.csv')

# Define a function to calculate the word count of responses
def word_count(text):
    return len(str(text).split())

# Calculate the word count for each response and add it to the DataFrame
df['Length 180B'] = df['180B Falcon Response'].apply(word_count)
df['Length On-Device'] = df['On-Device Falcon Response'].apply(word_count)

# Calculate average scores for accuracy and helpfulness by category
category_scores = df.groupby('Category').agg({
    'Accuracy Score 180B Falcon': 'mean',
    'Accuracy Score On-Device Falcon': 'mean',
    'Helpfulness Score 180B Falcon': 'mean',
    'Helpfulness Score On-Device Falcon': 'mean',
    'Length 180B': 'mean',
    'Length On-Device': 'mean'
}).reset_index()

threshold = 1
# Identify categories where the on-device LLM makes more mistakes
category_scores['Accuracy Gap'] = category_scores['Accuracy Score 180B Falcon'] - category_scores['Accuracy Score On-Device Falcon']
significant_gaps = category_scores[category_scores['Accuracy Gap'] > threshold]  # Adjust the threshold as needed

# Generate a word cloud for the 'Logical Reasoning Questions' category
logical_reasoning_text = " ".join(df[df['Category'] == 'Logical Reasoning Questions']['On-Device Falcon Response'].dropna())
wordcloud_logical = WordCloud(width=800, height=400, background_color='white').generate(logical_reasoning_text)

# Generate word clouds for each category
for category in df['Category'].unique():
    text = " ".join(df[df['Category'] == category]['On-Device Falcon Response'].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f'Word Cloud for {category}')
    plt.axis('off')
    plt.savefig(f'{category}_wordcloud.png')  # Save the word cloud as an image file
    plt.show()

# Plot a comparison of average scores
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))
category_scores.plot(x='Category', y=['Accuracy Score 180B Falcon', 'Accuracy Score On-Device Falcon'], kind='bar', ax=axes[0])
axes[0].set_title('Average Accuracy Scores by Category')
axes[0].set_ylabel('Accuracy Score')

category_scores.plot(x='Category', y=['Helpfulness Score 180B Falcon', 'Helpfulness Score On-Device Falcon'], kind='bar', ax=axes[1], color=['skyblue', 'orange'])
axes[1].set_title('Average Helpfulness Scores by Category')
axes[1].set_ylabel('Helpfulness Score')

plt.tight_layout()
plt.savefig('scores_comparison.png')  # Save the comparison chart as an image file
plt.show()

# Highlight the categories with significant accuracy gaps
if significant_gaps.empty:
    print("No significant accuracy gaps found.")
else:
    print("Categories with significant accuracy gaps:")
    print(significant_gaps[['Category', 'Accuracy Gap']])

# Save the analyzed data to a new CSV if needed
df.to_csv('/Users/aw/Documents/GitHub/on-device-llm-privacy-analysis/On-Device-score.csv', index=False)
