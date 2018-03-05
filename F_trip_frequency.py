import pandas as pd
import os
import glob
import random
import numpy as np
#pd.options.mode.chained_assignment = None  # default='warn'



folder = 'D:\\b-riders\Data\joinedtracks\*.csv'

exit = pd.DataFrame()

#iterate over all files and calculate the trip frequency per person
for file in glob.glob(folder):
	#Read csv, extract neccesary columns and drop duplicate rows, to obtain unique tracks
	df1 = pd.read_csv(file, sep = ',')
	df2 = df1[['person', 'track']]
	df3 = df2.drop_duplicates(subset = ['track'])
	#Add column with no values for indexing
	df3['count'] = np.nan
	#Count rows per file and drop duplicates
	df3['count'] = len(df3.index)
	df4 = df3.drop_duplicates(subset = ['person'])
	#Delete columns
	del df4['track']
	#append to file
	exit = exit.append(df4)
	del df1
	del df2
	del df3

print exit.head()
exit.to_csv('C:\Users\Joris\Google Drive\Gima\Module_2\Case_Study\Data\\tripfrequency.csv', sep = ';', decimal = ',', index = False)