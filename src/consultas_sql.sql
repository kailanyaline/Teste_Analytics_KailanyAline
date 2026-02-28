
-- ============================================================
-- ARQUIVO: consultas_sql.sql
-- DESCRIÇÃO: Consultas de análise de faturamento e volume de vendas
-- ============================================================

-- EXPLICAÇÃO DA LÓGICA:
-- O processo seguiu a estrutura fundamental da linguagem SQL:
-- 1. Filtragem (WHERE): Para a análise mensal, isolamos os dados 
--    através do operador LIKE, que permite selecionar um padrão 
--    específico de data (Ano-Mês).
-- 2. Agrupamento (GROUP BY): Para consolidar dados de diversas 
--    vendas em uma única linha por produto, agrupamos as 
--    informações pela coluna 'Produto'.
-- 3. Agregação (SUM): Realizamos o cálculo matemático de faturamento 
--    (Quantidade * Preço) e de volume (Quantidade) dentro de cada grupo.
-- 4. Ordenação (ORDER BY): Organizamos os resultados para facilitar 
--    a leitura (DESC para os maiores valores e ASC para os menores).

-- ------------------------------------------------------------
-- CONSULTA 1: Nome do produto, categoria e soma total de vendas
-- Objetivo: Ranking de faturamento em ordem decrescente.
-- ------------------------------------------------------------
SELECT 
    Produto, 
    Categoria, 
    SUM(Quantidade * Preco) AS Total_Vendas
FROM vendas
GROUP BY Produto, Categoria
ORDER BY Total_Vendas DESC;

-- ------------------------------------------------------------
-- CONSULTA 2: Produtos que venderam menos no mês de junho/2023
-- Objetivo: Identificar itens com menor performance de saída.
-- ------------------------------------------------------------
SELECT 
    Produto, 
    SUM(Quantidade) AS Total_Quantidade
FROM vendas
WHERE Data LIKE '2023-06%'
GROUP BY Produto
ORDER BY Total_Quantidade ASC;
