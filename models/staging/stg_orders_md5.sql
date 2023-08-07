{% set results = run_query('select 1 as id') %}
{% set keys = ['id','user_id'] %}
{% set source = 'seed_orders' %}


with source as (

    {#-
    Normally we would select from the table here, but we are using seeds to load
    our data in this project
    #}
    select * from {{ ref('raw_orders') }}

),

renamed as (

    select
        {{ md5_snowflake__concat(keys,source) }} as order_key,
        id as order_id,
        user_id as customer_id,
        order_date,
        status

    from source

)

select * from renamed