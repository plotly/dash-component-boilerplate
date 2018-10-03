def test_render_component(dash_app, percy_snapshot):
    app = dash_app('usage.py')

    percy_snapshot('{{cookiecutter.project_name}} usage.py')
