# captura itens que existam nas duas tabelas
import pandas as pd

# carregamento dos arquivos
file01_DF = pd.read_excel("C:\\RPA\\Scripts\\ExcelTest\\Vendas_+INNER_JOIN_Loja1.xlsx")
file02_DF = pd.read_excel("C:\\RPA\\Scripts\\ExcelTest\\Vendas_+INNER_JOIN_Loja2.xlsx")

# exibindo os dados
#display(file01_DF)
#display(file02_DF)


# criando um novo DataFrame como resultado do merge dos dois anteriores
# 'on' especifica qual coluna será utilizada como parâmetro de cruzamento
# 'how' especifica como será o merge, INNER especifica que somente dados que existirem nas duas tabelas serão retornados
vendedores_em_comum = pd.merge(file01_DF, file02_DF, on=["Vendedor"], how="inner")

# exibindo o novo DF
display(vendedores_em_comum)

# resumo dos dados, suffixes muda o nome padrão das colunas, ao invés de x/y será Loja1 e Loja2
vendedores_em_comum_resumo01 = pd.merge(file01_DF, file02_DF[["Vendedor", "Total Vendas"]], on=["Vendedor"], how="inner", suffixes=(" Loja 1", " Loja 2"))
display(vendedores_em_comum_resumo)

# resumo apenas dos totais dos vendedores
vendedores_em_comum_resumo02 = vendedores_em_comum_resumo01[["Vendedor", "Total Vendas Loja 1", "Total Vendas Loja 2"]]
display(vendedores_em_comum_resumo02)
