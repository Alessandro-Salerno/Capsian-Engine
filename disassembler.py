import dis

file = open("KeyFire/video/camera.py", "r")
text = file.read()
file.close()
code = compile(source=text, filename="camera.py", mode="exec", optimize=1)

dis.dis(code)