#calculating sum totals and appending to new or existing dataframe
import pandas as pd
import glob
pd.options.mode.chained_assignment = None  # default='warn'




folder = 'D:\\b-riders\Data\\np_no_duplicates\*.csv'

exit = pd.DataFrame(columns=['person','length_nature'])


#read over all csv files and calculate total of greenway usage
for file in glob.glob(folder):
	df1 = pd.read_csv(file, sep = ';', decimal = ',')
	df2 = df1[['lengte', 'omgeving', 'person']]
	df3 = df2[(df2.omgeving == 'bos' ) | (df2.omgeving == 'natuur (behalve bos)' ) | (df2.omgeving == 'akkers/weilanden' ) | (df2.omgeving == 'bebouwd (veel groen)' )]
	df3['length_nature'] = df3['lengte'].sum()
	df4 = df3[['length_nature', 'person']]
	df4 = df4.drop_duplicates(subset = ['person'])
	df4['person'] = df4['person'].astype(str)
	exit = exit.append(df4)

print exit.head()

exit.to_csv('D:\\b-riders\Data\\length_nature.csv', sep = ';', decimal = ',', index=False)
