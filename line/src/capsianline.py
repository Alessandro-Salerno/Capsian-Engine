import Capsian
from   Capsianline.commands.command import Command


class Line(Command):
	def __str__(self) -> str:
		return "line"

	def clear(self):
		import os
		os.system("cls" if os.name == "nt" else "clear")

	def exit(self):
		exit(0)


	def github(self):
		import os
		
		Capsian.Log.warning("The contents of this repostory may be outdated!")
		os.system("https://github.com/Carpall/capsianline")


__linecommand__ = Line()
