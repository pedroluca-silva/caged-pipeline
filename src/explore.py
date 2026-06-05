import pandas as pd

df = pd.read_csv("data/raw/CAGEDMOV202301.txt",
                 sep=";",
                 encoding="utf-8")

print("shape:", df.shape)
print("\nColunas:\n", df.columns.tolist())
print("\nTipos:\n", df.dtypes)
print("\nNulos:\n", df.isnull().sum())
print("\nPrimeiras linhas:\n", df.head())