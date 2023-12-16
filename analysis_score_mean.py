import pandas as pd

# Load the CSV file
df = pd.read_csv('On-Device-score_with_fill_Length.csv')

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
category_scores.to_csv('Category_Scores_Summary.csv', index=False)

