from os import system


print("Starting Capsian Preparation Tool...")
print("This script will install all the dependencies you need")
input("Press enter to continue or lcose to terminate ")

system("pip install pyglet==1.5.6")
system("pip install PyOpenGL")
system("pip install pyinstaller")

input("Installation completed!\nPress enter to exit ")
