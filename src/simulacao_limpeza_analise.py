# Importa a biblioteca pandas para manipulação e análise de dados em formato de tabela
import pandas as pd

# Importa a biblioteca numpy para geração de números aleatórios e operações numéricas
import numpy as np

# Importa datetime para trabalhar com datas
# e timedelta para somar dias a uma data específica
from datetime import datetime, timedelta

# Fixa a semente aleatória para garantir que os dados sejam sempre os mesmos!
np.random.seed(42)

# Define a data inicial do período (1º de janeiro de 2023)
inicio = datetime(2023, 1, 1)

# Define a data final do período (31 de dezembro de 2023)
fim = datetime(2023, 12, 31)

# Gera 60 datas aleatórias dentro de 2023
# np.random.randint(0, 365) gera um número aleatório de dias
# timedelta transforma esse número em dias
# inicio + timedelta soma esses dias à data inicial
# for _ in range(60) repete o processo 60 vezes
datas = [inicio + timedelta(days=np.random.randint(0, 365)) for _ in range(60)]

# Mapeamento de produtos para categorias fixas
mapa_produtos = {
    "Notebook": "Eletrônicos",
    "Monitor": "Eletrônicos",
    "Mouse": "Acessórios",
    "Teclado": "Acessórios",
    "Headset": "Acessórios"
}

# Sorteia apenas os produtos (usando as chaves do dicionário)
produtos_sorteados = np.random.choice(list(mapa_produtos.keys()), 60)

# Cria o DataFrame com 60 registros simulados
dados = pd.DataFrame({
    "ID": range(1, 61),  # Cria IDs de 1 até 60
    "Data": datas,  # Usa as datas aleatórias criadas anteriormente
    "Produto": produtos_sorteados,  # Usa os produtos sorteados
    "Categoria": [mapa_produtos[prod] for prod in produtos_sorteados],  # Puxa a categoria correta para cada produto
    "Quantidade": np.random.randint(1, 10, 60),  # Gera quantidade vendida entre 1 e 9
    "Preco": np.random.uniform(50, 5000, 60).round(2)  # Gera preços entre 50 e 5000
})
dados.head()

# Inserindo um valor faltante propositalmente na coluna Preco
dados.loc[5, "Preco"] = np.nan

# Inserindo uma linha duplicada propositalmente
dados = pd.concat([dados, dados.iloc[[0]]], ignore_index=True)

dados.info()


#Limpeza de Dados
# Remove registros duplicados
dados = dados.drop_duplicates()

# Verifica novamente
dados.info()

# Filtra e exibe apenas as linhas onde a coluna Preco está nula
# isnull() identifica valores ausentes
# O filtro retorna apenas os registros problemáticos
dados[dados['Preco'].isnull()]

# Preenche valores nulos usando média por produto (automático e seguro)
dados['Preco'] = dados.groupby('Produto')['Preco'].transform(lambda x: x.fillna(x.mean()))

# Verifica novamente
print(dados.isnull().sum())
# Exibe a linha de índice 5 para verificar o novo valor do Preco
print(dados.loc[5])

# Verifica o tipo dos dados
print(dados.dtypes)

# Visualiza as primeiras linhas finais
dados.head()

# Salva o dataset limpo com codificação que aceita acentos (UTF-8 com BOM)
dados.to_csv("data_clean.csv", index=False, encoding='utf-8-sig')
from google.colab import files
files.download("data_clean.csv")

# Cria coluna de faturamento total por linha
dados['Total_Venda'] = dados['Quantidade'] * dados['Preco']

# Calcula o total de vendas por produto
vendas_por_produto = dados.groupby('Produto')['Total_Venda'].sum().reset_index()
print(vendas_por_produto)

# Identifica o produto com maior faturamento total
produto_top = vendas_por_produto.sort_values(by='Total_Venda', ascending=False).iloc[0]
print(produto_top)
