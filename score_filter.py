import pandas as pd
df = pd.read_csv('On-Device-score.csv')

score_df = df[ [ 'Accuracy Score 180B Falcon',
    'Accuracy Score On-Device Falcon',
    'Helpfulness Score 180B Falcon',
    'Helpfulness Score On-Device Falcon',] ]

df1 = df[score_df.apply(lambda row:row.le(1).any(), axis=1)]

df2 = df[score_df.apply(lambda row: row.le(2).any(), axis=1)]

df3 = df[score_df.apply(lambda row: row.le(3).any(), axis=1)]

df1.to_csv('score_eq_1.csv', index=False)
df2.to_csv('score_le_2.csv', index=False)
df3.to_csv('score_le_3.csv', index=False)