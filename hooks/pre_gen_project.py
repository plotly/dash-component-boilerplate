from __future__ import print_function
import sys

full_name = '{{cookiecutter.author_name}}'
email = '{{cookiecutter.author_email}}'
project_shortname = '{{cookiecutter.project_shortname}}'

invalid_package_message = 'Invalid {variable}: {value}'
project_shortname_message = '''
({variable}={value}) should be a valid Python package name.

Only lowercase letters and `_` are allowed.
'''


def verify(check, variable_name, value, message):
    if check(value):
        print(message.format(variable=variable_name, value=value),
              file=sys.stderr)
        sys.exit(-1)


def package_check(s):
    return '(For package.json)' in s


def _check_specials_characters(s):
    i = ord(s)
    if i == 95:
        # Allow for `_`
        return False
    return not 96 < i < 123


def check_specials_characters(s):
    return any(_check_specials_characters(x) for x in s)


for values in (
    (package_check, 'author_name', full_name, invalid_package_message),
    (package_check, 'author_email', email, invalid_package_message),
    (check_specials_characters, 'project_shortname',
     project_shortname, project_shortname_message)
):
    verify(*values)


sys.exit(0)
