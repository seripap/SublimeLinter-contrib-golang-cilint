#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Alec Thomas
# Copyright (c) 2014 Alec Thomas
#
# License: MIT
#

"""This module exports the Gometalinter plugin class."""

from SublimeLinter.lint import Linter, highlight, util


class GolangCILint(Linter):
    """Provides an interface to golangci-lint."""

    cmd = 'golangci-lint run --fast --enable typecheck'
    regex = r'(?:[^:]+):(?P<line>\d+):(?P<col>\d+)?:?\s*(?P<message>.*)'
    error_stream = util.STREAM_BOTH
    default_type = highlight.ERROR
    defaults = {
        'selector': 'source.go'
    }
