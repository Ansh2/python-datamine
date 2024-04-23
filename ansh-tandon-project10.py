#Question 1
import pandas as pd
pd.set_option("display.max_column", None)
cols = [
    'DepDelay', 'ArrDelay', 'Distance',
    'CarrierDelay', 'WeatherDelay',
    'DepTime', 'ArrTime', 'Diverted', 'AirTime'
]

col_types = {
    'DepDelay': 'float64',
    'ArrDelay': 'float64',
    'Distance': 'float64',
    'CarrierDelay': 'float64',
    'WeatherDelay': 'float64',
    'DepTime': 'float64',
    'ArrTime': 'float64',
    'Diverted': 'int64',
    'AirTime': 'float64'
}

myDF = pd.read_csv("/anvil/projects/tdm/data/flights/2014.csv", usecols=cols, dtype=col_types)
myDF.head()




#Question 2
myDF.groupby('DepDelay')['DepDelay'].value_counts()

import numpy as np
my_depdelay_values = myDF['DepDelay'].to_numpy()
print("the shape of the numpy array is: ", my_depdelay_values.shape, "and the type is: ", my_depdelay_values.dtype)
my_cleaned_depdelay_values = np.nan_to_num(my_depdelay_values, nan=0)
my_larger_cleaned_depdelay_values = my_cleaned_depdelay_values + 15
print("The average Departure Delay before adding 15 minutes is: .......", np.mean(my_cleaned_depdelay_values))
print("The average Departure Delay after adding 15 minutes is: .......", np.mean(my_larger_cleaned_depdelay_values))



#Question 3
print("Max Arrival Delay: ...... minutes ", np.max(my_cleaned_depdelay_values))
print("Max Arrival Delay: ...... minutes ", np.min(my_cleaned_depdelay_values))



#Question 4
import time
start_time = time.time()

delayed_flights = myDF[(myDF['DepDelay'] > 60) | (myDF['ArrDelay'] > 60)]

my_average_delayed_flights = delayed_flights['Distance'].mean()

print(f"The average overall distances for the delayed flights is {my_average_delayed_flights}")

end_time = time.time()
print(f"Used time is {end_time - start_time}")




#Question 5
start_time = time.time()

mydeparray = myDF['DepDelay'].to_numpy()
myarrarray = myDF['ArrDelay'].to_numpy()
mydistancearray = myDF['Distance'].to_numpy()

my_filtered_average_distances = mydistancearray[(mydeparray > 60) | (myarrarray > 60)]

my_average_delayed_flights = np.mean(my_filtered_average_distances)

print(f"The average overall distances for the delayed flights is {my_average_delayed_flights}")

end_time = time.time()
print(f"Used time is {end_time - start_time}")