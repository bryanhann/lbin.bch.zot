#!/usr/bin/env python3
from pathlib import Path
import pytest
from bch.zot import  Zot
import bch.zot as Z
from bch.zot import BadXpath, BadBpath, BadZpath, BadImport

def test_raw_good(ZOTS,PATHS): assert list(  (ZOTS.good).module().more() ) == PATHS.good_more
def test_raw_dvd (ZOTS,PATHS): assert list(  (ZOTS.dvd ).module().more() ) == PATHS.dvd_more

def test_badX   (ZOTS, PATHS): assert (ZOTS.badX)   .more() == []
def test_badB   (ZOTS, PATHS): assert (ZOTS.badB)   .more() == []
def test_badZ   (ZOTS, PATHS): assert (ZOTS.badZ)   .more() == []
def test_badI   (ZOTS, PATHS): assert (ZOTS.badI)   .more() == []
def test_iso    (ZOTS, PATHS): assert (ZOTS.iso)    .more() == []
def test_foo    (ZOTS, PATHS): assert (ZOTS.foo)    .more() == []
def test_vcd    (ZOTS, PATHS): assert (ZOTS.vcd)    .more() == []
def test_good   (ZOTS, PATHS): assert (ZOTS.good)   .more() == PATHS.good_more
def test_dvd    (ZOTS, PATHS): assert (ZOTS.dvd)    .more() == PATHS.dvd_more
def test_movies (ZOTS, PATHS): assert (ZOTS.movies) .more() == PATHS.movies_more



'''

def test__badMissing_raises_MissingFile(PATHS,ZOTS):
    with pytest.raises( Zot.MissingFile ):
        (ZOTS.badMissing).module
def test__badImport_raises_CannotImport(ZOTS):
    print( (ZOTS.badImport.path/'.bch/zot.py').is_dir() )
    (ZOTS.badImport).module
    #assert  Zot.MissingFile
    #with pytest.raises( Zot.CannotImport ):
    #    (ZOTS.badImport).module

#def test__zot_badAttrib__raises_AttributeError(PATHS,ZOTS):
#    with pytest.raises( AttributeError ):
#        (ZOTS.badAttrib).module.more()


def test_ZotGood_raises_no_exception(PATHS,ZOTS):
    (ZOTS.good).module

def test_good_module_more(ZOTS,PATHS):
    assert list( (ZOTS.good).module.more() ) == PATHS.good_morelist

def test_good_more(ZOTS,PATHS):
    assert list( (ZOTS.good).more() ) == PATHS.good_morelist

def test_bad_more(ZOTS,PATHS):
    assert ZOTS.badMissing.more() == []
'''

