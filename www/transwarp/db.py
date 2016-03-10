#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-10 23:13:38
# @Author  : li (erwin.lic@hotmail.com)


import time
import uuid
import functools
import threading
import logging


class Dict(dict):
    """doc string for Dict"""

    def __init__(self, arg):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" key)

    def __setattr__(self, key, value):
        self[key] = value


def next_id(t=None):
	if t is None:
		return 
