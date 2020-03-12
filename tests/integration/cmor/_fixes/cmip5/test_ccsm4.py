"""Test fixes for CCSM4."""
import unittest

import numpy as np
from iris.coords import DimCoord
from iris.cube import Cube

from esmvalcore.cmor._fixes.cmip5.ccsm4 import Cl, Rlut, Rlutcs, So
from esmvalcore.cmor._fixes.common import ClFixHybridPressureCoord
from esmvalcore.cmor.fix import Fix


def test_get_cl_fix():
    """Test getting of fix."""
    fix = Fix.get_fixes('CMIP5', 'CCSM4', 'Amon', 'cl')
    assert fix == [Cl(None)]


def test_cl_fix():
    """Test fix for ``cl``."""
    assert Cl(None) == ClFixHybridPressureCoord(None)


class TestsRlut(unittest.TestCase):
    """Test for rlut fixes."""

    def setUp(self):
        """Prepare tests."""
        self.cube = Cube([1.0, 2.0], var_name='rlut')
        self.cube.add_dim_coord(
            DimCoord([0.50001, 1.499999],
                     standard_name='latitude',
                     bounds=[
                         [0.00001, 0.999999],
                         [1.00001, 1.999999],
                     ]), 0)
        self.fix = Rlut(None)

    def test_get(self):
        """Test fix get."""
        self.assertListEqual(Fix.get_fixes('CMIP5', 'CCSM4', 'Amon', 'rlut'),
                             [Rlut(None)])

    def test_fix_metadata(self):
        """Check that latitudes values are rounded."""
        cube = self.fix.fix_metadata([self.cube])[0]

        latitude = cube.coord('latitude')
        self.assertTrue(np.all(latitude.points == np.array([0.5000, 1.5000])))
        self.assertTrue(
            np.all(latitude.bounds == np.array([[0.0000, 1.0000],
                                                [1.0000, 2.0000]])))


class TestsRlutcs(unittest.TestCase):
    """Test for rlutcs fixes."""

    def setUp(self):
        """Prepare tests."""
        self.cube = Cube([1.0, 2.0], var_name='rlutcs')
        self.cube.add_dim_coord(
            DimCoord([0.50001, 1.499999],
                     standard_name='latitude',
                     bounds=[
                         [0.00001, 0.999999],
                         [1.00001, 1.999999],
                     ]), 0)
        self.fix = Rlutcs(None)

    def test_get(self):
        """Test fix get."""
        self.assertListEqual(Fix.get_fixes('CMIP5', 'CCSM4', 'Amon', 'rlutcs'),
                             [Rlutcs(None)])

    def test_fix_metadata(self):
        """Check that latitudes values are rounded."""
        cube = self.fix.fix_metadata([self.cube])[0]

        latitude = cube.coord('latitude')
        self.assertTrue(np.all(latitude.points == np.array([0.5000, 1.5000])))
        self.assertTrue(
            np.all(latitude.bounds == np.array([[0.0000, 1.0000],
                                                [1.0000, 2.0000]])))


class TestSo(unittest.TestCase):
    """Tests for so fixes."""

    def setUp(self):
        """Prepare tests."""
        self.cube = Cube([1.0, 2.0], var_name='so', units='1.0')
        self.fix = So(None)

    def test_get(self):
        """Test fix get."""
        self.assertListEqual(Fix.get_fixes('CMIP5', 'CCSM4', 'Amon', 'so'),
                             [So(None)])

    def test_fix_metadata(self):
        """Checks that units are changed to the correct value."""
        cube = self.fix.fix_metadata([self.cube])[0]
        self.assertEqual('1e3', cube.units.origin)
