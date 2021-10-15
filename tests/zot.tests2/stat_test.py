#!/usr/bin/env python3
import pytest
import bch.zot as Z
def _stat(zot): return [ zot.path.is_dir(), zot.bpath.is_dir(), zot.zpath.is_file(), ]
def test_badX(ZOTS): assert _stat(ZOTS.badX) == [ False, False, False ]
def test_badB(ZOTS): assert _stat(ZOTS.badB) == [ True,  False, False ]
def test_badZ(ZOTS): assert _stat(ZOTS.badZ) == [ True,  True,  False ]
def test_badI(ZOTS): assert _stat(ZOTS.badI) == [ True,  True,  True  ]
def test_dvd (ZOTS): assert _stat(ZOTS.dvd) == [ True,  True,  True  ]
def test_movies (ZOTS): assert _stat(ZOTS.movies) == [ True,  True,  True  ]
