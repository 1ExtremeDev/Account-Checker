"""

AUTHOR: ExtremeDev
INSTAGRAM: @extremedevalt
Date: 16/03/2020

"""

from threading import Thread
class ExtremeDev():
    class Threading(Thread):
        def __init__(self, group=None, goto=None, name=None,argumente=(), kwargs={}, Verbose=None):
            Thread.__init__(self, group, goto, name, argumente, kwargs)
            self._return = None
        def run(self):
            if self._target is not None: self._return = self._target(*self._args,**self._kwargs)
        def join(self, *args):
            Thread.join(self, *args)
            return self._return