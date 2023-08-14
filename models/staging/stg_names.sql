{{ config(
  post_hook = "create stream if not exists pmistry_dbt.rawstream1 ON table {{ ref('names') }};"
) }}

select * from {{ ref('names') }}