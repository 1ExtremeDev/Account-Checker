"""

AUTHOR: ExtremeDev
INSTAGRAM: @extremedevalt
Date: 17/03/2020

"""

from os import stat
import random
from pyfiglet import Figlet
import shutil
config = {
    "title": "Regrix",
    "author": "ExtremeDev",
    "version": "alpha"
}

messages = [
    "message1",
    "message2",
    "message3",
    "message4"
]

class Information:
    @staticmethod
    def print_half(text):
        if str(type(text)).__contains__('pyfiglet.FigletString'):
            columns = shutil.get_terminal_size().columns
            for each in str(text).split('\n'):
                print(each.center(columns))
        else:
            columns = shutil.get_terminal_size().columns
            print(text.center(columns))
    @staticmethod
    def title():
        return Figlet(font='standard').renderText(config['title'])

    @staticmethod
    def author():
        return config['author']

    @staticmethod
    def version():
        return str(config['version'])

    @staticmethod
    def information():
        return str(random.choice(messages))
