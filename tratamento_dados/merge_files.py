# Exemplos de merges com 3 diferentes arquivos
import pandas as pd

# carregamento dos arquivos
DF_produtos = pd.read_excel("C:\\RPA\\scripts\\ExcelTest\\Produtos_Merge.xlsx")
DF_vendas = pd.read_excel("C:\\RPA\\scripts\\ExcelTest\\Vendas_Merge.xlsx")
DF_vendores = pd.read_excel("C:\\RPA\\scripts\\ExcelTest\\Vendedores_Merge.xlsx")


# exibindo os DF
# display(DF_produtos)
# display(DF_vendas)
# display(DF_vendores)

# merge - usando um identificadoe em comum dos 2 DataFrames para criar um novo DF
# merge equivale mais ou menos ao PROCV do Excel

# fazendo primeiro vendas com vendedores
DF_vendas = DF_vendas.merge(DF_vendores)

# fazendo com produto
DF_vendas = DF_vendas.merge(DF_produtos)

resumo_DF = DF_vendas[["Vendedor", "Produto", "Total Vendas"]]
display(resumo_DF)
