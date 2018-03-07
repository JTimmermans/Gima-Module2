import pandas as pd
import glob
from datetime import datetime
from dateutil.parser import parse
import numpy as np

#Hide warnings, after checking the date the warning to use .loc did not affect the data result.
pd.options.mode.chained_assignment = None  # default='warning

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

#Set folder and create an empty dataframe to store the results
folder = 'D:\\b-riders\Data\\np_no_duplicates\*.csv'
result = pd.DataFrame(columns=['person','length_night' ])

#Read over all csv files and determine if a trip started during dark hours
for file in glob.glob(folder):
	#Load csv's and select appropriate columns
	df1 = pd.read_csv(file, sep = ';', decimal = ',')
	df2 = df1[['lengte', 'datetime', 'person', 'track']]

	#Set datetime column to datetime2
	df2['datetime2'] = pd.to_datetime(df2['datetime'])

	#Select the day date, drop hours and minutes
	df2['day_raw']=df2['datetime2'].dt.date
	df2['day']=pd.to_datetime(df2['day_raw'])
	del df2['day_raw']
	del df2['datetime']

	#Merge tracks on date day to obtain sunrise and sunset times for the track segment
	joinTo = df2
	joinFrom = time
	merge = pd.merge(joinTo, joinFrom, left_on = 'day', right_on = 'day')

	#Set merge to a value
	merge['during_day'] = 0

	#Create a column that is true if track segment was during the night
	current_time = merge['datetime2']
	sunrise = merge['datetime_sunrise']
	sunset = merge['datetime_sunset']
	merge['during_day'] = (sunset >= current_time) & (current_time >= sunrise)
	merge['night'] = merge['during_day'] != True

	#Select all day columns and calculate total meters during the day
	df3 = merge[(merge.night == True )]
	df3['length_night'] = df3['lengte'].sum()
	df4 = df3[['length_night', 'person']]
	df4 = df4.drop_duplicates(subset = ['person'])
	df4['person'] = df4['person'].astype(str)

	#Append a single line to the person file
	result= result.append(df4)
	
#Write results to a .csv	
result.to_csv('D:\\b-riders\Data\\night.csv', sep = ';', decimal = ',', index = False)
