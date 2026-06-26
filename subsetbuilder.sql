DECLARE @Items VARCHAR(100) = 'A,B,C'; -- Define the items

WITH ItemsList AS (
    -- Split the comma-separated string into individual rows with an index
    SELECT value AS Item, ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) - 1 AS BitIndex
    FROM STRING_SPLIT(@Items, ',')
),
Numbers AS (
    -- Generate numbers from 0 to (2^N - 1)
    -- Using TOP with CROSS JOIN handles up to 32,768 permutations (Adjust as needed)
    SELECT TOP (POWER(2, (SELECT COUNT(*) FROM ItemsList))) 
           ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) - 1 AS SubsetMask
    FROM master.dbo.spt_values t1
    CROSS JOIN master.dbo.spt_values t2
)
SELECT 
    n.SubsetMask,
    -- Aggregate the items based on the binary mask (where the bit is set)
    STUFF((
        SELECT ',' + i.Item
        FROM ItemsList i
        WHERE (n.SubsetMask & POWER(2, i.BitIndex)) > 0
        FOR XML PATH(''), TYPE
    ).value('.', 'VARCHAR(MAX)'), 1, 1, '') AS Subset
FROM Numbers n
ORDER BY n.SubsetMask;
