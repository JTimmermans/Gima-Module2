#Created by Joris Timmermans | Contact: Joris.timmermans@outlook.com
#Merge B-riders original files to mapmatched data. Only use the necesary columns.

import glob
import pandas as pd



joinFrom = pd.read_csv('C:\Users\Joris\Google Drive\Gima\Module_2\Case_Study\Data\Simon\gps-match.csv')
joinFrom = joinFrom[['linknummer', 'routeid']]
	


folder = 'C:\Users\Joris\Google Drive\Gima\Module_2\Case_Study\Data\joinedtracks\*.csv'
for file in glob.glob(folder):
	joinTo = pd.read_csv(file)
	result = pd.merge(joinTo, joinFrom, left_on = 'track', right_on = 'routeid')
	result.to_csv('C:\Users\Joris\Google Drive\Gima\Module_2\Case_Study\Data\mapmatched_person_csv\{}.csv'.format(str(file[-8:-4]) + '__' + 'mp'), sep = ';')
	print file