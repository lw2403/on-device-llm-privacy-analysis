import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('On-Device-score.csv')

category_scores = df[[ 'Category','Accuracy Score 180B Falcon','Accuracy Score On-Device Falcon']]\
    .groupby('Category').agg({
    'Accuracy Score 180B Falcon': 'sum',
    'Accuracy Score On-Device Falcon': 'sum'}).reset_index()
print(category_scores)





df = category_scores


plt.figure(figsize=(12, 8))


index = range(len(df['Category']))
bar_height = 0.35

plt.barh([i - bar_height/2 for i in index], df['Accuracy Score 180B Falcon'], bar_height, label='Accuracy Score 180B Falcon')
plt.barh([i + bar_height/2 for i in index], df['Accuracy Score On-Device Falcon'], bar_height, label='Accuracy Score On-Device Falcon')


plt.legend()


plt.title('Category wise Accuracy Comparison')
plt.ylabel('Category')
plt.xlabel('Sum Of Accuracy Score')


plt.yticks(index, df['Category'])


plt.tight_layout()


plt.savefig('analysis_accuracy_score_sum_diff.png', dpi=300, bbox_inches='tight')


plt.show()