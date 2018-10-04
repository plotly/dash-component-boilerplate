from __future__ import print_function

import shlex
import sys
import os
import subprocess
import json
import collections

import six

install_deps = '{{cookiecutter.install_dependencies}}'
project_shortname = '{{cookiecutter.project_shortname}}'


is_windows = sys.platform == 'win32'

if is_windows:
    python_executable = os.path.join('venv', 'Scripts', 'python')
else:
    python_executable = os.path.join('venv', 'bin', 'python')


def _execute_command(cmd):
    line = shlex.split(cmd, posix=not is_windows)

    print('Executing: {}'.format(cmd))

    # call instead of Popen to get realtime output
    status = subprocess.call(line, shell=is_windows)

    if status != 0:
        print('post_gen_project command failed: {}'.format(cmd),
              file=sys.stderr)
        sys.exit(status)

    return status


# Patch up the package.json to use the venv python for class generation.
# If install_dependencies is false, the venv must be created manually and
# the requirements installed.
print('Patching build command')

with open('package.json', 'r+') as package_file:
    package_json = json.load(package_file,
                             object_pairs_hook=collections.OrderedDict)

    package_json['scripts']['build:py'] \
        = package_json['scripts']['build:py'].replace(
        '%(python_path)', python_executable)

    package_file.seek(0)
    package_file.truncate(0)

    json.dump(package_json, package_file, indent=4)


if install_deps != 'True':
    print('`install_dependencies` is false!!', file=sys.stderr)
    print('Please create a venv in your project root'
          ' and install the dependencies in requirements.txt',
          file=sys.stderr)
    sys.exit(0)

# Create a virtual env
if sys.version.split(' ')[0] > '3.2':
    venv = 'python -m venv venv'
else:
    venv = 'virtualenv venv'

_execute_command(venv)


print('\n\nInstalling dependencies\n', file=sys.stderr)

# Install python requirements.
_execute_command(
   r'{} -m pip install -r requirements.txt'.format(python_executable))

# Install node_modules
_execute_command('npm install')

# Run the first build
print('Building initial bundles...')
_execute_command('npm run build:all')

print('\n{} ready!\n'.format(project_shortname))

sys.exit(0)
