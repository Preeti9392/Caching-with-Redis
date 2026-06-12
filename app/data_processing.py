import pandas as pd

flights= pd.read_csv(r"..\data\flights.csv")
airlines= pd.read_csv(r"..\data\airlines.csv")
airports= pd.read_csv(r"..\data\airports.csv")

# print(flights.head(10))
# print(flights.isnull().sum())
# print(flights.dtypes)

data =pd.merge()
