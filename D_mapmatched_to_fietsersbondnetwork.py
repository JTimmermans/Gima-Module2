#Created by Joris Timmermans | Contact: Joris.timmermans@outlook.com
#function to merge B-riders original files to mapmatched data.

import glob
import pandas as pd



joinFrom = pd.read_csv('C:\Users\Joris\Google Drive\Gima\Module_2\Case_Study\Data\Simon\\fietsnet_linkscor.csv', sep = ';', decimal = ',')

	


folder = 'C:\Users\Joris\Google Drive\Gima\Module_2\Case_Study\Data\mapmatched_person_csv\*.csv'
for file in glob.glob(folder):
	joinTo = pd.read_csv(file, sep = ';')
	result = pd.merge(joinTo, joinFrom, left_on = 'linknummer', right_on = 'LINKNUMMER')
	result = result.drop_duplicates(subset = ['linknummer', 'routeid'])
	result.to_csv('D:\\b-riders\Data\\np_no_duplicates\{}.csv'.format(str(file[-12:-8]) + '__' + 'np'), sep = ';', decimal=',', index=False)
	print file