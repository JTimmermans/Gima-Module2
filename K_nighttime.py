import pandas as pd
import glob
from datetime import datetime
from dateutil.parser import parse
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'

'''
#define function which defines if set times are within range
def isNowInTimePeriod(startTime, endTime, nowTime):
	if startTime < endTime:
		return (nowTime >= startTime) & (nowTime <= endTime)
	else: #Over midnight
		return (nowTime >= startTime) | (nowTime <= endTime)
'''




#Load unstructured file from KNMI containing sunrise and sunset dates per calendar day.
time_file = 'C:\Users\Joris\Google Drive\Gima\Module_2\Case_Study\Data\sun_rise_set_january_2014.csv'
time_df = pd.read_csv(time_file, sep=';')

#Concenate columns as strings for both sunrise and sunset
time_df['sunrise'] = time_df['y'].map(str)+'-'+time_df['m'].map(str)+'-'+time_df['d'].map(str)+' '+time_df['op'].map(str)
time_df['sunset'] = time_df['y'].map(str)+'-'+time_df['m'].map(str)+'-'+time_df['d'].map(str)+' '+time_df['onder'].map(str)
time_df['day_raw'] = time_df['y'].map(str)+'-'+time_df['m'].map(str)+'-'+time_df['d'].map(str)
#Convert sunrise and sunset columns to actual datetime properties

time_df['datetime_sunrise'] = pd.to_datetime(time_df['sunrise'])
time_df['datetime_sunset'] = pd.to_datetime(time_df['sunset'])
time_df['day'] = pd.to_datetime(time_df['day_raw'])

#Create a new dataframe with the sunrise and sunset datetime
time = time_df[['datetime_sunset', 'datetime_sunrise', 'day']]
del time_df
print(time.head())


folder = 'D:\\b-riders\Data\\np_no_duplicates\*.csv'
result = pd.DataFrame(columns=['person','tot_length_night', 'night'])


#read over all csv files and determine if a trip started during dark hours
for file in glob.glob(folder):
	#Load csv's and select appropriate columns
	df1 = pd.read_csv(file, sep = ';', decimal = ',')
	df2 = df1[['lengte', 'datetime', 'person', 'track']]

	#set datetime column to datetime2
	df2['datetime2'] = pd.to_datetime(df2['datetime'])

	#select the day date, drop hours and minutes
	df2['day_raw']=df2['datetime2'].dt.date
	df2['day']=pd.to_datetime(df2['day_raw'])
	del df2['day_raw']
	del df2['datetime']

	#merge tracks on date(day)
	joinTo = df2
	joinFrom = time
	merge = pd.merge(joinTo, joinFrom, left_on = 'day', right_on = 'day')
	empty = pd.DataFrame()

	#create a colun that is true if during the day
	current_time = merge['datetime2']
	sunrise = merge['datetime_sunrise']
	sunset = merge['datetime_sunset']
	merge['during_day'] = (sunset >= current_time) & (current_time >= sunrise)

	#select all day columns and calculate total meters during the day
	df3 = merge[(merge.during_day == True )]
	df3['length_during_day'] = df3['lengte'].sum()
	df4 = df3[['length_during_day', 'person']]
	df4 = df4.drop_duplicates(subset = ['person'])
	df4['person'] = df4['person'].astype(str)

	result= result.append(df4)
	print('x')
'''
	#For each row determine if time is within dark hours, if so, df2['night']=true.
	for index, row in df2.iterrows():
		current_time = merge['datetime2']
		sunrise = merge['datetime_sunrise']
		sunset = merge['datetime_sunset']
		merge['night'] = (sunset <= current_time) & (current_time<= sunrise)
		empty = empty.append(merge)
'''

	
test = result.to_csv('D:\\b-riders\Data\\night.csv', sep = ';', decimal = ',', index = False)

'''
	df3 = df2[(df2.wegdeksrt == 'asfalt/beton' )]
	df3['length_asphalt'] = df3['lengte'].sum()
	df4 = df3[['length_asphalt', 'person']]
	df4 = df4.drop_duplicates(subset = ['person'])
	df4['person'] = df4['person'].astype(str)
	exit = exit.append(df4)

print exit.head()

exit.to_csv('D:\\b-riders\Data\\length_asphalt.csv', sep = ';', decimal = ',', index=False)

result = result.to_csv('D:\\b-riders\Data\\testennnn.csv', sep = ';', decimal = ',', index = False)
'''