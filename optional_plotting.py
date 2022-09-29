## tests/conftest.py
import pytest

def pytest_addoption(parser):
    parser.addoption('--plot', action='store_true', help='Show plots', default=False)


@pytest.fixture
def plot(pytestconfig):
    return pytestconfig.getoption('plot')

## In your test
import xarray as xr
import matpotlib.pyplot as plt

def test_read_signal(plot):
    d = xr.open_dataset('somedata.nc')
    assert len(d.z) == 1024

    if plot:
        plt.figure()
        plt.plot(d.z)
        plt.show()


