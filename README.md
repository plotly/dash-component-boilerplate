# Dash Component Boilerplate

This repository contains a cookiecutter template to create your own dash components.

## Usage

To use this boilerplate:

1. Install the requirements:
    ```
    $ pip install cookiecutter
    $ pip install virtualenv
    ```
2. Run cookiecutter on the boilerplate repo:
    ```
    $ cookiecutter git@github.com:plotly/dash-component-boilerplate.git
    ```
3. Answer the questions about the project.
    - project name
    - component name
    - author info
    - description
    - version
    - license
    - publish_on_npm: Set to false to only serve locally from the package data.
    - install_dependencies: Set to false to only generate the project structure.
4. The project will be generated in the folder of `project_shorname`.
5. Follow the directions in the generated README to start developing your new dash component.

Installing the dependencies can take a long time. They will be installed in a
folder named `venv`, created by virtualenv. This ensure that dash is installed
to generate the components in the `build:py` script of the generated 
`package.json`.
