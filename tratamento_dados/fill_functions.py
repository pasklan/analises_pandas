# Algumas funções para tratar registros com valores faltantes
import pandas as pd

# carrega arquivo no DF
file_to_handle_DF = pd.read_excel("C:\\RPA\\scripts\\ExcelTest\\Tratamento_Dados.xlsx")

# cópias do mesmo DF para exemplificar
file_to_fillna_DF = file_to_handle_DF
file_to_ffill_DF = file_to_handle_DF

# alguns registros não possuem Total Vendas (NaN)
display(file_to_handle_DF)

# Preenche (usando fillna()) os valores vazios com a média  (.mean()) dos outros valores da coluna
# pode-se usar também valores fixos em '.fillna()', ex: .fillna(400)
file_to_fillna_DF["Total Vendas"] = file_to_handle_DF["Total Vendas"].fillna(file_to_handle_DF["Total Vendas"].mean())
display(file_to_fillna_DF)


# ffill - Preenche os valores faltantes com  último valor encontrado na coluna
file_to_ffill_DF["Total Vendas"] = file_to_ffill_DF["Total Vendas"].ffill()
display(file_to_ffill_DF)
