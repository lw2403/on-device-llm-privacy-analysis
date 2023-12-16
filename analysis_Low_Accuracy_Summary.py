import pandas as pd

# Load the CSV file
df = pd.read_csv('On-Device-score_with_fill_Length.csv')

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
low_accuracy_table.to_csv('Low_Accuracy_Summary.csv', index=False)
print(f'Number of low accuracy responses: {len(low_accuracy_table)}')

# Print the low accuracy table for console output
print(low_accuracy_table)
