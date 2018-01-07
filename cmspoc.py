# -*- encoding:"utf-8"-*-
from lib.core.data import target, path
from lib.parse.cmdline import cmdLineParser
from lib.core.common import banner
from lib.controllor.task import loadScripts
from lib.controllor.task import runPoc, autoPoc
from lib.controllor.task import start
import requests


def cli():
	try:
		banner()
		target.update(cmdLineParser().__dict__)
		start()
	except requests.exceptions.InvalidSchema as e:
		print("Please input the right url.")
	except requests.exceptions.MissingSchema as e:
		print("Please apply a right schema.e.g:http://www.example.com")
	except requests.exceptions.ConnectionError as e:
		print("The network is busy.Connetion error!")
	except KeyboardInterrupt as e:
		print("User aborted!")

if __name__ == "__main__":
	cli()
