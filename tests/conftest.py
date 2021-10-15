#!/usr/bin/env python3

import pytest
from pathlib import Path
from bch.zot import Zot
#SAMPLES=Path(__file__).parent.parent/'fixtures/SAMPLES'
SAMPLES=Path(__file__).parent/'fixtures/SAMPLES'

class Namespace: pass

@pytest.fixture
def PATHS():
    """Common Paths"""
    xx = Namespace()
    xx.badX   = SAMPLES/'badXpath'
    xx.badB   = SAMPLES/'badBpath'
    xx.badZ   = SAMPLES/'badZpath'
    xx.badI   = SAMPLES/'badImport'
    xx.badA   = SAMPLES/'badAttrib'
    xx.good   = SAMPLES/'good'
    xx.good   = SAMPLES/'good'
    xx.dvd    = xx.good/'dvd'
    xx.iso    = xx.good/'iso'
    xx.foo    = xx.good/'foo'
    xx.vcd    = xx.good/'vcd'
    xx.movies = xx.dvd/'movies'
    xx.upload = xx.movies/'to_upload'
    xx.good_more    = [xx.dvd, xx.foo, xx.iso, xx.vcd]
    xx.dvd_more     = [xx.movies]
    xx.movies_more  = [xx.upload]
    xx.good_rmore   = [xx.dvd, xx.movies, xx.upload, xx.foo, xx.iso, xx.vcd ]
    return xx
@pytest.fixture
def ZOTS(PATHS):
    xx = Namespace()
    for name in dir(PATHS):
        attrib = getattr(PATHS,name)
        if name.startswith('_'): continue
        if type(attrib)==type([]): continue
        setattr(xx,name,Zot(attrib))
    return xx
