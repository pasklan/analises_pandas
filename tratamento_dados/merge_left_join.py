# exemplo que retorna todos os dados da tabela da esquerda e as correspondências da tabela da direita 
import pandas as pd

# carregamento dos arquivos
vendedores_DF = pd.read_excel("C:\\RPA\\Scripts\\ExcelTest\\Vendedores_LEFT_JOIN.xlsx")
vendas_DF = pd.read_excel("C:\\RPA\\Scripts\\ExcelTest\\Vendas_LEFT_JOIN.xlsx")


# Cria um novo DataFrame com a junção de todos os dados da tabela 'Vendas' mais os vendedores cujos IDs \
# existam na tabela 'Vendedores'
vendas_left_join_vendedores_DF = pd.merge(vendas_DF, vendedores_DF, on=["Id Vendedor"], how="left", suffixes=(" Vendas", " Check"))
#display(vendas_left_join_vendedores_DF)

# limpando o DF
linhas_sem_NAN = vendas_left_join_vendedores_DF.dropna()
display(linhas_sem_NAN)

# deleta a coluna Vendedor Check
del linhas_sem_NAN["Vendedor Check"]
display(linhas_sem_NAN)
