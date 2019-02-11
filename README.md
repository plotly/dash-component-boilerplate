# Dash Component Boilerplate

This repository contains a [Cookiecutter](https://github.com/audreyr/cookiecutter) template to create your own Dash components.

## Usage

To use this boilerplate:

1. Install the requirements:
    ```
    $ pip install cookiecutter
    $ pip install virtualenv
    ```
   [Node.js/npm is also required.](https://nodejs.org/en/)
2. Run cookiecutter on the boilerplate repo:
    ```
    $ cookiecutter https://github.com/plotly/dash-component-boilerplate.git
    ```
3. Answer the questions about the project.
    - `project_name`: This is the "human-readable" name of your project. For example, "Dash Core Components". 
    - `project_shortname`: is derived from the project name, it is the name of the "python library" for your project. By default, this is generated from your `project_name` by lowercasing the name and replacing spaces & `-` with underscores. For example, for "Dash Core Components" this would be "dash_core_components".
    - `component_name`: This is the name of the initial component that is generated. The default takes the `project_name` and remove the whitespace and `-`. As a javascript class name it should be in PascalCase.
    - `author info`: author_name and author_email for package.json metadata.
    - `description`: the project description, included in package.json.
    - `license`: License type for the component library.
    - `publish_on_npm`: Set to false to only serve locally from the package data.
    - `install_dependencies`: Set to false to only generate the project structure.
4. The project will be generated in the folder of `project_shortname`.
5. Follow the directions in the generated README to start developing your new Dash component.

Installing the dependencies can take a long time. They will be installed in a
folder named `venv`, created by virtualenv. This ensures that dash is installed
to generate the components in the `build:py` script of the generated 
`package.json`.


## More Resources

- Learn more about Dash: https://dash.plot.ly
- Questions about this project? Create an issue: https://github.com/plotly/dash-component-boilerplate/issues/new
- Watch the [component boilerplate repository](https://github.com/plotly/dash-component-boilerplate) to stay informed of changes to our components.
- [React guide for python developers](https://dash.plot.ly/react-for-python-developers)
- Need help with your component? View the Dash Community Forum: https://community.plot.ly/c/dash
- Examples of Dash component libraries include `dash-core-components`: https://github.com/plotly/dash-core-components and `dash-html-components`: https://github.com/plotly/dash-html-components.
- To get a feel for what's involved in creating a component, read through the [README.MD file that this cookiecutter project generates](%7B%7Bcookiecutter.project_shortname%7D%7D/README.md)
