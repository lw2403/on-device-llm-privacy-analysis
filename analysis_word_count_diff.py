import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('On-Device-score_with_fill_Length.csv')

category_scores = df[[ 'Category','Length 180B Falcon','Length On-Device Falcon']]\
    .groupby('Category').agg({
    'Length 180B Falcon': 'sum',
    'Length On-Device Falcon': 'sum'}).reset_index()
print(category_scores)



df = category_scores


plt.figure(figsize=(12, 8))


index = range(len(df['Category']))
bar_height = 0.35

plt.barh([i - bar_height/2 for i in index], df['Length 180B Falcon'], bar_height, label='Length 180B Falcon')
plt.barh([i + bar_height/2 for i in index], df['Length On-Device Falcon'], bar_height, label='Length On-Device Falcon')


plt.legend()


plt.title('Category wise Word Count Comparison')
plt.ylabel('Category')
plt.xlabel('Sum Of Word Count')


plt.yticks(index, df['Category'])


plt.tight_layout()


plt.savefig('analysis_word_count_diff.png', dpi=300, bbox_inches='tight')


plt.show()