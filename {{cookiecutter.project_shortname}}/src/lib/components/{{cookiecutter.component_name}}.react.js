{%- if "Async" in cookiecutter.component_type and "Class" in cookiecutter.component_type -%}
    {%- include 'cookiecutter_templates/AsyncClassComponent.react.js' -%}
{%- elif "Async" in cookiecutter.component_type and "Function" in cookiecutter.component_type -%}
    {%- include 'cookiecutter_templates/AsyncFunctionComponent.react.js' -%}
{%- elif "Class" in cookiecutter.component_type -%}
    {%- include 'cookiecutter_templates/ClassComponent.react.js' -%}
{%- else -%}
    {%- include 'cookiecutter_templates/FunctionComponent.react.js' -%}
{%- endif -%}
