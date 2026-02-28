# Teste Analytics Kailany Aline

## Parte 1 — Limpeza e Análise de Dados de Vendas

### Objetivo

Simular um dataset de vendas contendo pelo menos 50 registros no período de 01/01/2023 a 31/12/2023, realizar a limpeza dos dados e executar análises básicas de faturamento.

---

### Estrutura dos Dados

O dataset contém as seguintes colunas:

* **ID**: identificador único da venda
* **Data**: data da transação
* **Produto**: nome do produto vendido
* **Categoria**: categoria do produto
* **Quantidade**: quantidade vendida
* **Preco**: preço unitário do produto
* **Total_Venda**: faturamento por transação (Quantidade × Preco)

Foram gerados **60 registros simulados**.

### Simulação dos Dados

* A geração dos dados foi feita utilizando `numpy` e `pandas`.
* Foi definida uma **seed aleatória (`np.random.seed(42)`)** para garantir reprodutibilidade.
* Os preços foram simulados de forma coerente com cada produto, utilizando faixas específicas:

  * Notebook: 1800 a 5000
  * Monitor: 800 a 3500
  * Mouse: 50 a 400
  * Teclado: 120 a 600
  * Headset: 150 a 800
* As categorias foram atribuídas de forma consistente via mapeamento fixo produto → categoria.

### Limpeza dos Dados

Durante a simulação, foram inseridos propositalmente:

* 1 valor faltante na coluna **Preco**
* 1 linha duplicada

Os seguintes tratamentos foram aplicados:

* Remoção de duplicatas com `drop_duplicates()`
* Identificação de valores nulos com `isnull()`
* Imputação do valor faltante utilizando a **média do preço do próprio produto**, evitando distorções
* Verificação dos tipos de dados com `.dtypes`

Após a limpeza, o dataset final foi salvo como:

```
data_clean.csv
```

### Geração e Download dos Arquivos CSV

O script gera automaticamente dois arquivos:

* `data_raw.csv` — dataset bruto (antes da limpeza)
* `data_clean.csv` — dataset após tratamento e criação da coluna `Total_Venda`

Os arquivos são salvos no diretório de execução.

### Execução no Google Colab

Como o desenvolvimento foi realizado no Google Colab, foi incluído no script o seguinte trecho:

```python
from google.colab import files
files.download("data_clean.csv")
```

Esse comando permite realizar o download automático do arquivo gerado para a máquina local.

Caso o script seja executado fora do Colab (ex: VS Code ou terminal), essa parte pode ser removida sem impactar o funcionamento principal.

### Análise Realizada

1. Criação da coluna **Total_Venda** (Quantidade × Preco)
2. Cálculo do faturamento total por produto
3. Identificação do produto com maior faturamento total

A agregação foi realizada utilizando `groupby()` e `sum()`.

### Suposições Adotadas

* Os dados foram simulados para fins analíticos e não representam vendas reais.
* As faixas de preço foram definidas para manter coerência entre produtos.
* A imputação por média do produto foi escolhida por preservar o comportamento estatístico específico de cada item.

### Como Executar

1. Instale as dependências:

```
pip install pandas numpy
```

2. Execute o script:

```
python simulacao_limpeza_analise.py
```

---

## Parte 2 — Análise Exploratória de Dados (EDA)

### Objetivo

Realizar análise exploratória utilizando o dataset limpo (`data_clean.csv`), com foco em identificar padrões temporais, concentração de receita e comportamento de preços.

### Visualizações Desenvolvidas

Foram construídos os seguintes gráficos:

1. **Tendência de Vendas Mensais (Gráfico de Linha)**

   * Análise da evolução do faturamento ao longo de 2023.
   * Identificação de padrões de crescimento, quedas e possíveis sazonalidades.

2. **Distribuição de Preço por Produto (Boxplot)**

   * Avaliação da dispersão e variabilidade dos preços.
   * Comparação entre produtos de alto e baixo valor agregado.

3. **Quantidade Total Vendida por Produto (Gráfico de Barras)**

   * Análise de volume comercializado.
   * Identificação de produtos com maior demanda.

4. **Ticket Médio por Produto (Gráfico de Barras)**

   * Cálculo do valor médio por unidade vendida.
   * Comparação entre produtos de alto e baixo valor unitário.

5. **Faturamento Total por Produto (Gráfico de Barras)**

   * Avaliação da concentração de receita.
   * Identificação do principal produto gerador de receita.

### Principais Achados

* Observou-se volatilidade nas vendas mensais, com pico significativo em setembro.
* O produto **Notebook** apresenta maior ticket médio, maior volume e maior faturamento total, indicando forte concentração de receita.
* Produtos de menor valor unitário possuem menor dispersão de preço e menor impacto na receita.
* A estrutura de receita demonstra dependência relevante de produtos de maior valor agregado.

### Tecnologias Utilizadas

* `pandas`
* `matplotlib`
* `seaborn`

---
