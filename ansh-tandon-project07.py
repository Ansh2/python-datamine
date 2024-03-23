#Question 1
import pandas as pd
myyear = 1880
myDF = pd.read_csv(f'/anvil/projects/tdm/data/noaa/{myyear}.csv', header=None, names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
myDF.shape
us_records = myDF[myDF['id'].str.startswith('US')]
us_records.shape
us_records.head()
myyear = 1881
myDF = pd.read_csv(f'/anvil/projects/tdm/data/noaa/{myyear}.csv', names=["id","date","element_code","value","mflag","qflag","sflag","obstime"], header=None)
us_records = myDF[myDF['id'].str.startswith('US')]
us_records.shape
myyear = 1882
myDF = pd.read_csv(f'/anvil/projects/tdm/data/noaa/{myyear}.csv', names=["id","date","element_code","value","mflag","qflag","sflag","obstime"], header=None)
us_records = myDF[myDF['id'].str.startswith('US')]
us_records.shape
myyear = 1883
myDF = pd.read_csv(f'/anvil/projects/tdm/data/noaa/{myyear}.csv', names=["id","date","element_code","value","mflag","qflag","sflag","obstime"], header=None)
us_records = myDF[myDF['id'].str.startswith('US')]
us_records.shape

def get_noaa_data (myyear: int) -> pd.DataFrame:
    """
    This function accepts a 4-digit year as input, and returns a data frame that contains the NOAA data for that year

    Args:
    myyear (int): This is a 4-digit year for which we will load a data frame to be returned.

    Returns:
    myDF (pd.DataFrame): This is the data frame that contains the NOAA data for that year
    """
    myfilepath = f'/anvil/projects/tdm/data/noaa/{myyear}.csv'
    mycolumnnames=["id","date","element_code","value","mflag","qflag","sflag","obstime"]
    myDF = pd.read_csv(myfilepath, names=mycolumnnames)
    myDF['date'] = pd.to_datetime(myDF['date'], format="%Y%m%d")
    return myDF

get_noaa_data(1880)

get_noaa_data(1880).shape[0]

newDF = get_noaa_data(1880)
newDF[newDF['id'].str.startswith('US')].shape
newDF = get_noaa_data(1881)
newDF[newDF['id'].str.startswith('US')].shape
newDF = get_noaa_data(1882)
newDF[newDF['id'].str.startswith('US')].shape
newDF = get_noaa_data(1883)
newDF[newDF['id'].str.startswith('US')].shape

mydict = {}
mylist = list(range(1880, 1884))
for myyear in mylist:
    newDF = get_noaa_data(myyear)
    mydict.update({myyear: newDF[newDF['id'].str.startswith('US')].shape[0]})

mydict

def get_dict_us_sizes (mylist: int) -> dict:
    """
    This function accepts a list of 4-digit years as input, and returns a dictionary that contains the NOAA data for each of the years.

    Args:
    mylist (int): This is a list of 4-digit years for which we will load a dictionary to be returned.

    Returns:
    mydict (dict): This is the dictionary that contains the NOAA data for each of the years provided
    """
    mydict = {}
    for myyear in mylist:
        newDF = get_noaa_data(myyear)
        mydict.update({myyear: newDF[newDF['id'].str.startswith('US')].shape[0]})
    return mydict

get_dict_us_sizes(list(range(1880, 1884)))
    
    
    
#Question 2
mydict
mydescendingdict = dict([key, mydict[key]] for key in sorted(mydict, key=mydict.get, reverse=True))
mydescendingdict
def get_dict_us_sizes_reverse (mylist: int) -> dict:
    """
    This function accepts a list of 4-digit years as input, and returns a dictionary in reverse order that contains the NOAA data for USA for each of the years.

    Args:
    mylist (int): This is a list of 4-digit years for which we will load a dictionary to be returned.

    Returns:
    mydescendingdict (dict): This is the dictionary that contains the NOAA data for USA for each of the years provided in reverse order.
    """
    mydict = {}
    for myyear in mylist:
        newDF = get_noaa_data(myyear)
        mydict.update({myyear: newDF[newDF['id'].str.startswith('US')].shape[0]})
    mydescendingdict = dict([key, mydict[key]] for key in sorted(mydict, key=mydict.get, reverse=True))
    return mydescendingdict

get_dict_us_sizes_reverse(list(range(1880, 1884)))


#Question 3
newDF = get_noaa_data(1880)
newDF[ (newDF['id'].str.startswith('US')) & (newDF['element_code'] == "SNOW") & (newDF['value'] > 0) ].shape
newDF = get_noaa_data(1881)
newDF[ (newDF['id'].str.startswith('US')) & (newDF['element_code'] == "SNOW") & (newDF['value'] > 0) ].shape
newDF = get_noaa_data(1882)
newDF[ (newDF['id'].str.startswith('US')) & (newDF['element_code'] == "SNOW") & (newDF['value'] > 0) ].shape
newDF = get_noaa_data(1883)
newDF[ (newDF['id'].str.startswith('US')) & (newDF['element_code'] == "SNOW") & (newDF['value'] > 0) ].shape
mydict = {}
mylist = list(range(1880, 1884))
for myyear in mylist:
    newDF = get_noaa_data(myyear)
    mydict.update({myyear: newDF[ (newDF['id'].str.startswith('US')) & (newDF['element_code'] == "SNOW") & (newDF['value'] > 0) ].shape[0]})
mydict

def get_dict_us_sizes_snow_days (mylist: int) -> dict:
    """
    This function accepts a list of 4-digit years as input, and returns a dictionary that contains the NOAA data for USA for each of the years with positive snowfall.

    Args:
    mylist (int): This is a list of 4-digit years for which we will load a dictionary to be returned.

    Returns:
    mydict (dict): This is the dictionary that contains the NOAA data for USA for each of the years provided with positive snowfall.
    """
    mydict = {}
    for myyear in mylist:
        newDF = get_noaa_data(myyear)
        mydict.update({myyear: newDF[ (newDF['id'].str.startswith('US')) & (newDF['element_code'] == "SNOW") & (newDF['value'] > 0) ].shape[0]})
    return mydict

get_dict_us_sizes_snow_days(list(range(1880,1884)))


    
#Question 4
newDF = get_noaa_data(1880)
snowyDF = newDF[ (newDF['id'].str.startswith('US')) & (newDF['element_code'] == "SNOW") & (newDF['value'] > 0) ]
snowyDF.shape
snowyDF.groupby('id').size()
snowyDF.groupby('id').size().idxmax()
snowyDF.groupby('id').size().max()
newDF = get_noaa_data(1881)
snowyDF = newDF[ (newDF['id'].str.startswith('US')) & (newDF['element_code'] == "SNOW") & (newDF['value'] > 0) ]
snowyDF.groupby('id').size()
snowyDF.groupby('id').size().idxmax()
newDF = get_noaa_data(1882)
snowyDF = newDF[ (newDF['id'].str.startswith('US')) & (newDF['element_code'] == "SNOW") & (newDF['value'] > 0) ]
snowyDF.groupby('id').size()
snowyDF.groupby('id').size().idxmax()
newDF = get_noaa_data(1883)
snowyDF = newDF[ (newDF['id'].str.startswith('US')) & (newDF['element_code'] == "SNOW") & (newDF['value'] > 0) ]
snowyDF.groupby('id').size()
snowyDF.groupby('id').size().idxmax()

mydict = {}
mylist = list(range(1880, 1884))
for myyear in mylist:
    newDF = get_noaa_data(myyear)
    snowyDF = newDF[ (newDF['id'].str.startswith('US')) & (newDF['element_code'] == "SNOW") & (newDF['value'] > 0) ]
    mydict.update({myyear: snowyDF.groupby('id').size().idxmax()})
    
mydict

def get_dict_us_sizes_largest_snowfall (mylist: int) -> dict:
    """
    This function accepts a list of 4-digit years as input, and returns a dictionary that contains the NOAA data for USA for each year's largest positive snowfall.

    Args:
    mylist (int): This is a list of 4-digit years for which we will load a dictionary to be returned.

    Returns:
    mydict (dict): This is the dictionary that contains the NOAA data for USA for each year's largest positive snowfall.
    """
    mydict = {}
    for myyear in mylist:
        newDF = get_noaa_data(myyear)
        snowyDF = newDF[ (newDF['id'].str.startswith('US')) & (newDF['element_code'] == "SNOW") & (newDF['value'] > 0) ]
        mydict.update({myyear: snowyDF.groupby('id').size().idxmax()})
    return mydict

get_dict_us_sizes_largest_snowfall(list(range(1880, 1884)))



#Question 5
newDF = get_noaa_data(1880)
snowyDF = newDF[ (newDF['id'].str.startswith('US')) & (newDF['element_code'] == "SNOW") & (newDF['value'] > 0) ]
snowyDF.groupby('id')['value'].sum().idxmax()
newDF = get_noaa_data(1881)
snowyDF = newDF[ (newDF['id'].str.startswith('US')) & (newDF['element_code'] == "SNOW") & (newDF['value'] > 0) ]
snowyDF.groupby('id')['value'].sum().idxmax()
newDF = get_noaa_data(1882)
snowyDF = newDF[ (newDF['id'].str.startswith('US')) & (newDF['element_code'] == "SNOW") & (newDF['value'] > 0) ]
snowyDF.groupby('id')['value'].sum().idxmax()
newDF = get_noaa_data(1883)
snowyDF = newDF[ (newDF['id'].str.startswith('US')) & (newDF['element_code'] == "SNOW") & (newDF['value'] > 0) ]
snowyDF.groupby('id')['value'].sum().idxmax()

mydict = {}
mylist = list(range(1880, 1884))
for myyear in mylist:
    newDF = get_noaa_data(myyear)
    snowyDF = newDF[ (newDF['id'].str.startswith('US')) & (newDF['element_code'] == "SNOW") & (newDF['value'] > 0) ]
    mydict.update({myyear: snowyDF.groupby('id')['value'].sum().idxmax()})
    
mydict

def get_dict_us_sizes_largest_snowfall (mylist: int) -> dict:
    """
    This function accepts a list of 4-digit years as input, and returns a dictionary that contains the NOAA data for USA based on
    the sum of the values of largest snowfall for each of the years and the id that achieves the highest.

    Args:
    mylist (int): This is a list of 4-digit years for which we will load a dictionary to be returned.

    Returns:
    mydict (dict): This is the dictionary that contains the NOAA data for USA based on
    the sum of the values of largest snowfall for each of the years and the id that achieves the highest.
    """
    mydict = {}
    for myyear in mylist:
        newDF = get_noaa_data(myyear)
        snowyDF = newDF[ (newDF['id'].str.startswith('US')) & (newDF['element_code'] == "SNOW") & (newDF['value'] > 0) ]
        mydict.update({myyear: snowyDF.groupby('id')['value'].sum().idxmax()})
    return mydict

get_dict_us_sizes_largest_snowfall(list(range(1880, 1884)))

