
import sys
from cx_Freeze import setup, Executable


build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="MPM-UN",
    version="0.5.7",
    description="App mpm unal!",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
)