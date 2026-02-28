import pandas as pd
import matplotlib.pyplot as plt

# Carregando o arquivo que limpei na Parte 1
df = pd.read_csv('data_clean.csv')

# Recriando a coluna de Total da Venda (pois não tínhamos salvo ela no CSV)
df['Total_Venda'] = df['Quantidade'] * df['Preco']

df.head()

# Garante que o Pandas entenda a coluna 'Data' como um formato de data real
df['Data'] = pd.to_datetime(df['Data'])

# Cria uma nova coluna chamada 'MesAno', pegando apenas o Ano e o Mês (ex: 2023-01)
df['MesAno'] = df['Data'].dt.to_period('M')

# Agrupa as linhas pelo 'MesAno' e SOMA o 'Total_Venda'
vendas_mensais = df.groupby('MesAno')['Total_Venda'].sum().reset_index()

# Vamos ver a nova tabela resumida:
print(vendas_mensais)

# 1. Ajuste técnico: convertemos o 'MesAno' para texto (string)
# 1. Criamos um dicionário "traduzindo" o formato numérico para os nomes em português
meses_ptbr = {
    '2023-01': 'Janeiro', '2023-02': 'Fevereiro', '2023-03': 'Março',
    '2023-04': 'Abril', '2023-05': 'Maio', '2023-06': 'Junho',
    '2023-07': 'Julho', '2023-08': 'Agosto', '2023-09': 'Setembro',
    '2023-10': 'Outubro', '2023-11': 'Novembro', '2023-12': 'Dezembro'
}

# 2. Usamos a função .replace() para substituir os valores na nossa tabela
vendas_mensais['MesAno'] = vendas_mensais['MesAno'].replace(meses_ptbr)

# Vamos confirmar que mudou:
print(vendas_mensais)

# 2. Cria a "tela" do nosso gráfico e define o tamanho (10 de largura por 5 de altura)
plt.figure(figsize=(10, 5))

# 3. Desenha a linha!
# Passamos quem é o eixo X (Meses) e quem é o eixo Y (Total).
# O "marker='o'" coloca uma bolinha marcando cada mês para ficar mais fácil de ler.
plt.plot(vendas_mensais['MesAno'], vendas_mensais['Total_Venda'], marker='o', color='blue', linewidth=2)

# 4. Coloca os textos para deixar o gráfico profissional
plt.title('Tendência de Vendas Mensais em 2023', fontsize=14)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Faturamento Total (R$)', fontsize=12)

# 5. Dá uma leve inclinada (45 graus) nos nomes dos meses para eles não se espremerem
plt.xticks(rotation=45)

# 6. Ajusta as margens para ficar bonito e mostra o gráfico na tela!
plt.tight_layout()
plt.show()

**Insight 1: Sazonalidade Negativa no Início do Ano**
A análise da tendência revela que o ano se inicia com um forte déficit de faturamento. Janeiro representa o vale do gráfico, sendo o pior mês em vendas de todo o período. Após uma breve e leve melhora em fevereiro, a receita volta a despencar em março e se mantém em patamares de baixa oscilação durante quase todo o primeiro semestre. Esse padrão sugere uma possível sazonalidade negativa para o negócio nos primeiros meses do ano, típica de períodos pós-festas.

**Insight 2: Alta Volatilidade e Pico Isolado no 3º Trimestre**
O gráfico demonstra que as vendas não seguem uma linha de crescimento constante, caracterizando um cenário de alta volatilidade. O maior destaque é a recuperação abrupta no final do terceiro trimestre, onde setembro atinge o pico máximo de vendas do ano, superando de longe todos os outros meses. Como esse salto é precedido por um mês muito fraco (agosto) e seguido por novas quedas, o padrão indica que o faturamento da empresa é fortemente dependente de eventos pontuais, promoções ou demandas muito específicas dessa época.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carrega os dados oficiais
df = pd.read_csv('data_clean.csv')
df['Total_Venda'] = df['Quantidade'] * df['Preco']
df['Data'] = pd.to_datetime(df['Data'])
df['MesAno'] = df['Data'].dt.to_period('M').astype(str)

# Dicionário para traduzir os meses (como fizemos antes)
meses_ptbr = {
    '2023-01': 'Jan', '2023-02': 'Fev', '2023-03': 'Mar', '2023-04': 'Abr',
    '2023-05': 'Mai', '2023-06': 'Jun', '2023-07': 'Jul', '2023-08': 'Ago',
    '2023-09': 'Set', '2023-10': 'Out', '2023-11': 'Nov', '2023-12': 'Dez'
}
df['MesAno'] = df['MesAno'].replace(meses_ptbr)

# Configura o estilo dos gráficos
sns.set_theme(style="whitegrid")

# ==========================================
# GRÁFICO EXTRA 1: Faturamento por Produto
# ==========================================
# Agrupa os dados para saber qual produto deu mais dinheiro no ano todo
faturamento_produto = df.groupby('Produto')['Total_Venda'].sum().reset_index()
# Coloca em ordem do maior para o menor
faturamento_produto = faturamento_produto.sort_values(by='Total_Venda', ascending=False)

plt.figure(figsize=(10, 6))
# Gráfico de barras horizontais (ótimo para ler nomes de produtos)
sns.barplot(data=faturamento_produto, x='Total_Venda', y='Produto', hue='Produto', palette='viridis', legend=False)

plt.title('Ranking de Faturamento por Produto (2023)', fontsize=16, pad=15)
plt.xlabel('Faturamento Total (R$)', fontsize=12)
plt.ylabel('Produto', fontsize=12)
plt.tight_layout()
plt.show()


# ==========================================
# GRÁFICO EXTRA 2: Quantidade Vendida por Mês (Empilhado por Produto)
# ==========================================
# Esse gráfico mostra o volume de vendas a cada mês, com cores diferentes para cada produto!
# Prepara uma tabela cruzada (Pivot Table)
pivot_produtos = df.pivot_table(index='MesAno', columns='Produto', values='Quantidade', aggfunc='sum').fillna(0)

# Garante que os meses fiquem na ordem certa no gráfico
ordem_meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
pivot_produtos = pivot_produtos.reindex(ordem_meses)

# Desenha o gráfico de barras empilhadas
pivot_produtos.plot(kind='bar', stacked=True, figsize=(12, 7), colormap='Set2')

plt.title('Quantidade de Produtos Vendidos a Cada Mês', fontsize=16, pad=15)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Quantidade de Unidades Vendidas', fontsize=12)
plt.legend(title='Produtos', bbox_to_anchor=(1.05, 1), loc='upper left') # Coloca a legenda fora do gráfico
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

**Insight 1: Liderança de Faturamento do Segmento de Periféricos e Portáteis:**

Através do ranking de faturamento, identifica-se que o Teclado e o Notebook são os pilares financeiros da operação em 2023, somando os maiores valores acumulados. O Teclado, especificamente, destaca-se como o produto de maior impacto no caixa, superando a marca de R$ 230 mil reais.

**Insight 2: Correlação entre Volume de Itens e Pico de Faturamento em Setembro:**

Ao cruzar os dados, observa-se que o pico de faturamento registrado em Setembro foi diretamente impulsionado por um volume recorde de unidades vendidas (aprox. 50 itens). O gráfico empilhado revela que este sucesso deveu-se à alta demanda simultânea de Teclados e Notebooks naquele mês, enquanto os meses de baixa (como Janeiro) sofreram com a ausência quase total de vendas desses itens de maior valor.
