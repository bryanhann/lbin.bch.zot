#!/usr/bin/env python3
from pathlib import Path
import pytest
from bch.zot import  Zot
import bch.zot as Z
from bch.zot import BadXpath, BadBpath, BadZpath, BadImport

def test_raw_good(ZOTS,PATHS): assert list(  (ZOTS.good).module().more() ) == PATHS.good_more
def test_raw_dvd (ZOTS,PATHS): assert list(  (ZOTS.dvd ).module().more() ) == PATHS.dvd_more

