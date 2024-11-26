import pandas as pd

# Carrega o arquivo, pulando as linhas iniciais de cabeçalho (agora pularemos 5 linhas)
arquivo = r'c:\Users\alenc\Desktop\DadosMeteorologicos_barra_Janeiro_2023\riocentro_202301_Met.txt'
dados = pd.read_csv(arquivo, sep=r'\s+', skiprows=5, engine='python')

# Exibe as 10 primeiras linhas para verificar os dados
print("Dados carregados:")
print(dados.head(10))

# Substitui valores "ND" por NaN (Not a Number) e converte a coluna "Chuva" para numérico
dados['Chuva'] = pd.to_numeric(dados['Chuva'].replace('ND', pd.NA), errors='coerce')

# Verifica o tipo da coluna "Chuva"
print("\nTipo de dados da coluna 'Chuva':")
print(dados['Chuva'].dtype)

# Verifica os valores únicos na coluna "Chuva"
print("\nValores únicos na coluna 'Chuva':")
print(dados['Chuva'].unique())

# Filtra as linhas onde o valor de chuva é diferente de 0.0 e não é NaN
chuva_diferente_zero = dados[dados['Chuva'].notna() & (dados['Chuva'] != 0.0)]

# Exibe os resultados
print("\nRegistros com chuva diferente de 0.0:")
print(chuva_diferente_zero[['Dia', 'Hora', 'Chuva']])
