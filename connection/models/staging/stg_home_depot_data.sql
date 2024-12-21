-- models/staging/stg_home_depot_data.sql

WITH raw_data AS (
    SELECT
        "INDEX"::int AS "INDEX",          -- Replace with actual case-sensitive name
        "URL" AS "URL",
        "TITLE" AS "TITLE",
        "IMAGES" AS "IMAGES",
        "DESCRIPTION" AS "DESCRIPTION",
        "PRODUCT_ID"::int AS "PRODUCT_ID",
        "SKU"::bigint AS "SKU",
        "GTIN13"::bigint AS "GTIN13",
        "BRAND" AS "BRAND",
        "PRICE"::float AS "PRICE",
        "CURRENCY" AS "CURRENCY",
        "AVAILABILITY" AS "AVAILABILITY",
        "UNIQ_ID" AS "UNIQ_ID",
        "SCRAPED_AT"::timestamp AS "SCRAPED_AT"
    FROM {{ source('home_depot_source', 'raw_data') }}
)

SELECT * FROM raw_data
