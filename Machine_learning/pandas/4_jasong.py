#ASSUMING A DATASET IS ALREADY PRESENT,
#THIS IS HOW WE READ/LOAD IT
import pandas as pd

#jason=JavaScript Object Notation.
df=pd.read_json("data.json")
print(df)