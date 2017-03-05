#Code to determine how long a user traded before becoming core
#Author: Annie Tang
#Date: February 24, 2017

import pandas as pd
import math
import numpy as np

df = pd.read_csv('MonthToCore.csv', thousands = ',')

df['Core Month'] = pd.to_datetime(df['Core Month'], format='%y-%b')
df['NTA Month'] = pd.to_datetime(df['NTA Month'], format = '%y-%b')

df['day_to_core'] = df['Core Month'] - df['NTA Month']

days = df['day_to_core']/np.timedelta64(1, 'D')
df['month_to_core'] = days.apply(lambda x: round(x/30))

#1-2 months, 3-5 months, more than 5 months
def func(row):
	if row['month_to_core'] < 2: 
		return 1
	elif row['month_to_core'] < 5:
		return 2
	else:
		return 3

df['month_category'] = df.apply(func, axis = 1)

df.to_excel('Output MonthToCore.xlsx')