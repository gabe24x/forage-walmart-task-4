import pandas as pd
import sqlite3

conn = sqlite3.connect('path_to_your_database.db')
cursor = conn.cursor()

df0 = pd.read_excel('path_to_spreadsheet0.xlsx')
df1 = pd.read_excel('path_to_spreadsheet1.xlsx')
df2 = pd.read_excel('path_to_spreadsheet2.xlsx')

df0.to_sql('table_name', conn, if_exists='append', index=False)


merged_df = df1.merge(df2, on='shipping_identifier')
merged_df['total_quantity'] = df1.groupby('shipping_identifier')['quantity'].transform(sum)
merged_df.to_sql('table_name', conn, if_exists='append', index=False)

conn.commit()
conn.close()
