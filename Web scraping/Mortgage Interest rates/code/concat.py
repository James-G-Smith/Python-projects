import pandas as pd
from glob import glob

#define the path variable
path="..\\data\\"

#open a list with all file names in that directory that have the following extension
files = glob(path + "*.csv")

#open an empty list
dfs = []

def splity(x):

    return x.split("% ")[0]
#loop through all file names
for file in files:
    
    df = pd.read_csv(file, encoding = "ISO-8859-1")
    
    #create a new column and populat with the date
    file_name = file.split("_")[-1].split(".")[0]
    df["date"] = file_name
    
    df = df.rename(columns={'Initial interest rate*': 'Initial interest rate','Booking fee*': 'Booking fee'})
    
    df["Initial interest rate"] = df["Initial interest rate"].apply(splity)
    
    df["Booking fee"] = df["Booking fee"].str[3:]

    # add each df to the list
    dfs.append(df)

#create a new df from all the sub dfs    
df = pd.concat(dfs)

#write this new df to a excel file
df.to_csv("..\\Interest_rates_concat.csv")
