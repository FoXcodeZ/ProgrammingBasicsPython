from termcolor import colored
import platform

print(f"Hello world - {colored('Marcin', 'blue')} - Python version: {colored(platform.python_version(), 'red')}")