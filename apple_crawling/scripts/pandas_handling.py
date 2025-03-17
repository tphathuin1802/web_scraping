import csv

import pandas as pd

path = (
    "C:/Users/phath/OneDrive/DevProjects/DataScience/Crawling/apple_crawling/mac.json"
)

df = pd.read_json(path)
df = pd.DataFrame(df)
print(df)


df.to_csv(
    "data.csv",
    index=False,
    encoding="utf-8",
    sep=",",
    header=True,
    mode="w",
)
