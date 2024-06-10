"""Demo package for live course"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pyadv-coursetc98")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Tadeas Cervik"
__email__ = "tadeas.cervik@gmail.com"

from . import algos
