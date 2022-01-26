import os

print("Starting Capsian Preparation Tool...")
print("This script will install all the dependencies you need")
input("Press enter to continue or lcose to terminate ")

_pip_type = "pip"
if os.name == "posix":
    _pip_type = "pip3"

os.system(_pip_type + " install pyglet==1.5.6")
os.system(_pip_type + " install PyOpenGL")
os.system(_pip_type + " install pyinstaller")

input("Installation completed!\nPress enter to exit ")
