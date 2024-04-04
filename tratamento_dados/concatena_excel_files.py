# Mescla vários arquivos Excel em um único DataFrame
import pandas as pd

# Lendo os arquivos do trimestre
fileVendasJan_DF = pd.read_excel("C:\\RPA\\scripts\\ExcelTest\\Vendas_Jan.xlsx")
fileVendasFev_DF = pd.read_excel("C:\\RPA\\scripts\\ExcelTest\\Vendas_Fev.xlsx")
fileVendasMar_DF = pd.read_excel("C:\\RPA\\scripts\\ExcelTest\\Vendas_Mar.xlsx")


# unindo Jan e Fev
# também pode-se usar o .append() para unir 2 DataFrames:
# fileVendasJan_DF = fileVendasJan_DF.append(fileVendasFev_DF)

# Unindo os 3 arquivos em um único DF
quarterFile_DF = pd.concat([fileVendasJan_DF, fileVendasFev_DF, fileVendasMar_DF])


# novo DF apenas com as colunas especificadas
resume_quarter_DF = quarterFile_DF[["Vendedor", "Data Venda", "Total Vendas"]]
display(resume_quarter_DF)


# criando novo DF agora de maneira agrupada, 'keys' permite criar grupos:
grouped_quaerteFile_DF = pd.concat([fileVendasJan_DF, fileVendasFev_DF, fileVendasMar_DF], keys=["Janeiro", "Fevereiro", "Março"])
display(grouped_quaerteFile_DF)

# para separar um mês específico do DF agrupado, usa-se 'loc':
extracted_Feb_DF = grouped_quaerteFile_DF.loc["Fevereiro"]
display(extracted_Feb_DF)
