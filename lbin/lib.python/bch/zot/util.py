#!/usr/bin/env python3
import importlib.util
def mod4path(path):
    name='anonymoose'
    path=str(path)
    spec = importlib.util.spec_from_file_location(name, path)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo
