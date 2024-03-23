#Question 1
import pandas as pd
myDF = pd.read_csv('/anvil/projects/tdm/data/whin/weather.csv')
myDF.head()
myDF['station_id'].value_counts()
myDF.groupby('station_id').size()



#Question 2
myDF.isnull()
myDF.isnull().sum()
myDF.isnull().sum().sum()
myDF_cleaned = myDF.dropna()
myDF_cleaned
myDF_cleaned.isnull().sum()



#Question 3
myDFcleaned = myDF.dropna(subset = ['temperature']).copy()
myDFcleaned.shape
myDF.shape
myDFcleaned.head()
myDFcleaned['location'] = myDFcleaned['latitude'].astype(str) + '_' +  myDFcleaned['longitude'].astype(str)
myDFcleaned.head()
myDFcleaned.groupby('location')['temperature'].mean()



#Question 4
def avg_temp_location(file_location) -> pd.Series: 
    """
    This function takes in a file location of the exact file that needs to be analyzed, and then creates a new dataframe where the temperature values are null. After that, 
    the function combines the latitude and longitude columns as a new column called 'location'. Finally, that new data column is grouped and then is paired with the 
    average temperature for each of the location, which is the series that will be returned. 
    
    Args:
    file_location - the exact location in anvil of the specific file to be analyzed

    
    Returns:
    A series that has all the new locations and the average temperatures for each of the locations
    """
    myDF = pd.read_csv(file_location)
    myDFcleaned = myDF.dropna(subset = ['temperature']).copy()
    myDFcleaned['location'] = myDFcleaned['latitude'].astype(str) + '_' +  myDFcleaned['longitude'].astype(str)
    return myDFcleaned.groupby('location')['temperature'].mean()

avg_temp_location('/anvil/projects/tdm/data/whin/weather.csv')



#Question 5
myDF['wind_gust_speed_mph'].value_counts()
myDFwindcleaned = myDF.dropna(subset = ['wind_gust_speed_mph']).copy()
myDF.shape
myDFwindcleaned.shape
myDFwindcleaned['location'] = myDFcleaned['latitude'].astype(str) + '_' +  myDFcleaned['longitude'].astype(str)
myDFwindcleaned.groupby('location')['wind_gust_speed_mph'].mean()

def avg_wind_speed_location(file_location) -> pd.Series: 
    """
    This function takes in a file location of the exact file that needs to be analyzed, and then creates a new dataframe where the temperature values are null. After that, 
    the function combines the latitude and longitude columns as a new column called 'location'. Finally, that new data column is grouped and then is paired with the 
    average wind gust speed for each of the location, which is the series that will be returned. 
    
    Args:
    file_location - the exact location in anvil of the specific file to be analyzed

    
    Returns:
    A series that has all the new locations and the average wind gust speed for each of the locations
    """
    myDF = pd.read_csv(file_location)
    myDFcleaned = myDF.dropna(subset = ['wind_gust_speed_mph']).copy()
    myDFcleaned['location'] = myDFcleaned['latitude'].astype(str) + '_' +  myDFcleaned['longitude'].astype(str)
    return myDFcleaned.groupby('location')['wind_gust_speed_mph'].mean()

avg_wind_speed_location('/anvil/projects/tdm/data/whin/weather.csv')