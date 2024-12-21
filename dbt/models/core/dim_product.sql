WITH latest_data AS (
    SELECT
        "PRODUCT_ID",
        "TITLE",
        "BRAND",
        "PRICE",
        "AVAILABILITY",
        "SCRAPED_AT",
        ROW_NUMBER() OVER(PARTITION BY "PRODUCT_ID" ORDER BY "SCRAPED_AT" DESC) AS row_num
    FROM {{ ref('stg_home_depot_data') }}
),

effective_data AS (
    SELECT
        "PRODUCT_ID",
        "TITLE",
        "BRAND",
        "PRICE",
        "AVAILABILITY",
        "SCRAPED_AT" AS effective_date,
        LEAD("SCRAPED_AT") OVER(PARTITION BY "PRODUCT_ID" ORDER BY "SCRAPED_AT") AS end_date,
        CASE WHEN row_num = 1 THEN 1 ELSE 0 END AS current_flag
    FROM latest_data
)

SELECT
    "PRODUCT_ID",
    "TITLE",
    "BRAND",
    "PRICE",
    "AVAILABILITY",
    effective_date,
    end_date,
    current_flag
FROM effective_data
