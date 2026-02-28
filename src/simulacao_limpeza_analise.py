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

# Gera 60 datas aleatórias dentro de 2023
datas = [inicio + timedelta(days=np.random.randint(0, 365)) for _ in range(60)]

# Mapeamento de produtos para categorias fixas
mapa_produtos = {
    "Notebook": "Eletrônicos",
    "Monitor": "Eletrônicos",
    "Mouse": "Acessórios",
    "Teclado": "Acessórios",
    "Headset": "Acessórios"
}

# Sorteia produtos
produtos_sorteados = np.random.choice(list(mapa_produtos.keys()), 60)

# Cria DataFrame (SEM preço ainda)
dados = pd.DataFrame({
    "ID": range(1, 61),
    "Data": datas,
    "Produto": produtos_sorteados,
    "Categoria": [mapa_produtos[prod] for prod in produtos_sorteados],
    "Quantidade": np.random.randint(1, 10, 60)
})

# Faixas de preço por produto
faixas_preco = {
    "Notebook": (1800, 5000),
    "Monitor": (800, 3500),
    "Mouse": (50, 400),
    "Teclado": (120, 600),
    "Headset": (150, 800)
}

# Função para gerar preço conforme o produto
def gerar_preco(produto):
    minimo, maximo = faixas_preco[produto]
    return np.random.uniform(minimo, maximo)

# Criar coluna de preço
dados["Preco"] = dados["Produto"].apply(gerar_preco).round(2)

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

# Preenche valores nulos usando a média por produto, arredondada para 2 casas decimais
dados['Preco'] = dados.groupby('Produto')['Preco'].transform(lambda x: x.fillna(x.mean().round(2)))

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
