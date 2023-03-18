# -*- coding: utf-8 -*-
import importlib
import sys
import traceback

__author__ = 'Dmitry Petrov'
__email__ = 'e2m3x4@mail.ru'
__version__ = '0.1.1'

try:
    # from . import patches
    # for _, f in patches.__dict__.items():
    #     if callable(f):
    #         f()
    from .cli import cli

except Exception as ex:
    print("Exception in user code:")
    print("-" * 30)
    traceback.print_exc(file=sys.stdout)
    print("-" * 30)

__all__ = ['cli']
