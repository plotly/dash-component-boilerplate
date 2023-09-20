{% if cookiecutter.component_type == "Function Component" -%}
    {%- include 'cookiecutter_templates/FunctionComponent.react.js' -%}
{%- else -%}
    {%- include 'cookiecutter_templates/ClassComponent.react.js' -%}
{%- endif -%}
