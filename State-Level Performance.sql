SELECT
    State,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    (SUM(Profit) / SUM(Sales)) * 100 AS Profit_Margin_Percentage
FROM
    retail_project.superstore
GROUP BY
    State
ORDER BY
    Profit_Margin_Percentage DESC;