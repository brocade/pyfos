PyFOS - Prototype code (testing - developer unit test sanity)

env:

    Tested with Python3 (3.5.2) with setuptools
    Ubuntu 16.04.3 LTS

installation:

    1) create library directories
    mkdir ~<login>/python_lib
    mkdir ~<login>/python_lib/lib
    mkdir ~<login>/python_lib/lib/python3.5
    mkdir ~<login>/python_lib/lib/python3.5/site-packages

    2) set env variable for library directory
    setenv PYTHONPATH ~<login>/python_lib/lib/python3.5/site-packages

    3) install pyfos modules into the library path
    cd <pyfos directory>
    python3 setup.py install --prefix=~<login>/python_lib

HTML based documentation.

    HTML files are created under <pyfos directory>/docs/documentations/html. use index.html
    as the starting point.

Uninstall:

    if library path is used for pyfos & dependencies only - remove the directory as a whole
    if library path is used by other modules also - remove pyfos & dependencies manually

Contact:

    automation@brocade.com
