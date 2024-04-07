import pandas as pd
import numpy as np

data = {
    "X" : [10, 15, 18, np.nan],
    "Y" : [34.67, np.nan, 22.21, 45.39],
    "Z" : [12, 56, np.nan, 44]
}

df = pd.DataFrame(data)

print(df)

df["X"] = df["X"].replace(np.nan, df["X"].mean())
df["Y"] = df["Y"].replace(np.nan, df["Y"].mean())
df["Z"] = df["Z"].replace(np.nan, df["Z"].mean())

print(df)