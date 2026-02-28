import pandas as pd
import matplotlib.pyplot as plt

# Carregando o arquivo que limpei na Parte 1
df = pd.read_csv('data_clean.csv')

print(df.head())

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

**Insight 1 — Forte Recuperação e Pico no Terceiro Trimestre**

Observa-se uma trajetória de crescimento consistente entre maio e julho, indicando uma fase de recuperação nas vendas ao longo do segundo trimestre. No entanto, o destaque principal ocorre em setembro, que apresenta um pico expressivo de faturamento, significativamente superior aos demais meses do ano. Esse comportamento sugere a presença de um fator sazonal ou evento específico que impulsionou as vendas nesse período.

**Insight 2 — Alta Volatilidade e Quedas Abruptas**

O gráfico evidencia um padrão de alta volatilidade nas vendas ao longo do ano. Após períodos de crescimento, há quedas abruptas, como observado entre julho e agosto, e novamente após o pico de setembro. Esse comportamento indica instabilidade no volume de vendas, sugerindo que o desempenho pode estar associado a fatores pontuais, como campanhas específicas ou variações de demanda.

import seaborn as sns

plt.figure(figsize=(8,5))
sns.boxplot(x='Produto', y='Preco', data=df)
plt.title("Distribuição de Preço por Produto")
plt.xticks(rotation=45)
plt.show()

O boxplot revela maior dispersão de preços para Notebook e Monitor, indicando variação relevante dentro desses produtos, possivelmente associada a diferentes modelos ou configurações. Já Mouse e Teclado apresentam menor amplitude e menor variabilidade, sugerindo precificação mais estável. A maior variabilidade nos produtos de maior valor pode representar flexibilidade estratégica de precificação, enquanto os itens de menor valor operam dentro de faixas mais restritas.

quantidade_produto = df.groupby('Produto')['Quantidade'].sum().reset_index()

plt.figure(figsize=(8,5))
plt.bar(quantidade_produto['Produto'], quantidade_produto['Quantidade'])
plt.title("Quantidade Total Vendida por Produto")
plt.xlabel("Produto")
plt.ylabel("Quantidade Vendida")
plt.xticks(rotation=45)
plt.show()

A análise do volume total vendido mostra que o Notebook lidera também em quantidade comercializada, não apenas em valor médio. Teclado e Headset apresentam volumes próximos, enquanto o Mouse possui a menor quantidade vendida no período. Esse comportamento indica que o Notebook combina alto valor unitário com alta demanda, tornando-se o principal impulsionador de desempenho do portfólio. Já os produtos de menor valor unitário não compensam completamente o preço reduzido com maior volume.

ticket_medio = df.groupby('Produto')['Total_Venda'].sum() / df.groupby('Produto')['Quantidade'].sum()
ticket_medio = ticket_medio.reset_index(name='Ticket_Medio')

plt.figure(figsize=(8,5))
plt.bar(ticket_medio['Produto'], ticket_medio['Ticket_Medio'])
plt.title("Ticket Médio por Produto")
plt.xlabel("Produto")
plt.ylabel("Ticket Médio (R$)")
plt.xticks(rotation=45)
plt.show()

O gráfico de ticket médio evidencia diferenças significativas entre os produtos. O Notebook apresenta o maior valor médio por unidade vendida, seguido pelo Monitor, indicando que esses itens possuem maior valor agregado. Em contrapartida, Mouse e Teclado apresentam ticket médio consideravelmente inferior, caracterizando-os como produtos de menor valor unitário. Esse padrão sugere que o faturamento total é fortemente influenciado por itens de alto preço, enquanto os produtos mais acessíveis dependem de maior volume para gerar impacto relevante na receita.

# Faturamento total por produto
vendas_produto = df.groupby('Produto')['Total_Venda'].sum().reset_index()

plt.figure(figsize=(8,5))
plt.bar(vendas_produto['Produto'], vendas_produto['Total_Venda'])
plt.title("Faturamento Total por Produto")
plt.xlabel("Produto")
plt.ylabel("Faturamento Total (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

O faturamento total por produto confirma a forte concentração de receita no Notebook, que supera amplamente os demais itens. O Monitor aparece como segundo maior gerador de receita, enquanto Mouse, Teclado e Headset apresentam participação significativamente menor. Essa concentração pode representar oportunidade de crescimento nos demais produtos, mas também sugere risco operacional caso haja queda na demanda do principal item responsável pela geração de receita.
