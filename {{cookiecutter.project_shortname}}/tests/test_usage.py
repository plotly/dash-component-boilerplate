import time


# Basic test for the component rendering.
def test_render_component(dash_app, selenium):
    # Start a dash app contained in `usage.py`
    # dash_app is a fixture by pytest-dash
    # It will load a py file containing a Dash instance named `app`
    # and start it in a thread.
    app = dash_app('usage.py')

    # Get the generated component input with selenium
    # The html input will be a children of the #input dash component
    my_component = selenium.find_element_by_css_selector('#input > input')

    # Send keys to the custom input.
    my_component.send_keys('Hello dash')

    # Sleep for the output callback to complete.
    time.sleep(1)

    # Get the output component.
    output = selenium.find_element_by_id('output')

    # assert the text has changed
    assert output.text == 'You have entered Hello dash'

