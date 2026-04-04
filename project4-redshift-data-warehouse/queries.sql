SELECT product_category, SUM(total_profit) AS total_profit
FROM sales_warehouse
GROUP BY product_category
ORDER BY total_profit DESC;


SELECT sales_rep, SUM(total_profit) AS total_profit
FROM sales_warehouse
GROUP BY sales_rep
ORDER BY total_profit DESC
LIMIT 5;

SELECT sales_rep, SUM(total_profit) AS total_profit
FROM sales_warehouse
GROUP BY sales_rep
ORDER BY total_profit DESC
LIMIT 5;