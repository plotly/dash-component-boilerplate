# Basic test for the component rendering.
def test_render_component(dash_app, selenium):
    # Start a dash app contained in `usage.py`
    # dash_app is a fixture by pytest-dash
    # It will load a py file containing a Dash instance named `app`
    # and start it in a thread.
    app = dash_app('usage.py')

    # Get the generated component with selenium
    my_component = selenium.find_element_by_id('input')
