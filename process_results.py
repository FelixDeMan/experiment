import pandas as pd

df = pd.read_csv('yolo_eval_db.csv')


min_value = df['mean_confidence_score'].min()
max_value = df['mean_confidence_score'].max()

df['normalized_yolo'] =  (df['mean_confidence_score'] - min_value) / (max_value - min_value)



min_value = df['mean_ocr_score'].min()
max_value = df['mean_ocr_score'].max()

df['normalized_ocr'] = (df['mean_ocr_score'] - min_value) / (max_value - min_value)

print(df.head())

df['normalized_score'] = (df['normalized_yolo'] + df['normalized_ocr']) /2.

df.to_csv('yolo_eval_db_normalized.csv', index=False)