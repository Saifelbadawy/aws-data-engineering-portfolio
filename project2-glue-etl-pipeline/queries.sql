SELECT *
FROM sales_processed_parquet
LIMIT 10;

SELECT region, SUM(total_profit) AS total_profit
FROM sales_processed_parquet
GROUP BY region;

SELECT sales_rep, SUM(total_profit) AS total_profit
FROM sales_processed_parquet
GROUP BY sales_rep
ORDER BY total_profit DESC;