from __future__ import print_function
import sys

full_name = '{{cookiecutter.author_name}}'
email = '{{cookiecutter.author_email}}'


def verify(variable_name, s):
    if '(For package.json)' in s:
        print('\nInvalid {}: {}\n'.format(variable_name, s),
              file=sys.stderr)
        sys.exit(-1)


for name, value in (('author_name', full_name), ('author_email', email)):
    verify(name, value)

sys.exit(0)
