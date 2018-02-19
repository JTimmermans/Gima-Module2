import glob
import pandas as pd
import csv
import os




#concenate all B-rider tracks to one large file
path = 'C:\\Users\\Joris\\Google Drive\\Gima\Module_2\\Case_Study\\Data\\joinedtracks'
allFiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_)
    list_.append(df)
frame = pd.concat(list_)

frame.to_csv('C:\Users\Joris\Google Drive\Gima\Module_2\Case_Study\Data\complete\joris.csv', sep = ';')
print 'csv concenated/created'


