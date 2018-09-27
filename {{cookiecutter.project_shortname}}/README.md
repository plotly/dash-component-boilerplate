# Dash Component Boilerplate

This repository contains the minimal set of code required to create your own custom Dash component.

To create your own Dash component:

1. Install cookiecutter:
```
$ pip install cookiecutter
```
2. Run cookiecutter on the boilerplate repo:
```
$ cookiecutter git@github.com:plotly/dash-component-boilerplate.git
```
The prompt will ask questions about the project, then it will create your project in a directory with the `project_shortname` variable.

3. Install dependencies
    ```
    $ cd {{cookiecutter.project_shortname}}
    ```
    1. Install npm packages
    ```
    $ npm install
    ```
    2.1 Create a virtual env and activate (optional)
    ```
    $ virtualenv venv
    $ venv/Scripts/activate
    ```
    __Note: venv\Scripts\activate for windows__
    2.2 Install python packages (required to build the component)
    ```
    $ pip install -r requirements.txt
    ```
    2.3 Install the python packages for testing (optional)
    ```
    $ pip install -r tests/requirements.txt
    ```
4. Write your component code in `src/lib/components/{{cookiecutter.component_name}}.react.js`. The demo app is in `src/demo` and you will import your example component code into your demo app.
5. Test your code in a Python environment:
    1. Build your code
    ```
    $ npm run build:all
    ```
    2. Run and modify the `usage.py` sample dash app:
    ```
    $ python usage.py
    ```
6. Create a production build and publish:
    1. Build your code:
    ```
    $ npm run build:all
    ```
    2. Create a Python tarball
    ```
    $ python setup.py sdist
    ```
    This distribution tarball will get generated in the `dist/` folder

    3. Test your tarball by copying it into a new environment and installing it locally:
    ```
    $ pip install my_dash_component-0.0.1.tar.gz
    ```

    4. If it works, then you can publish the component to NPM and PyPI:
        1. Cleanup the dist folder (optional)
        ```
        $ rm -rf dist
        ```
        2. Publish on PyPI
        ```
        $ twine upload dist/*
        ```
        3. Publish on NPM (Optional if chosen False in `publish_on_npm`)
        ```
        $ npm publish
        ```
7. Share your component with the community! https://community.plot.ly/c/dash

# More details
- Include CSS files in your distribution folder (`{{cookiecutter.project_shortname}}`) and reference them in `MANIFEST.in`
- The `tests` folder contains a sample integration test. This will run a sample Dash app in a browser. Run this with:
    ```
    $ python -m unittest tests.test_render
    ```
    The Dash team uses these types of integration tests extensively. Browse the Dash component code on GitHub for more examples of testing (e.g. https://github.com/plotly/dash-core-components)
- Publishing your component to NPM will make the JavaScript bundles available on the unpkg CDN. By default, Dash servers the component library's CSS and JS from the remote unpkg CDN, so if you haven't published the component package to NPM you'll need to set the `serve_locally` flags to `True` (unless you choose `False` on `publish_on_npm`). We will eventually make `serve_locally=True` the default, [follow our progress in this issue](https://github.com/plotly/dash/issues/284).
- Watch the [component boilerplate repository](https://github.com/plotly/dash-component-boilerplate) to stay informed of changes to our components.


# More Resources
- Learn more about Dash: https://dash.plot.ly
- View the original component boilerplate: https://github.com/plotly/dash-component-boilerplate
