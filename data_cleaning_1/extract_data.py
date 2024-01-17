import pandas as pd
import numpy as np
import re

df = pd.read_csv('my_custom_data.csv')
# print(df.columns)

field = df.columns[2]
print(field)
custom_data = []

filtered_df = df[df[field].str.contains('organic_tag', case=False, na=False)]
# print(filtered_df)

pd.set_option('display.max_columns', None)
# print(filtered_df)

filtered_df['VALUE'] = np.where(filtered_df['VALUE'].str.contains(
    'review|rating|vote', case=False, na=False), filtered_df['VALUE'], np.NaN)
# print(filtered_df)
# filtered_df.to_csv('filtered.csv', index=False)

filtered_df["Rating"] = filtered_df['VALUE'].str.extract(r'Rating:\s*([\d.]+)', expand=False)
filtered_df["Review_total"] = filtered_df['VALUE'].str.extract(r'(\d+(?:\.\d+)?)\s*(?:reviews|vote)', expand=False)
filtered_df['Reviewer_Name'] = filtered_df['VALUE'].str.extract(r'Review by\s*([\w\s]+)', flags=re.IGNORECASE, expand=False)

new_df = pd.DataFrame()
new_df[['Organic_tag','Rating', 'Total_Review', 'Reviewer_Name']] = filtered_df[['VALUE', 'Rating', 'Review_total', 'Reviewer_Name']]
new_df.to_csv('organic_tag.csv', index=False)