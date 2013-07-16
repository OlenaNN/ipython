"""
Module with tests for sphinx_howto.py
"""

#-----------------------------------------------------------------------------
# Copyright (c) 2013, the IPython Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

from .base import ExportersTestsBase
from ..sphinx_howto import SphinxHowtoExporter

#-----------------------------------------------------------------------------
# Class
#-----------------------------------------------------------------------------

class Test_SphinxHowtoExporter(ExportersTestsBase):
    """Contains test functions for sphinx_howto.py"""

    def test_constructor(self):
        """
        Can a SphinxHowtoExporter be constructed?
        """
        SphinxHowtoExporter()


    def test_export(self):
        """
        Can a SphinxHowtoExporter export something?
        """
        (output, resources) = SphinxHowtoExporter().from_filename(self._get_notebook())
        assert len(output) > 0