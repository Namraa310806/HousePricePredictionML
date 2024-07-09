import pandas as pd

# Try with 'latin1' encoding
#housing = pd.read_csv("data.csv", encoding='latin1')
#print(housing.head())

# If 'latin1' does not work, try 'iso-8859-1'
#housing = pd.read_csv("data.csv", encoding='iso-8859-1')
#print(housing.head())

# If 'iso-8859-1' does not work, try 'cp1252'
housing = pd.read_csv("data.csv", encoding='cp1252')
print(housing.head())
