import sys, os
from cx_Freeze import setup, Executable

__version__ = "1.1.0"

include_files = []
excludes = []
packages = ["os", "urllib.request", "requests","time","genanki","bs4","idna","json","base64"]

setup(
    name = "appname",
    description='App Description',
    version=__version__,
    options = {"build_exe": {
    'packages': packages,
    'include_files': include_files,
    'excludes': excludes,
    'include_msvcr': True,
}},
executables = [Executable("Main.py",base="Console")]
)