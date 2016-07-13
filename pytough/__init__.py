from os.path import dirname, basename, isfile
import glob

# get all `.py` files
modules = glob.glob(dirname(__file__)+'/*.py')

# list all `.py` files in `__all__`
# basename(f)[:-3]: remove extension name `.py`
__all__ = [basename(f)[:-3] for f in modules if isfile(f)]

# make submodules to be available using
from . import *
