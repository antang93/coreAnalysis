# Program to add a column for core user or not, 

import pandas as pd
import numpy as np

df = pd.read_csv('JanByVol.csv')
df_core = pd.read_csv('Core Americas.csv', thousands = ',')
df_feb = pd.read_csv('FebToDate26Feb')

df['core'] = df['Username'].isin(df_core['Username'])

for i in df['Username']:
	if i in df_feb['Username']:
		df['Feb_vol'] = 


df.to_excel('outputJan.xlsx')