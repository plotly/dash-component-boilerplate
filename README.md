# Dash Component Boilerplate

This repository contains the minimal set of code required to create your own custom Dash component.

To create your own Dash component:

1. Fork this repo
2. Find-and-replace:
    1. `my_dash_component` with your component library name.
    2. `my-dash-component` with your component library name.
    3. `my-name` with your name and `my-email` with your email address
    4. `my-license` with your license (e.g. `MIT`)
    5. Rename the folder `my_dash_component/` with your component library name
3. Install the dependencies:

    ```
    npm install
    ```

4. Open up the JavaScript demo environment:

    ```
    npm run start
    ```

5. Write your component code in `src/lib/components`. There is a sample component called `ExampleComponent.react.js` that you can use for inspiration. The demo app is in `src/demo` and you will import your example component code into your demo app.

6. Add custom styles to your component by putting your custom CSS files into your distribution folder (`my_dash_component`) and making sure that they are referenced in `MANIFEST.in` so that they get properly included when you're ready to publish your component.

7. Test your code in a Python environment:
    1. Build your code
        ```
        npm run build:js-dev
        npm run build:py
        ```
    2. Run and modify the `usage.py` sample dash app:
        ```
        python usage.py
        ```
8. [Review your code](checklist.md)
9. <span id="publishing">Create a production build and publish</span>

    1. Build your code:

        ```
        npm run build:js
        npm run build:py
        ```

    2. Create a Python tarball

        ```
        python setup.py sdist
        ```

        This distribution tarball will get generated in the `dist/` folder

    3. Test your tarball by copying it into a new environment and installing it locally:

        ```
        pip install my_dash_component-0.0.1.tar.gz
        ```

    4. Choose how you'd like to serve your library's CSS and JS (locally or via npm):

        By default, Dash serves the component library's CSS and JS from the remote unpkg CDN. Publishing your component to NPM will make the JavaScript bundles available there. To publish to npm:

        ```
        npm run publish
        ```

        If you choose not publish the component's package to NPM you'll need to set the `serve_locally` flags in `usage.py` to `True`. We will eventually make `serve_locally=True` the default, [follow our progress in this issue](https://github.com/plotly/dash/issues/284).

    5. Publish your component to PyPI:

        ```
        twine upload dist/dash_component-0.0.1.tar.gz
        ```

10. [Share your component with the community!](https://community.plot.ly/c/dash)

# More Resources

-   Learn more about Dash: https://dash.plot.ly
-   View the original component boilerplate: https://github.com/plotly/dash-component-boilerplate

Watch the [component boilerplate repository](https://github.com/plotly/dash-component-boilerplate) to stay informed of changes to our components.
