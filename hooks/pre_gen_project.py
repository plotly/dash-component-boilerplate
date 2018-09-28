from __future__ import print_function
import sys

full_name = '{{cookiecutter.full_name}}'
email = '{{cookiecutter.email}}'


def verify(variable_name, s):
    if '(For package.json)' in s:
        print('\nInvalid {}: {}\n'.format(variable_name, s),
              file=sys.stderr)
        sys.exit(-1)


for name, value in (('full_name', full_name), ('email', email)):
    verify(name, value)

sys.exit(0)
