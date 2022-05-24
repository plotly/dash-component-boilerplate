from __future__ import print_function
import sys
import re

full_name = '{{cookiecutter.author_name}}'
email = '{{cookiecutter.author_email}}'
project_shortname = '{{cookiecutter.project_shortname}}'

invalid_package_message = 'Invalid {variable}: {value}'
project_shortname_message = '''
({variable}={value}) should be a valid Python package name.

Only lowercase letters, numbers, and `_` are allowed, and the name must start with a non-numeric character. 
'''


def verify(check, variable_name, value, message):
    if check(value):
        print(message.format(variable=variable_name, value=value),
              file=sys.stderr)
        sys.exit(-1)


def package_check(s):
    return '(For package.json)' in s

def check_specials_characters(s):
    pattern = re.compile("^[a-z_][a-z_0-9]*")
    return not pattern.fullmatch(s)

for values in (
    (package_check, 'author_name', full_name, invalid_package_message),
    (package_check, 'author_email', email, invalid_package_message),
    (check_specials_characters, 'project_shortname',
     project_shortname, project_shortname_message)
):
    verify(*values)


sys.exit(0)
