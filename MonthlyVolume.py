import pandas as pd
import numpy as np

df = pd.read_csv('CoreByVolAMR incl. before 2015.csv', thousands = ',')
df_out = pd.read_csv('CoreMonthlyVolume.csv', thousands = ',')

for i in df_out['user_name']:
	count = 0
	for j in df['user_name']:
		if i = j and df_out['user_name'][i]>10000:
			count++
	df_out['months_active_core'] = count





df.to_excel('outputJan.xlsx')