#calculating sum totals and appending to new or existing dataframe
import pandas as pd
import glob


folder = 'D:\\b-riders\Data\\np_no_duplicates\*.csv'

result = pd.DataFrame(columns=['person','tot_length'])
print result

#read over all csv files and create seperate csv based on tripnr
for file in glob.glob(folder):
	df1 = pd.read_csv(file, sep = ';', decimal = ',')
	df1['tot_length'] = df1['lengte'].sum()
	df2=df1[['tot_length', 'person']]
	df2 = df2.drop_duplicates(subset = ['person', 'tot_length'])
	df2['person'] = df2['person'].astype(str)
	result = result.append(df2)
	#print result.head()

result = result.to_csv('D:\\b-riders\Data\\testennnn.csv', sep = ';', decimal = ',', index = False)
