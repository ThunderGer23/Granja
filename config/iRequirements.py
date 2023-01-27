# Importing the debug and install modules from the upip package.
from upip import debug as deb
from upip import install

def requirements():
    """
    It checks if the device is running MicroPython, and if so, it installs the urequests module and
    returns it
    :return: The urequests module
    """
    deb = True
    install('urequests')
    import urequests
    return urequests