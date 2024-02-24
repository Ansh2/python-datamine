#Question 1
import pandas as pd
myDF = pd.read_csv("/anvil/projects/tdm/data/noaa/1880.csv" , header=None, names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
myDF
myDF[(myDF['date'] >= 18800701) & (myDF['date'] <= 18800731)].shape
myDF.shape

def avg_aggreg_temp(file_location, column_title_list, start_date, end_date, my_element_code = "TAVG"):
    """
    arguments:
    file_location - the exact location in anvil of the specific file to be analyzed
    column_title_list - the names of the columns of the dataset
    start_date - the beginning date to use to analysis
    end_date - the last date to use for analysis
    my_element_code - the type of data (this limits the amount of rows in the data) to be considered in the analysis
    
    returns:
    A float that is the average values of the rows from the start_date to the end_date based upon the element_code parameter passed in
    """
    myDF = pd.read_csv(file_location, header=None, names=column_title_list)
    my_result = myDF[(myDF['date'] >= start_date) & (myDF['date'] <= end_date) & (myDF['element_code'] == my_element_code)]['value'].mean()
    return my_result

avg_aggreg_temp('/anvil/projects/tdm/data/noaa/2018.csv', ["id","date","element_code","value","mflag","qflag","sflag","obstime"], 20180101, 20180115, "TAVG")


#Question 2
column_title_list =  ["id","date","element_code","value","mflag","qflag","sflag","obstime"]
myyear = 1880
file_location = f'/anvil/projects/tdm/data/noaa/{myyear}.csv'
my_element_code = 'PCRP'
myresult = myDF[(myDF['element_code'] == my_element_code)]['value'].mean()

def avg_aggreg_temp_by_year(range_of_years, column_title_list, my_element_code = "TAVG") -> float:
    """
    arguments:
    range_of_years - the total amount of years that is inclusive
    column_title_list - the names of the columns of the dataset
    my_element_code  - the type of data (this limits the amount of rows in the data) to be considered in the analysis

    returns:
    a dictionary with one floating point value for each year with the average of the values for the rows corresponding to the chosen elements based on the element_code provided as well
    """
    
    mydict = {}
    for myyear in range_of_years:
        file_location = f'/anvil/projects/tdm/data/noaa/{myyear}.csv'
        myDF = pd.read_csv(file_location, header=None, names=column_title_list)
        myresult = myDF[(myDF['element_code'] == my_element_code)]['value'].mean()
        mydict[myyear] = myresult
    return mydict

avg_aggreg_temp_by_year(range(1880,1884), ["id","date","element_code","value","mflag","qflag","sflag","obstime"], "TAVG")


#Question 3

def avg_aggreg_temp_by_year_and_month(range_of_years, mymonth, column_title_list, my_element_code = "TAVG") -> float:
    """
    arguments:
    range_of_years - a list that contains the years of the data we want to analyze
    mymonth - the only month in the range we want to analyze
    column_title_list - the names of the columns of the dataset
    my_element_code  - the type of data (this limits the amount of rows in the data) to be considered in the analysis

    returns:
    a dictionary with one floating point value for each year with the average of the values for the rows corresponding to the chosen elements based on the element_code provided and a specific month
    """
    
    mydict = {}
    for myyear in range_of_years:
        file_location = f'/anvil/projects/tdm/data/noaa/{myyear}.csv'
        myDF = pd.read_csv(file_location, header=None, names=column_title_list)
        myDF['month'] = pd.to_datetime(myDF['date'], format='%Y%m%d').dt.month
        myresult = myDF[(myDF['element_code'] == my_element_code) & (myDF['month'] == mymonth)]['value'].mean()
        mydict[myyear] = myresult
    return mydict

avg_aggreg_temp_by_year_and_month(range(1880,1884), 7,  ["id","date","element_code","value","mflag","qflag","sflag","obstime"], "TAVG")


#Question 4

def most_qflags(range_of_years, column_title_list, my_qflag) -> dict:
    """
    arguments:
    range_of_years - a list that contains the years of the data we want to analyze
    column_title_list - the names of the columns of the dataset
    my_qflag - the specified type of the qflag based on the paramter passed to the function

    
    returns:
    a dictionary with the list of each of the years in the range provided for the rows corresponding to elements that have the same qflag as provided in the function parameters
    """
    myqflagdict = {}
    for myyear in range_of_years:
        file_location = f'/anvil/projects/tdm/data/noaa/{myyear}.csv'
        myDF = pd.read_csv(file_location, header=None, names=column_title_list)
        qflag = myDF[(myDF['qflag'] == my_qflag)].shape[0]
        mycount = myDF[(myDF['qflag'] == my_qflag)]['value'].count()
        myqflagdict[myyear] = qflag
    return myqflagdict

most_qflags(range(1880, 1884), ["id","date","element_code","value","mflag","qflag","sflag","obstime"], "I") # This gets the years from 1880 to 1883
most_qflags(range(1880, 1884), ["id","date","element_code","value","mflag","qflag","sflag","obstime"], "D") # This gets the years from 1880 to 1883
most_qflags(range(1880, 1884), ["id","date","element_code","value","mflag","qflag","sflag","obstime"], "X") # This gets the years from 1880 to 1883


#Question 5
myDF = pd.read_csv("/anvil/projects/tdm/data/noaa/2022.csv" , header=None, names=["id","date","element_code","value","mflag","qflag","sflag","obstime"])
myDF

def min_temp_for_years(range_of_years, column_title_list) -> float:
    """
    arguments:
    range_of_years - a list that contains the years of the data we want to analyze
    column_title_list - the names of the columns of the dataset

    returns:
    a dictionary with one floating point value for each year with the minimum temperature values
    """
    
    mydict = {}
    for myyear in range_of_years:
        file_location = f'/anvil/projects/tdm/data/noaa/{myyear}.csv'
        myDF = pd.read_csv(file_location, header=None, names=column_title_list)
        myresult = myDF['value'].min()
        mydict[myyear] = myresult
    return mydict

min_temp_for_years(range(2018, 2022), ["id","date","element_code","value","mflag","qflag","sflag","obstime"])