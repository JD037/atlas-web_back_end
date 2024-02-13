-- Assumes metal_bands table is already imported
SELECT origin, COUNT(*) AS nb_fans
FROM bands
GROUP BY origin
ORDER BY nb_fans DESC;