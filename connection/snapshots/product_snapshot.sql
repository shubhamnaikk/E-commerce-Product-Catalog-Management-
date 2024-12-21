{% snapshot product_snapshot %}

SELECT
    PRODUCT_ID,
    TITLE,
    BRAND,
    PRICE,
    AVAILABILITY,
    EFFECTIVE_DATE,
    END_DATE,
    CURRENT_FLAG
FROM {{ ref('dim_product') }}

{% endsnapshot %}
