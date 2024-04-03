# Ordena as linhas de um DataFrame de acordo com a coluna desejada
import pandas as pd

# carrega arquivo no DF
file_to_order_DF = pd.read_excel("C:\\RPA\\scripts\\ExcelTest\\Ordenação.xlsx")

# ordena pela coluna 'Vendedor' de forma crescente (A -> Z)
ordenarVendedor = file_to_order_DF.sort_values(by="Vendedor")

# ordena pela coluna 'Vendedor' de forma decrescente (Z -> A), 'ascending' determina se será ascendente ou não,
# o padrão é ascendente
desc_ordenarVendedor = file_to_order_DF.sort_values(by="Vendedor", ascending=False)

# ordena pela coluna 'Produto' de forma crescente (A -> Z)
ordenarProduto = file_to_order_DF.sort_values(by="Produto")

# ordena pela coluna 'Data Venda' de forma crescente (JAN -> DEZ)
ordenarDataVenda = file_to_order_DF.sort_values(by="Data Venda")

# ordena pela coluna 'Total Vendas' de forma crescente (0 -> 9)
ordenarTotalVendas = file_to_order_DF.sort_values(by="Total Vendas")

# display(ordenarVendedor)
#displau(desc_ordenarVendedor)
# display(ordenarProduto)
# display(ordenarDataVenda)
# display(ordenarTotalVendas)

# para ordenar por duas colunas, deve se especificar a primeira coluna a ser usada para a ordenacao e depois
# a segunda:
ordenarDuasColunas = file_to_order_DF.sort_values(by=["Vendedor", "Produto"])

display(ordenarDuasColunas)
