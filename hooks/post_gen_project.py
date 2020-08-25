from __future__ import print_function

import shlex
import sys
import os
import subprocess

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


if install_deps != 'True':
    print('`install_dependencies` is false!!', file=sys.stderr)
    print('Please create a venv in your project root'
          ' and install the dependencies in requirements.txt',
          file=sys.stderr)
    sys.exit(0)

# Create a virtual env
if sys.version.split(' ')[0] > '3.2':
    venv = '{} -m venv venv'.format(sys.executable)
else:
    venv = 'virtualenv venv'

# noinspection PyBroadException
try:
    _execute_command(venv)
except BaseException:
    print(
        '''
        venv creation failed.
        Make sure you have installed virtualenv on Python 2.
        ''',
        file=sys.stderr
    )
    raise

print('\n\nInstalling dependencies\n', file=sys.stderr)

# Install Python requirements.
_execute_command(
    r'{} -m pip install -r requirements.txt'.format(python_executable)
)

# Install node_modules
_execute_command('npm install --ignore-scripts')

# Run the first build
print('Building initial bundles...')

_execute_command('npm run build:js')

# Activating the venv and running the command
# doesn't work on Linux with subprocess.
# The command needs to run in the venv we just created to use the dash cmd.
# But it also needs shell to be true for the command to work.
# And shell doesn't work with `npm run` nor `. venv/bin/activate`
# The command works in a terminal.
_execute_command("{} -m dash.development.component_generator"
                 " ./src/lib/components"
                 " {{cookiecutter.project_shortname}}"
                 " -p package-info.json"
                 " --jl-prefix '{{ cookiecutter.jl_prefix }}'"
                 " --r-prefix '{{ cookiecutter.r_prefix }}'"
                 .format(python_executable))

print('\n{} ready!\n'.format(project_shortname))

sys.exit(0)
