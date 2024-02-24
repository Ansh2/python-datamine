#Question 1 
import pandas as pd
from pathlib import Path
Path("/anvil/projects/tdm/data/noaa/1750.csv")
import os
len(os.listdir('/anvil/projects/tdm/data/noaa/'))
myfiles=[]
for year in range (1880, 1884):
    file= Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
    myfiles.append(file)
print(myfiles)
# the below uses list comprehension
myfiles=[Path(f'/anvil/projects/tdm/data/noaa/{year}.csv') for year in range (1880, 1884)]
print(myfiles)



#Question 2
# the below will calculate the amount of records for 1880
file = "/anvil/projects/tdm/data/noaa/1880.csv"
with open(file,"r") as f:
    mycount = 0
    for line in f:
        mycount += 1
print(f'There are {mycount} records in the file called {file}')
total_count = 0
for file in myfiles:
    with open(file,"r") as f:
        mycount = 0
        for line in f:
            total_count += 1
            mycount += 1
    print(f'There are {mycount} records in the file called {file}\n')
print(f'There are {total_count} records in the 4 files altogether.\n')



#Question 3
myDF = pd.read_csv(myfiles[0])
myDF.columns
myDF.head()
myDF.tail()
myDF = pd.read_csv(myfiles[0], header=None)
myDF.columns
myDF.head()
myDF.tail()
myfiles=[]
for year in range (1880, 1884):
    file= Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
    myfiles.append(file)
print(myfiles)
myfiles[0]
newDF = pd.read_csv(myfiles[0],names = ["id","date","element_code","value","mflag","qflag","sflag","obstime"])
newDF
mydataframes = []
for i in range(0,4):
    mydataframes.append(pd.read_csv(myfiles[i],names = ["id","date","element_code","value","mflag","qflag","sflag","obstime"]))
for i in range(0,4):
    print(mydataframes[i].shape)
for i in range(0,4):
    print(mydataframes[i].columns)

    

#Question 4
len(mydataframes)
for i in range(0,4):
    print(mydataframes[i]['element_code'].unique())
    print("\n")
# Number of unique elements in each of the four dadtaframes
for i in range(0,4):
    print(len(mydataframes[i]['element_code'].unique()))
# Number of times SNOW occurs in each of the four dataframes
for i in range(0,4):
    print(mydataframes[i]['element_code'].value_counts()['SNOW'])


    
#Question 5
import pandas as pd
from pathlib import Path
myfiles=[]
for year in range (1880, 1884):
    file= Path(f'/anvil/projects/tdm/data/noaa/{year}.csv')
    myfiles.append(file)
count = 0
for file in myfiles:
    for myDF in pd.read_csv(file,names=["id","date","element_code","value","mflag","qflag","sflag","obstime"],chunksize =10000):
        count += len(myDF[myDF['element_code'] == 'SNOW'])

print(count)
count = 0
for file in myfiles:
    for myDF in pd.read_csv(file,names=["id","date","element_code","value","mflag","qflag","sflag","obstime"],chunksize =10000):
        for index, row in myDF.iterrows():
            if row['element_code'] == 'SNOW':
                count += 1

print(count)