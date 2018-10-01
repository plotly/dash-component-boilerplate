import json
import os


def test_package_json(cookies):
    result = cookies.bake(extra_context={
        'install_dependencies': False,
        'project_name': 'Test Component',
        'full_name': 'test',
        'email': 'test@example.com'
    })

    package_json = json.loads(result.project.join('package.json').read())

    assert package_json['name'] == 'test_component'
    assert package_json['license'] == 'MIT'
    assert os.path.join('venv', 'Scripts', 'python')\
        in package_json['scripts']['build:py']
