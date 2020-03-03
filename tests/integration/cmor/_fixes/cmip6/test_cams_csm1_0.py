"""Test fixes for CAMS-CSM1-0."""
import unittest

from esmvalcore.cmor._fixes.cmip6.cams_csm1_0 import Cl
from esmvalcore.cmor._fixes.fix import Fix


def test_get_cl_fix():
    """Test getting of fix."""
    fix = Fix.get_fixes('CMIP6', 'CAMS-CSM1-0', 'Amon', 'cl')
    assert fix == [Cl(None)]


@unittest.mock.patch(
    'esmvalcore.cmor._fixes.cmip6.cams_csm1_0.BaseCl.fix_metadata',
    autospec=True)
def test_cl_fix_metadata(mock_base_fix_metadata):
    """Test ``fix_metadata`` for ``cl``."""
    fix = Cl(None)
    fix.fix_metadata('cubes')
    mock_base_fix_metadata.assert_called_once_with(fix, 'cubes')