#Question 1 
mydata = [("Ansh Tandon", 18, "Computer Science"), 
          ("Robert Davis", 20, "Computer Engineering"), 
          ("John Doe", 18, "Data Science"), 
          ("Ethan Mehta", 17, "Artificial Intelligence"), 
          ("Alex Yang", 21, "Cybersecurity"), 
          ("Kevin Wang", 19, "Mechanical Engineering")]
import pandas as pd
studentDF = pd.DataFrame(mydata)
studentDF
print(studentDF.iloc[1, ])
print("Name: " + str(studentDF.iloc[1, 0]) + "\nAge: " + str(studentDF.iloc[1, 1]) + "\nMajor: " + str(studentDF.iloc[1, 2]))


#Question 2
myDF = pd.read_csv("/anvil/projects/tdm/data/craigslist/vehicles.csv")
myDF["id"] #will be using this as df index
myDF.head()
myDF.tail()


#Question 3
myDF.shape
myDF.shape[0] # number of rows
myDF.size
len(myDF.columns) # number of columns
myDF.columns


#Question 4
myDF[myDF["price"] > 6000].shape[0]
myDF["state"].unique()
myDF[myDF["state"] == "in"].shape[0]
myDF[myDF["state"] == "tx"].shape[0]
len(myDF["state"].unique())


#Question 5
subDF = myDF[myDF["price"] < 6000]
subDF.shape
newDF = subDF.groupby("state").size()
import matplotlib.pyplot as plt
plt.figure(figsize=(15, 8))
plt.xlabel("State")
plt.ylabel("Number of Vehicles")
plt.title("Number of Vehicles In States With Price Lower Than $6000")
newDF.plot(kind = "bar", figsize = (20,9))