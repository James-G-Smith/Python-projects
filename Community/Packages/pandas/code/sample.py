import pandas as pd

#df = pd.read_excel("../data/data.xlsx")
df = pd.read_csv("../data/data.csv")

#df = pd.read_csv("../data/data.csv", sheet_name=None)

print(df.head())
print("\n")

#if Milestone = phase then print what's in PHASE
def first_word(x):
    return x.split()[0]

def concat(row):
    return str(row['Sentence'] + " - " + row['Positive/Negative'])

#apply our function using 1 variable
df['first word'] = df['Sentence'].apply(first_word)

#apply our function using 2 variables
df['Concat'] = df.apply(concat,axis=1)

#forward fill (fills the blanks below the phase)
df['Confidence'] = df['Confidence'].ffill()

print(df)

#take a subtable
print(df.iloc[0:1,2:3])
print(df.iloc[3:,1:3])

# drop the rows in Sentence with element "I do not enjoy my job"
df2 = df[df['Sentence'] != "I do not enjoy my job"]

#filter the df over a cell
df3 = df[df['Sentence'] == "I do not enjoy my job"]

print(df3.head())

df.to_excel("../data/data_transformed.xlsx")
df.to_csv("../data/data_transformed.csv")

columns = ["date","height","size"]

df1 = pd.DataFrame([["25/12/1988","1.89m","12s"],["26/12/1988","1.99m","13s"]],columns = columns)

df2 = pd.DataFrame([["25/12/1988","1.89m","12s"],["26/12/1988","1.99m","13s"]]).transpose()
columns = ["date","height"]
df2.columns = columns

print(df1)
print(df2)
    
    


