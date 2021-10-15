#!/usr/bin/env python3
from pathlib import Path


def test_good_rmore(ZOTS,PATHS):
    aa=list(ZOTS.good.rmore())
    assert aa == PATHS.good_rmore


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

