# Identifica e remove linhas duplicadas em DataFrames
import pandas as pd

# Carrega o excel
baseVendas_DF = pd.read_excel("C:\RPA\scripts\ExcelTest\Base_Vendas.xlsx")

# Exibe um resumo dos dados
baseVendasUnicaResume = baseVendas_DF.nunique()

# verifica pelo parâmetro 'subset' onde existe duplicidade, 'keep' controla como considerar a ocorrência
# do valor duplicado, (considerar primeira ocorrência, considerar última ou falso, considerar qualquer valor 
# que tenha duplicidade)
baseVendasUnica = baseVendas_DF.duplicated(subset="Vendedor", keep="first")

# Exibindo dados: existem vários dados duplicados
display(baseVendas_DF)
# Exibindo resumo dos dados duplicados
display(baseVendasUnicaResume)
# Exibindo onde existe duplicidade
display(baseVendasUnica)

# Adicionando nova coluna com a exibição da duplicidade
baseVendas_DF['Confere Duplicidade'] = baseVendas_DF.duplicated(subset="Vendedor", keep="first")
display(baseVendas_DF)

# Mantem a primeira ocorrência de um valor duplicado e elimina as demais
baseSemCopias = baseVendas_DF.drop_duplicates(subset='Vendedor', keep="first")
display(baseSemCopias)
