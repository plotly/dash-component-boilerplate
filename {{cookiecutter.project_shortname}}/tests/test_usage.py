import time

from pytest_dash.utils import import_app


# Basic test for the component rendering.
def test_render_component(dash_threaded, selenium):
    # Start a dash app contained in `usage.py`
    # dash_threaded is a fixture by pytest-dash
    # It will load a py file containing a Dash instance named `app`
    # and start it in a thread.
    app = import_app('usage.py')
    dash_threaded(app)

    # Get the generated component input with selenium
    # The html input will be a children of the #input dash component
    my_component = selenium.find_element_by_css_selector('#input > input')

    assert 'my-value' == my_component.get_attribute('value')

    # Clear the input
    my_component.clear()

    # Send keys to the custom input.
    my_component.send_keys('Hello dash')

    # Wait for the output callback to complete.
    time.sleep(1)

    # Get the output component.
    output = selenium.find_element_by_id('output')

    # assert the text has changed
    assert output.text == 'You have entered Hello dash'
