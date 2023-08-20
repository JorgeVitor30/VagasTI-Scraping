import pandas as pd


arquivos = ["DataScienceBD.xlsx", "DevBD.xlsx", "JavaBD.xlsx", "SoftwareBD.xlsx","JS.xlsx", "PHP.xlsx", "SQL.xlsx", "Swift.xlsx", "Ruby.xlsx"]


dataframes = []


for arquivo in arquivos:
    df = pd.read_excel(arquivo)
    dataframes.append(df)

df_final = pd.concat(dataframes, ignore_index=True)


df_final.to_excel("LangsBD.xlsx", index=False)


