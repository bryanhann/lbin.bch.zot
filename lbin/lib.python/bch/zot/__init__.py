#!/usr/bin/env python3
import sys
from pathlib import Path
import traceback

from bch.zot.util import mod4path

class ZotExc(Exception): pass
class BadXpath(ZotExc): pass
class BadBpath(ZotExc): pass
class BadZpath(ZotExc): pass
class BadImport(ZotExc): pass

class Zot:
    def __init__(self, path):
        self._path = Path(path)
        self._exc_info=sys.exc_info()

    @property
    def path(self): return self._path
    @property
    def bpath(self): return self.path/'.bch'
    @property
    def zpath(self): return self.bpath/'zot.py'


    #@property
    def module(self):
        if not self.path.is_dir():   raise BadXpath
        if not self.bpath.is_dir():  raise BadBpath
        if not self.zpath.is_file(): raise BadZpath
        try:
            self._exc_info=sys.exc_info()
            return mod4path(self.zpath)
        except:
            self._exc_info=sys.exc_info()
            raise BadImport

    def more(self):
        try:
            return list( self.module().more() )
        except ZotExc:
            return []
    def rmore(self):
        for xx in self.more():
            yield xx
            yield from Zot(xx).rmore()

