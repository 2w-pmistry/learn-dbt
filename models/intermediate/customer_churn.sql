WITH customers AS (
    SELECT * FROM {{ ref('stg_customers') }}
),

orders AS (
    SELECT * FROM {{ ref('stg_orders') }}
),

customer_orders AS (
    SELECT
        customer_id,
        MIN(order_date) AS first_order,
        MAX(order_date) AS most_recent_order,
        COUNT(order_id) AS number_of_orders
    FROM orders
    GROUP BY customer_id
),

final AS (
    SELECT
        customers.customer_id,
        customers.first_name,
        customers.last_name,
        customer_orders.first_order,
        customer_orders.most_recent_order,
        CASE 
            WHEN customer_orders.first_order IS NULL OR customer_orders.most_recent_order IS NULL THEN 'Never Ordered'
            WHEN DATEDIFF(DAY, customer_orders.most_recent_order, CURRENT_DATE) > 90 THEN 'Churned'
            WHEN DATEDIFF(DAY, customer_orders.most_recent_order, CURRENT_DATE) BETWEEN 60 AND 90 THEN 'Churn Risk'
            ELSE 'Healthy'
        END AS customer_status,
        COALESCE(customer_orders.number_of_orders, 0) AS number_of_orders
    FROM customers
    LEFT JOIN customer_orders
        ON customers.customer_id = customer_orders.customer_id
)

SELECT * FROM final