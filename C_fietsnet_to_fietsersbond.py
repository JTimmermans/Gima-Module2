# Created by Joris Timmermans | Contact info: Joris.timmermans@outlook.com
#!!! Note to self: This one is a mess, tidy up for final report
import pandas as pd
import geopandas as gpd
import sys


def join_shapefiles(shapefile1, key_column1,key_column1_2, shapefile2, key_column2, key_column2_2, output_loc_name):
	'''Function to join two shapefiles w/o arcpy.
	The result is exported as an shapefile (.shp) and a comma delimted file (.csv). 
	Necesarry modules are 'pandas as pd' and 'geopandas as gpd

	Parameter shapefile1 is the data which is the main file(join_to), full path required.
	Parameter key_column1 requires the name of the column that functions as a common identifier in shapefile1.
	Parameter shapefile2 is the data which is the new file (join_from), full path required.
	Parameter key_column2 requires the name of column that functions as a common identifier in shapefile2.
	Parameter output_loc_name is the output path and filename, do not add an extensions (e.g. .csv/.shp)
	Necesarry modules are 'pandas as pd' and 'geopandas as gpd and 'sys'.
	'''

	# Load variables
	try:
		shp1 = pd.read_table(shapefile1, sep = ';')
		key1 = key_column1
		key1_2 = key_column1_2
		print str(shapefile1) + ' has been read.\n'
		shp1[str(key1)] = shp1[str(key1)].astype(str)
		shp1[str(key1_2)] = shp1[str(key1_2)].astype(str)
		print shp1.head()
	except:
		print 'Shapefile1 or key_column1 has not been read'

	
	shp2 = gpd.read_file(shapefile2)
	key2 = key_column2
	key2_2 = key_column2_2
	print str(shapefile2) + ' has been read.\n'
	shp2[str(key2)] = shp2[str(key2)].astype(str)
	shp2[str(key2_2)] = shp2[str(key2_2)].astype(str)
	print shp2.head()
	
	print 'Shapefile2 or key_column2 has not been read'

	# Merge shapefiles
	try:
		shapefile_merge = pd.merge(shp1, shp2, how='left', left_on =[str(key1), str(key1_2)], right_on = [str(key2), str(key2_2)], suffixes=('y', ''))
		#shapefile_merge.geometry
		#Print example of data to verify join
		shapefile_merge['lengte'] = shapefile_merge['lengte'].astype('float64')
		print shapefile_merge.head()
		print '\n'
	except:
		print 'Merge has failed'

	# Export output as .csv and .shp
	try:
		shapefile_merge.to_csv(output_loc_name + '.csv', encoding='utf-8', sep = ';', decimal=',', index=False)
	
		print 'Exported as .csv'
	except:
		print 'Could not export as .csv'
	
	'''try:
		shapefile_merge.to_file(driver = 'ESRI Shapefile', filename = output_loc_name + '.shp')
		print 'Exported as .shp'
	except:
		print("Unexpected error:", sys.exc_info()[0])
    	raise'''

#test
input_1 = 'C:\Users\Joris\Google Drive\Gima\Module_2\Case_Study\Data\Simon\Export_output.txt'
column_1 = 'van_id'
column_1_2 = 'naar_id'
input_2 = 'C:\Users\Joris\Google Drive\Gima\Module_2\Case_Study\Data\Simon\\fietsnet.shp'
column_2 = 'SOURCE'
column_2_2 = 'TARGET'
outname = 'C:\Users\Joris\Google Drive\Gima\Module_2\Case_Study\Data\Simon\\fietsnet_linkscor'

help(join_shapefiles)
join_shapefiles(input_1, column_1, column_1_2, input_2, column_2, column_2_2, outname)
