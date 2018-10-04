import shutil
import time
import sys


def test_install(cookies, dash_app, selenium):
    results = cookies.bake(extra_context={
        'project_name': 'Test Component',
        'author_name': 'test',
        'author_email': 'test',
        # 'install_dependencies': False
    })

    # Add the generated project to the path so it can be loaded from usage.py
    sys.path.insert(0, str(results.project))

    dash_app(str(results.project.join('usage.py')))

    selenium.get('http://localhost:8050')
    time.sleep(1)

    input_component = selenium.find_element_by_xpath(
        '//div[@id="input"]/input')
    input_component.clear()
    input_component.send_keys('Hello dash component')

    time.sleep(2)

    output = selenium.find_element_by_id('output')

    assert output.text == 'You have entered Hello dash component'

    node_modules = str(results.project.join('node_modules'))

    if sys.platform == 'win32':
        # Fix delete long names on windows.
        node_modules = '\\\\?\\' + node_modules

    shutil.rmtree(node_modules)

