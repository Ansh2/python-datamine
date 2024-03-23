#Question 1
import pandas as pd
myDF = pd.read_parquet('/anvil/projects/tdm/data/whin/weather.parquet')
pd.set_option('display.max_columns', None)
myDF.head()
myDF['observation_time'] = pd.to_datetime(myDF['observation_time'])
myDF['year'] = myDF['observation_time'].dt.year
myDF.head()
myDF['month'] = myDF['observation_time'].dt.month
myDF['day'] = myDF['observation_time'].dt.day
myDF.head()
myDF['station_id'].value_counts()
my_station_id = 1
myDF[myDF['station_id'] == my_station_id].shape
myDF.shape
myDF[myDF['station_id'] == my_station_id].groupby(['year', 'month'])['temperature'].mean()
my_station_id = 4
myDF[myDF['station_id'] == my_station_id].groupby(['year', 'month'])['temperature'].mean()
my_stsation_id = 67
myDF[myDF['station_id'] == my_station_id].groupby(['year', 'month'])['temperature'].mean()

def get_avg_temp(my_station_id: int) -> pd.DataFrame:
    """
    This function accepts a integer id as input, and returns a data frame of the average temperatures for all of the years and months given that id.

    Args:
    my_station_id (int): This is a integer id for which we will load a data frame to be returned.

    Returns:
    myDF (pd.DataFrame): This is the data frame that contains all of the average temperatures for all of the years and months given that particular id.
    """
    myDF = pd.read_parquet('/anvil/projects/tdm/data/whin/weather.parquet')
    myDF['observation_time'] = pd.to_datetime(myDF['observation_time'])
    myDF['year'] = myDF['observation_time'].dt.year
    myDF['month'] = myDF['observation_time'].dt.month
    myDF['day'] = myDF['observation_time'].dt.day
    return myDF[myDF["station_id"] == my_station_id].groupby(["year", "month"])["temperature"].mean()

get_avg_temp(1)
get_avg_temp(4)
get_avg_temp(67)




#Question 2

import matplotlib.pyplot as plt
my_station_id = 1
myresults = myDF[myDF["station_id"] == my_station_id].groupby(["year", "month"])["temperature"].mean()
myresults.plot(kind = 'line')
myresults.unstack(0)

myresults.unstack(0).plot(kind = 'line', marker = 'o')
plt.title(f'Average monthly temperatures for given station_id and all month-and-year pairs')
plt.xlabel('Month')
plt.ylabel('Average temperatures')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend(title = 'Year')
plt.grid(True)
plt.show()

my_station_id = 4
myresults = myDF[myDF["station_id"] == my_station_id].groupby(["year", "month"])["temperature"].mean()
myresults.unstack(0).plot(kind = 'line', marker = 'o')
plt.title(f'Average monthly temperatures for given station_id and all month-and-year pairs')
plt.xlabel('Month')
plt.ylabel('Average temperatures')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend(title = 'Year')
plt.grid(True)
plt.show()

my_station_id = 67
myresults = myDF[myDF["station_id"] == my_station_id].groupby(["year", "month"])["temperature"].mean()
myresults.unstack(0).plot(kind = 'line', marker = 'o')
plt.title(f'Average monthly temperatures for given station_id and all month-and-year pairs')
plt.xlabel('Month')
plt.ylabel('Average temperatures')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend(title = 'Year')
plt.grid(True)
plt.show()


def plot_avg_temps(my_station_id: int):
    """
    This function accepts a integer id as input, and plots a graph of the average monthly temperatures for the given id and the according month-and-year pairs.

    Args:
    my_station_id (int): This is a integer id for which we will graph using matplotlib

    Returns:
    This function does not have any specified return value.
    """
    myresults = myDF[myDF["station_id"] == my_station_id].groupby(["year", "month"])["temperature"].mean()
    myresults.unstack(0).plot(kind = 'line', marker = 'o')
    plt.title(f'Average monthly temperatures for given station_id and all month-and-year pairs')
    plt.xlabel('Month')
    plt.ylabel('Average temperatures')
    plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.legend(title = 'Year')
    plt.grid(True)
    plt.show()
    

plot_avg_temps(1)
plot_avg_temps(4)
plot_avg_temps(67)




#Question 3

my_station_id = 1
myDF[myDF['station_id'] == my_station_id].groupby(['year', 'month'])['temperature'].max()
my_station_id = 4
myDF[myDF['station_id'] == my_station_id].groupby(['year', 'month'])['temperature'].max()
my_station_id = 67
myDF[myDF['station_id'] == my_station_id].groupby(['year', 'month'])['temperature'].max()

def get_max_temp(my_station_id: int) -> pd.DataFrame:
    """
    This function accepts a integer id as input, and returns a data frame of the max temperatures for all of the years and months pairs given that id.

    Args:
    my_station_id (int): This is a integer id for which we will load a data frame to be returned.

    Returns:
    myDF (pd.DataFrame): This is the data frame that contains all of the max temperatures for all of the years and months pairs given that particular id.
    """
    myDF = pd.read_parquet('/anvil/projects/tdm/data/whin/weather.parquet')
    myDF['observation_time'] = pd.to_datetime(myDF['observation_time'])
    myDF['year'] = myDF['observation_time'].dt.year
    myDF['month'] = myDF['observation_time'].dt.month
    myDF['day'] = myDF['observation_time'].dt.day
    return myDF[myDF['station_id'] == my_station_id].groupby(['year', 'month'])['temperature'].max()


get_max_temp(1)
get_max_temp(4)
get_max_temp(67)

def plot_max_temps(my_station_id: int):
    """
    This function accepts a integer id as input, and plots a graph of the max monthly temperatures for the given id and the according month-and-year pairs.

    Args:
    my_station_id (int): This is a integer id for which we will graph using matplotlib

    Returns:
    This function does not have any specified return value.
    """
    myresults = myDF[myDF["station_id"] == my_station_id].groupby(["year", "month"])["temperature"].max()
    myresults.unstack(0).plot(kind = 'bar')
    plt.title(f'Maxium monthly temperatures for given station_id and all month-and-year pairs')
    plt.xlabel('Month')
    plt.ylabel('Maximum temperatures')
    plt.xticks(range(0, 12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.legend(title = 'Year')
    plt.grid(True)
    plt.show()

plot_max_temps(1)
plot_max_temps(4)
plot_max_temps(67)




#Question 4

my_station_id = 1
myyear = 2020

myresults = myDF[myDF["station_id"] == my_station_id & (myDF['year'] == myyear)]

myresults.shape
myresults.boxplot(column = 'wind_speed_mph', by = 'month')
plt.title(f'Monthly wind speeds at station {my_station_id} and {myyear}')
plt.xlabel('Month')
plt.ylabel('Wind Speed (in mph)')
plt.show()

def plot_monthly_wind_speeds(my_station_id: int, myyear: int):
    """
    This function accepts a integer id as input and a year as an integer, and plots a graph the monthly wind speeds at a particular station and year.

    Args:
    my_station_id (int): This is a integer id for which we will graph using matplotlib
    myyear (int): This is an integer value of the yedar for which we will plot the data for 

    Returns:
    This function does not have any specified return value.
    """
    myresults = myDF[myDF["station_id"] == my_station_id & (myDF['year'] == myyear)]
    myresults.boxplot(column = 'wind_speed_mph', by = 'month')
    plt.title(f'Monthly wind speeds at station {my_station_id} and {myyear}')
    plt.xlabel('Month')
    plt.ylabel('Wind Speed (in mph)')
    plt.show()

plot_monthly_wind_speeds(1, 2020)
plot_monthly_wind_speeds(3, 2019)
plot_monthly_wind_speeds(1, 2019)




#Question 5

myDF = pd.read_parquet('/anvil/projects/tdm/data/whin/weather.parquet')
myDF.head()

pd.set_option('display.max_columns', None)
myDF['observation_time'] = pd.to_datetime(myDF['observation_time'])
myDF['year'] = myDF['observation_time'].dt.year
myDF['month'] = myDF['observation_time'].dt.month
myDF['day'] = myDF['observation_time'].dt.day

# Will now do some analysis on the max pressure for a given year and month given a particular station id
# average monthly pressures for the given id and the according month-and-year pairs.
my_station_id = 1
myresults = myDF[myDF['station_id'] == my_station_id].groupby(['year', 'month'])['pressure'].mean()

myresults.unstack(0).plot(kind = 'line', marker = 'o')
plt.title(f'Average monthly pressure for given station_id and all month-and-year pairs')
plt.xlabel('Month')
plt.ylabel('Average pressure')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])  
plt.legend(title = 'Year')
plt.grid(True)
plt.show()


my_station_id = 4
myresults = myDF[myDF['station_id'] == my_station_id].groupby(['year', 'month'])['pressure'].mean()
myresults.unstack(0).plot(kind = 'line', marker = 'o')
plt.title(f'Average monthly pressure for given station_id and all month-and-year pairs')
plt.xlabel('Month')
plt.ylabel('Average pressure')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])  
plt.legend(title = 'Year')
plt.grid(True)
plt.show()


def plot_avg_pressure(my_station_id: int):
    """
    This function accepts a integer id as input, and plots a graph of the average pressure temperatures for the given id based on month-and-year pairs.

    Args:
    my_station_id (int): This is a integer id for which we will graph using matplotlib

    Returns:
    This function does not have any specified return value.
    """
    myresults = myDF[myDF['station_id'] == my_station_id].groupby(['year', 'month'])['pressure'].mean()
    myresults.unstack(0).plot(kind = 'line', marker = 'o')
    plt.title(f'Average monthly pressure for given station_id and all month-and-year pairs')
    plt.xlabel('Month')
    plt.ylabel('Average pressure')
    plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])  
    plt.legend(title = 'Year')
    plt.grid(True)
    plt.show()
    
plot_avg_pressure(1)
plot_avg_pressure(4)