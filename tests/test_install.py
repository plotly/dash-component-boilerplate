import os
import shutil
import sys

from dash.testing.application_runners import import_app


def test_install(cookies, dash_duo):
    results = cookies.bake(extra_context={
        'project_name': 'Test Component',
        'author_name': 'test',
        'author_email': 'test',
        'jl_prefix': 'dash',
        'r_prefix': 'dash',
    })

    # Add the generated project to the path so it can be loaded from usage.py
    # It lies somewhere in a temp directory created by pytest-cookies
    sys.path.insert(0, str(results.project))

    # Test that `usage.py` works after building the default component.
    app = import_app('usage')
    dash_duo.start_server(app)

    my_component = dash_duo.find_element('#input > input')
    assert 'my-value' == my_component.get_attribute('value')

    dash_duo.clear_input(my_component)
    my_component.send_keys('Hello dash')
    dash_duo.wait_for_text_to_equal('#output', 'You have entered Hello dash')

    # Check for the existence of the right autogenerated files (R etc)
    # We'll leave their contents to other tests at least for now,
    # but existence tests verify that we can make the right directories
    # on a clean installation.

    expected_files = [
        # base cookiecutter
        ['README.md'],
        ['package.json'],
        ['LICENSE'],
        # Py
        ['test_component', '__init__.py'],
        ['test_component', '_imports_.py'],
        ['test_component', 'TestComponent.py'],
        ['test_component', 'test_component.min.js'],
        ['test_component', 'test_component.min.js.map'],
        ['test_component', 'package-info.json'],
        ['test_component', 'metadata.json'],
        # R
        ['DESCRIPTION'],
        ['NAMESPACE'],
        ['R', 'dashTestComponent.R'],
        ['R', 'internal.R'],
        ['man', 'dashTestComponent.Rd'],
        ['inst', 'deps', 'test_component.min.js'],
        ['inst', 'deps', 'test_component.min.js.map'],
        # Julia
        ['Project.toml'],
        ['deps', 'test_component.min.js'],
        ['deps', 'test_component.min.js.map'],
        ['src', 'jl', 'dash_testcomponent.jl'],
        ['src', 'TestComponent.jl'],
    ]

    for path in expected_files:
        path_str = str(results.project.join(*path))
        assert os.path.exists(path_str), path_str

    node_modules = str(results.project.join('node_modules'))

    if sys.platform == 'win32':
        # Fix delete long names on Windows.
        # pytest-cookies have trouble deleting some file generated by webpack.
        node_modules = '\\\\?\\' + node_modules

    shutil.rmtree(node_modules)
