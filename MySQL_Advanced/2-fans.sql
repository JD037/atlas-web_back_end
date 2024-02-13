-- Ranks country origins of bands by the total number of fans
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
WHERE split IS NULL -- Considering only bands that haven't split
GROUP BY origin
ORDER BY nb_fans DESC;
