import os
import tempfile

_package_dir = os.path.join(tempfile.gettempdir(), '.gitimport', 'packages')
if 'GITIMPORT_TEMPCOPY_DIR' in os.environ:
    _package_dir = os.environ['GITIMPORT_TEMPCOPY_DIR']

config = {
    'package_dir': _package_dir
}
"""
The config dictionary contains global configuration values for gitimport.

The config is defined in ``gitimport/__init__.py``. Values can be overwridden in two
ways: either by manually setting dictionary keys, or by setting environment variables.

Keys in the config dictionary:

``package_dir``
    The absolute path to a directory where `gitimport.package` stores
    copies of packages. The default value is set to 
    `tempfile.gettempdir()/.gitimport/packages`, and the value can be overwritten by 
    setting the `GITIMPORT_TEMPCOPY_DIR` environment variable.
"""