import pandas as pd

# Function to calculate word count
def word_count(text):
    return len(str(text).split())

# Load the CSV file
df = pd.read_csv('On-Device-score.csv')

# Calculate word counts for each response
df['Length 180B Falcon'] = df['180B Falcon Response'].apply(word_count)
df['Length On-Device Falcon'] = df['On-Device Falcon Response'].apply(word_count)

df.to_csv('On-Device-score_with_fill_Length.csv')
