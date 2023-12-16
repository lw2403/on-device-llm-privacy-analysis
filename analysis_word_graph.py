import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('On-Device-score_with_fill_Length.csv')

# Function to generate word clouds
def generate_word_clouds(category, column_name, title):
    text = " ".join(df[df['Category'] == category][column_name].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f'Word Cloud for {title} in {category}')
    plt.axis('off')
    #plt.show()
    plt.savefig(f"word_graph/{category}_{column_name}_{title}.png")



# Generate word clouds for each model and category
for category in df['Category'].unique():
    generate_word_clouds(category, '180B Falcon Response', '180B Falcon')
    generate_word_clouds(category, 'On-Device Falcon Response', 'On-Device Falcon')
