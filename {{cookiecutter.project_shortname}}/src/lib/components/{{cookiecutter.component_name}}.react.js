{%- if cookiecutter.use_async == "True" -%}
    {%- include 'cookiecutter_templates/AsyncComponent.react.js' -%}
{%- else -%}
    {%- include 'cookiecutter_templates/Component.react.js' -%}
{%- endif -%}