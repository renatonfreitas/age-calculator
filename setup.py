from sys import platform
from cx_Freeze import setup, Executable

build_exe_options = {
    "includes": ["tkinter", "datetime"]
}

base = None
if platform == 'win32':
    base = "Win32Gui"

setup(
    name="calculator_of_smiile",
    version='1.0',
    description="Practicing tkinter building a calculator",
    options={"build_exe": build_exe_options},
    executables=[
        Executable("age-calculator.py", base=base)
    ]
)