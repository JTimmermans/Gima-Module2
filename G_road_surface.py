#calculating sum totals and appending to new or existing dataframe
import pandas as pd
import glob
pd.options.mode.chained_assignment = None  # default='warn'






folder = 'D:\\b-riders\Data\\np_no_duplicates\*.csv'

exit = pd.DataFrame(columns=['person','length_asphalt'])


#read over all csv files and create seperate csv based on tripnr
for file in glob.glob(folder):
	df1 = pd.read_csv(file, sep = ';', decimal = ',')
	df2 = df1[['lengte', 'wegdeksrt', 'person']]
	df3 = df2[(df2.wegdeksrt == 'asfalt/beton' )]
	df3['length_asphalt'] = df3['lengte'].sum()
	df4 = df3[['length_asphalt', 'person']]
	df4 = df4.drop_duplicates(subset = ['person'])
	df4['person'] = df4['person'].astype(str)
	exit = exit.append(df4)

print exit.head()

exit.to_csv('D:\\b-riders\Data\\length_asphalt.csv', sep = ';', decimal = ',', index=False)

