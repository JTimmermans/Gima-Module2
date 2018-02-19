#calculating sum totals and appending to new or existing dataframe
import pandas as pd
import glob
pd.options.mode.chained_assignment = None  # default='warn'




result = pd.read_csv('D:\\b-riders\Data\\testennnn.csv', sep = ';', decimal = ',')
folder = 'D:\\b-riders\Data\\np_no_duplicates\*.csv'
result['person'] = result['person'].astype(str)
print result.head()

exit = result = pd.DataFrame(columns=['person','length_cpath'])

#read over all csv files and create seperate csv based on tripnr
for file in glob.glob(folder):
	df1 = pd.read_csv(file, sep = ';', decimal = ',')
	df2 = df1[['lengte', 'wegtype', 'person']]
	df3 = df2[(df2.wegtype == 'bromfietspad (langs weg)') | (df2.wegtype == 'fietspad (langs weg)') | (df2.wegtype == 'solitair bromfietspad') | (df2.wegtype=='solitair fietspad')]
	df3['length_cpath'] = df3['lengte'].sum()
	df4 = df3[['length_cpath', 'person']]
	df4 = df4.drop_duplicates(subset = ['person'])
	df4['person'] = df4['person'].astype(str)
	exit = exit.append(df4)

print exit.head()

exit.to_csv('D:\\b-riders\Data\\testennnn1.csv', sep = ';', decimal = ',', index=False)


