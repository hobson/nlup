# Copyright (C) 2014-2015 Kyle Gorman
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# decorators.py: decorators for library
import sys
exit = sys.exit

from functools import wraps

import logging


def listify(gen):
    """
    Converts a generator into a function which returns a list.
    """
    @wraps(gen)
    def patched(*args, **kwargs):
        return list(gen(*args, **kwargs))
    return patched


def reversify(fnc):
    """
    Converts a function (or generator) which returns an iterable to one
    which returns that as a reversed list. This is done by casting the
    iterable to a list (which evaluates it, in the case it's a generator)
    and then reversing it in place.
    """
    @wraps(fnc)
    def patched(*args, **kwargs):
        retval = list(fnc(*args, **kwargs))
        retval.reverse()
        return retval
    return patched


def tupleify(gen):
    """
    Converts a generator into a function which returns a set.
    """
    @wraps(gen)
    def patched(*args, **kwargs):
        return tuple(gen(*args, **kwargs))
    return patched


def setify(gen):
    """
    Converts a generator into a function which returns a set.
    """
    @wraps(gen)
    def patched(*args, **kwargs):
        return set(gen(*args, **kwargs))
    return patched


def frozensetify(gen):
    """
    Converts a generator into a function which returns a frozenset.
    """
    @wraps(gen)
    def patched(*args, **kwargs):
        return frozenset(gen(*args, **kwargs))
    return patched


def meanify(gen):
    """
    Converts. a generator of numbers to one which returns the mean value,
    iteratively computed to avoid overflow. This algorithm is recommended
    in AoCP (2.4.2.2).
    """
    @wraps(gen)
    def patched(*args, **kwargs):
        avg = 0
        for (i, val) in enumerate(gen(*args, **kwargs), 1):
            avg += (val - avg) / i
        return avg
    return patched


def IO(fnc):
    """
    Converts a function which may throw an IOError to one which logs the
    error and quits, if it arises.
    """
    @wraps(fnc)
    def patched(*args, **kwargs):
        try:
            return fnc(*args, **kwargs)
        except IOError as err:
            logging.error(err)
            exit(1)
    return patched
