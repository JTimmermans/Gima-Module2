import pandas as pd
import os
import glob
pd.options.mode.chained_assignment = None  # default='warn'



folder = 'D:\\b-riders\Data\\np_no_duplicates\*.csv'

exit = pd.DataFrame(columns=['person', 'count'])

#iterate over all files and calculate the trip frequency per person
for file in glob.glob(folder):
	df1 = pd.read_csv(file, sep = ';', decimal=',')
	df2 = df1[['person', 'track']]
	df2['count'] = df2.groupby('track')['person'].nunique()
	df3 = df2[df2['count'].notnull()]
	df3 = df2.drop_duplicates(subset = ['person', 'count'])
	#df3=df2.ix[df2['count'] < 0 ]
	del df3['track']
	exit = exit.append(df3)
	del df1
	del df2
	del df3

print exit.head()
exit.to_csv('C:\Users\Joris\Google Drive\Gima\Module_2\Case_Study\Data\\tripfrequency.csv', sep = ';', decimal = ',', index = False)
