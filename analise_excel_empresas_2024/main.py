import pandas as pd
import plotly.express as px

# formata a saída de dados do tipo float em 2 casas decimais
pd.options.display.float_format = '{:.2f}'.format

file_name = "C:\\Dados\\Excel\\Imersão Python_Tabela de ações.xlsx"

df_principal = pd.read_excel(file_name, sheet_name="Principal")
df_Total_de_acoes = pd.read_excel(file_name, sheet_name="Total_de_acoes")
df_Ticker = pd.read_excel(file_name, sheet_name="Ticker")
df_ChatGPT = pd.read_excel(file_name, sheet_name="ChatGPT")

# Recupera apenas as colunas necessárias
df_principal = df_principal[['Ativo', 'Data', 'Último (R$)', 'Var. Dia (%)']].copy()

# Renomear colunas
df_principal = df_principal.rename(columns={'Último (R$)': 'valor_final', 'Var. Dia (%)': 'var_dias_pct'}).copy()

### TRATAMENTOS: ###

# transforma as % da coluna 'var_dias_pct' para decimal para efetuar os cálculos
df_principal['var_dias_pct'] = df_principal['var_dias_pct'] / 100 

# Cria coluna 'valor_inicial'
df_principal['valor_inicial'] = df_principal['valor_final'] / (df_principal['var_dias_pct'] + 1)

# Agrupa coluna 'Ativo' com a planilha TICKER e adiciona coluna 'Qtde. Teórica'
df_principal = df_principal.merge(df_Total_de_acoes, left_on='Ativo', right_on='Código', how='left')

# Remove a coluna 'Código'
df_principal = df_principal.drop(columns=['Código'])

# Calcula variação em reais a diciona a coluna 'Variacao_R$'
df_principal['variacao_R$'] = (df_principal['valor_final'] - df_principal['valor_inicial']) * df_principal['Qtde. Teórica']

# Formata a coluna 'Qtde. Teórica' para inteiro
df_principal['Qtde. Teórica'] = df_principal['Qtde. Teórica'].astype(int)

# Renomear coluna 'Qtde. Teórica'
df_principal = df_principal.rename(columns={'Qtde. Teórica': 'qtd_teorica'}).copy()

# Verifica linha a linha se a variação subiu ou desceu, verificando se a mesma é maior que 0 ou não, ou se é igual a 0 
df_principal['Resultado'] = df_principal['variacao_R$'].apply(lambda x: 'Subiu' if x > 0 else ('Desceu' if x < 0 else 'Não se alterou'))

# Recupera o nome da empresa e cria uma nova coluna chamada 'nome_empresa'
df_principal = df_principal.merge(df_Ticker, left_on='Ativo', right_on='Ticker', how='left')

# Remove a coluna com valores duplicados 'Ticker'
df_principal = df_principal.drop(columns=['Ticker'])

# Agrupa com a idade informada na Planilha 'ChatGPT'
df_principal = df_principal.merge(df_ChatGPT, left_on='Nome', right_on='Empresa', how='left')

# Remove a coluna 'Empresa' que está com valores duplicados
df_principal = df_principal.drop(columns=['Empresa'])

# Renomear coluna 'Qtde. Teórica'
df_principal = df_principal.rename(columns={'Idade (em anos)': 'idade'}).copy()

# Separa em 3 categorias a idade das empresas
df_principal['cat_idade'] = df_principal['idade'].apply(lambda x: 'Mais de 100 anos' if x > 100 else ('Menos que 50 anos' if x < 50 else 'Entre 50 e 100 anos'))

### ANÁLISES: ###
# Maior valor
maior_valor = df_principal['variacao_R$'].max()
# Menor valor
menor_valor = df_principal['variacao_R$'].min()
# Media
media = df_principal['variacao_R$'].mean()
# Média de quem subiu
media_quem_subiu = df_principal[df_principal['Resultado'] == 'Subiu']['variacao_R$'].mean()
media_quem_desceu = df_principal[df_principal['Resultado'] == 'Desceu']['variacao_R$'].mean()

# Novo DF com primeiras analises dos valores
df_analise_valores = pd.DataFrame({
    'maior_valor': [maior_valor],
    'menor_valor': [menor_valor],
    'media_quem_subiu': [media_quem_subiu],
    'media_quem_desceu': [media_quem_desceu],
})

# cria um DataFrame apenas com as empresas que tenha Resultado = 'Subiu'
df_principal_subiu = df_principal[df_principal['Resultado'] == 'Subiu']

# cria um Dataframe agrupado por segmento, somando a coluna 'variacao_R$', a funcao reset_index() transforma a variável
# df_analise_segmento que estava como array, em um DataFrame
df_analise_segmento = df_principal_subiu.groupby('Segmento')['variacao_R$'].sum().reset_index()

# cria novo DataFrame para agrupar os valores de quem subiu, quem desceu e quem não se alterou
df_analise_saldo = df_principal.groupby('Resultado')['variacao_R$'].sum().reset_index()

# Plotando gráfico
fig = px.bar(df_analise_saldo, 'Resultado', 'variacao_R$', text='variacao_R$', title='Variação Reais por Resultado')
fig.show()
