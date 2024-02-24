#Question 1
import pandas as pd
myyear = 1980
myfilepath = f'/anvil/projects/tdm/data/election/itcont{myyear}.txt'
mycolumnnames=["CMTE_ID","AMNDT_IND","RPT_TP","TRANSACTION_PGI","IMAGE_NUM","TRANSACTION_TP","ENTITY_TP","NAME","CITY","STATE","ZIP_CODE","EMPLOYER","OCCUPATION","TRANSACTION_DT","TRANSACTION_AMT","OTHER_ID","TRAN_ID","FILE_NUM","MEMO_CD","MEMO_TEXT","SUB_ID"]

mydictionarytypes = {"CMTE_ID": str, "AMNDT_IND": str, "RPT_TP": str, "TRANSACTION_PGI": str, "IMAGE_NUM": str, "TRANSACTION_TP": str, "ENTITY_TP": str, "NAME": str, "CITY": str, "STATE": str, "ZIP_CODE": str, "EMPLOYER": str, "OCCUPATION": str, "TRANSACTION_DT": str, "TRANSACTION_AMT": float, "OTHER_ID": str, "TRAN_ID": str, "FILE_NUM": str, "MEMO_CD": str, "MEMO_TEXT": str, "SUB_ID": int}

myDF = pd.read_csv(myfilepath, delimiter='|', names=mycolumnnames, dtype=mydictionarytypes)
myDF['TRANSACTION_DT'] = pd.to_datetime(myDF['TRANSACTION_DT'], format="%m%d%Y")
myDF['TRANSACTION_DT'][0:10]
myDF.head()

def read_election_year (myyear: int) -> pd.DataFrame:
    """
    This function accepts a 4-digit year as input, and returns a data frame that contains information about the donations to the federal election campaigns in that year
    
    Args:
    myyear (int): The is a 4-digit year for which we will load a data frame to be returned. 
    
    Returns:
    myDF (pd.DataFrame): This is the data frame that contains the information about the donations to the fedearl election campaigns. 
    """
    myfilepath = f'/anvil/projects/tdm/data/election/itcont{myyear}.txt'
    mycolumnnames=["CMTE_ID","AMNDT_IND","RPT_TP","TRANSACTION_PGI","IMAGE_NUM","TRANSACTION_TP","ENTITY_TP","NAME","CITY","STATE","ZIP_CODE","EMPLOYER","OCCUPATION","TRANSACTION_DT","TRANSACTION_AMT","OTHER_ID","TRAN_ID","FILE_NUM","MEMO_CD","MEMO_TEXT","SUB_ID"]
    mydictionarytypes = {"CMTE_ID": str, "AMNDT_IND": str, "RPT_TP": str, "TRANSACTION_PGI": str, "IMAGE_NUM": str, "TRANSACTION_TP": str, "ENTITY_TP": str, "NAME": str, "CITY": str, "STATE": str, "ZIP_CODE": str, "EMPLOYER": str, "OCCUPATION": str, "TRANSACTION_DT": str, "TRANSACTION_AMT": float, "OTHER_ID": str, "TRAN_ID": str, "FILE_NUM": str, "MEMO_CD": str, "MEMO_TEXT": str, "SUB_ID": int}
    myDF = pd.read_csv(myfilepath, delimiter='|', names=mycolumnnames, dtype=mydictionarytypes)
    myDF['TRANSACTION_DT'] = pd.to_datetime(myDF['TRANSACTION_DT'], format="%m%d%Y")
    return myDF

myDF = read_election_year(1988)
myDF.head()
myDF = read_election_year(1980)
myDF.head()
myDF = read_election_year(1984)
myDF.head()



#Question 2
myyear = 1980
myDF = read_election_year(myyear)
len(myDF['CMTE_ID'].unique())
myyear = 1984
myDF = read_election_year(myyear)
len(myDF['CMTE_ID'].unique())
myyear = 1988
myDF = read_election_year(myyear)
len(myDF['CMTE_ID'].unique())
def committees_function(myear: int) -> int:
    """
    This functions accepts a 4-digit year as input, and returns the number of (unique) CMTE_ID value for that year. 
    
    Args:
    myyear (int): This is a 4-digit year for which we will find the number of (unique) CMTE_ID values in that year. 
    
    Returns:
    myresult (int): This is the number of (unique) CMTE_ID value in the specified year. 
    """
    myDF = read_election_year(myear)
    myresult = len(myDF['CMTE_ID'].unique())
    return myresult
committees_function(1980)
committees_function(1984)
committees_function(1988)



#Question 3
myDF = read_election_year(1980)
myDF[myDF['STATE'] == "CA"]['TRANSACTION_AMT'].sum() # This amount is reasonable in 1980, and it is shown that California contributed over 24 million dollars
myDF.groupby('STATE')['TRANSACTION_AMT'].sum().sort_values() # The top 5 are the last 5
myDF.groupby('STATE')['TRANSACTION_AMT'].sum().sort_values().tail()
myDF = read_election_year(1984)
myDF[myDF['STATE'] == "CA"]['TRANSACTION_AMT'].sum() # This amount is reasonable in 1980, and it is shown that California contributed over 24 million dollars
myDF.groupby('STATE')['TRANSACTION_AMT'].sum().sort_values() # The top 5 are the last 5
myDF.groupby('STATE')['TRANSACTION_AMT'].sum().sort_values().tail()
myDF = read_election_year(1988)
myDF[myDF['STATE'] == "CA"]['TRANSACTION_AMT'].sum() # This amount is reasonable in 1980, and it is shown that California contributed over 24 million dollars
myDF.groupby('STATE')['TRANSACTION_AMT'].sum().sort_values().tail()
def top_five_states (myyear: int) -> pd.DataFrame:
    """
    This function accepts a 4-digit year as an input, and returns a data frame that contains information about transaction amount for the top 5 states.
    
    Args:
    myyear (int): This is a 4 digit year for which we will load a data frame to be returned.
    
    Returns:
    myDF (pd.DataFrame): This is the data frame that contains the information about the trasnaction amounts for the top 5 states.
    """
    myDF = read_election_year(myyear)
    myDF[myDF['STATE'] == "NY"]['TRANSACTION_AMT'].sum() 
    newDF = myDF.groupby('STATE')['TRANSACTION_AMT'].sum().sort_values().tail()
    return newDF
top_five_states(1980)
top_five_states(1984)
top_five_states(1988)



#Question 4
myDF = read_election_year(1980)
myDF.groupby('EMPLOYER')['TRANSACTION_AMT'].sum().sort_values().tail()
myDF = read_election_year(1984)
myDF.groupby('EMPLOYER')['TRANSACTION_AMT'].sum().sort_values().tail()
myDF = read_election_year(1988)
myDF.groupby('EMPLOYER')['TRANSACTION_AMT'].sum().sort_values().tail()
def top_employers(myyear: int) -> pd.DataFrame:
    """
    This function accepts a 4-digit year as an input, and returns a data frame that contains information about amount given to top 5 employers.
    
    Args:
    myyear (int): This is a 4 digit year for which we will load a data frame to be returned.
    
    Returns:
    myDF (pd.DataFrame): This is the data frame that contains the information about the amount of money given to top 5 employers
    """
    myDF = read_election_year(myyear)
    newDF = myDF.groupby('EMPLOYER')['TRANSACTION_AMT'].sum().sort_values().tail()
    return newDF
top_employers(1980)
top_employers(1984)
top_employers(1988)



#Question 5
myDF = read_election_year(1980)
myDF['TRANSACTION_AMT'][0:10]
myDF['TRANSACTION_AMT'].head()
myDF['TRANSACTION_AMT'].sum()
myDF.groupby('NAME')['TRANSACTION_AMT'].sum().sort_values().head()
myDF.groupby('NAME')['TRANSACTION_AMT'].sum().sort_values().tail()
myDF = read_election_year(1984)
myDF.groupby('NAME')['TRANSACTION_AMT'].sum().sort_values().tail()
myDF = read_election_year(1988)
myDF.groupby('NAME')['TRANSACTION_AMT'].sum().sort_values().tail()
def most_popular_names_or_organizations(myyear: int) -> pd.DataFrame:
    """
    This function accepts a 4-digit year as an input, and returns a data frame that contains information about the most popular names or organizations given how much they gave.
    
    Args:
    myyear (int): This is a 4 digit year for which we will load a data frame to be returned.
    
    Returns:
    myDF (pd.DataFrame): This is the data frame that contains the information about the most popular names or organizations given how much they gave.
    """
    myDF = read_election_year(myyear)
    newDF = myDF.groupby('NAME')['TRANSACTION_AMT'].sum().sort_values().tail()
    return newDF
most_popular_names_or_organizations(1980)
most_popular_names_or_organizations(1984)
most_popular_names_or_organizations(1988)