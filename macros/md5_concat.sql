{% macro md5_concat(fields) -%}
    MD5({{ adapter.dispatch('concat')(fields) }})
{%- endmacro %}

{% macro md5_concat__default(fields) -%}
    CONVERT(VARCHAR(32), HashBytes('MD5', concat({{ fields|join(', ') }})),2)
{%- endmacro %}

{% macro md5_snowflake__concat(fields, source) %}
    md5(
        '{{ source }}' || '-' || 
        {% for field in fields %} ifnull(CAST({{ field }} AS VARCHAR),'') {{ ' || ' if not loop.last else '' }}{% endfor %}
        || '-' || '{{ source }}'
    )
{% endmacro %}

{% macro md5_redshift__concat(fields) %}
    md5({% for field in fields %}nullif(CAST({{ field }} AS VARCHAR),'') {{ ' || ' if not loop.last }}{% endfor %})
{% endmacro %}