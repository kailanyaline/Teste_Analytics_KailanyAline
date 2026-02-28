-- ============================================================
-- ARQUIVO: consultas_sql.sql
-- DESCRIÇÃO: Consultas SQL + explicação da lógica (Parte 2)
-- TABELA: vendas
--
-- Observação:
-- O dataset simulado cobre o período 01/01/2023 a 31/12/2023.
-- Portanto, a consulta solicitada para "junho de 2024" foi
-- adaptada para "junho de 2023", mantendo a mesma lógica.
-- ============================================================


-- ------------------------------------------------------------
-- CONSULTA 1
-- Objetivo: Listar produto, categoria e o faturamento total
--           (Quantidade * Preco) por produto, em ordem decrescente.
--
-- Lógica:
-- 1) GROUP BY Produto, Categoria:
--    Agrupa as vendas por produto (e sua categoria) para consolidar
--    várias linhas em uma linha por item.
-- 2) SUM(Quantidade * Preco):
--    Calcula o faturamento por linha (Qtd * Preço) e soma dentro
--    de cada grupo, resultando no faturamento total por produto.
-- 3) ORDER BY Total_Vendas DESC:
--    Ordena do maior para o menor faturamento para obter o ranking.
-- ------------------------------------------------------------
SELECT
    Produto,
    Categoria,
    SUM(Quantidade * Preco) AS Total_Vendas
FROM vendas
GROUP BY Produto, Categoria
ORDER BY Total_Vendas DESC;


-- ------------------------------------------------------------
-- CONSULTA 2
-- Objetivo: Identificar quais produtos venderam menos em junho/2023
--           (considerando "vender menos" como menor QUANTIDADE).
--
-- Lógica:
-- 1) WHERE (filtro de mês):
--    Seleciona apenas registros do mês de junho de 2023.
--    A função strftime('%Y-%m', Data) é compatível com SQLite,
--    retornando "YYYY-MM" e permitindo filtrar exatamente "2023-06".
-- 2) GROUP BY Produto:
--    Consolida as vendas do mês por produto.
-- 3) SUM(Quantidade):
--    Soma o volume total vendido por produto em junho.
-- 4) ORDER BY Total_Quantidade ASC:
--    Ordena do menor para o maior para destacar os produtos com
--    menor volume de vendas no mês.
-- ------------------------------------------------------------
SELECT
    Produto,
    SUM(Quantidade) AS Total_Quantidade
FROM vendas
WHERE strftime('%Y-%m', Data) = '2023-06'
GROUP BY Produto
ORDER BY Total_Quantidade ASC;
