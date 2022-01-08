import pandas as pd

xlsx_path = "test.xlsx"
df = pd.read_excel(xlsx_path)
print(df.head(3))
print()
# print(df.loc[300:310, "deaths": "population"])
# print()
# print(df.iloc[300:311, 5:10])
# print()
print(df[["Countries", "deaths"]])
print(df["Countries"].unique())
df1 = df[df["deaths"] >= 3000]
print(df1)
print(df1[df1["cases"] > 30000])
