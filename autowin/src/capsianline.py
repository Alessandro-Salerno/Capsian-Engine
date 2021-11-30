import Capsian
from   Capsianline.commands.command import Command


def get_string(width, height, vsync):
	return """
{
	"Window": {
		"Width": ___WIDTH___,
		"Height": ___HEIGHT___,
		"VSync": ___VSYNC___
	},

	"Camera": {
		"Position": [0, 0, 0],
		"Rotation": [0, 0, 0],
		"Field of View": 90,
		"Draw Distance": 3000
	}
}
""".replace("___WIDTH___", width).replace("___HEIGHT___", height).replace("___VSYNC___", str(vsync).lower())


class Autowin(Command):
	def __str__(self) -> str:
		return "autowin"

	def __repr__(self) -> str:
		return """
AUTOWIN
-------
This command helps you interact with the autowin package.
"""

	def setup(self, width=1280, height=720, vsync=False):
		with open("autowin.json", "w") as file:
			file.write(get_string(width, height, vsync))
			Capsian.Log.successful(f"Created Windows Setup file with RES:{width}x{height} VSYNC:{vsync}")


__linecommand__ = Autowin()
