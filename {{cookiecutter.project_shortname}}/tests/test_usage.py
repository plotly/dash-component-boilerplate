# Basic test for the component rendering.
def test_render_component(dash_app, selenium):
    # Start a dash app contained in `usage.py`
    app = dash_app('usage.py')

    # Get the generated component with selenium
    my_component = selenium.find_element_by_id('input')
