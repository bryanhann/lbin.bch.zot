#!/usr/bin/env python3

import pytest

from bch.zot import BadXpath, BadBpath, BadZpath, BadImport

def test_badX(ZOTS):
    with pytest.raises( BadXpath ):
        (ZOTS.badX).module()
    assert (ZOTS.badX)
def test_badB(ZOTS):
    with pytest.raises(BadBpath):
        (ZOTS.badB).module()
def test_badZ(ZOTS):
    with pytest.raises(BadZpath):
        (ZOTS.badZ).module()
def test_badI(ZOTS):
    with pytest.raises(BadImport):
        (ZOTS.badI).module()

def test_good(ZOTS):
    (ZOTS.good).module()
def test_dvd(ZOTS):
    (ZOTS.dvd).module()
def test_movies(ZOTS):
    (ZOTS.movies).module()
