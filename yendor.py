#!/usr/bin/python3
"""The start and end of yendor"""
import atexit
from yendor import core

core.main()


def onclose(self):
    """sets the existing results to nil"""
    self.result_string = ""


atexit.register(onclose)
