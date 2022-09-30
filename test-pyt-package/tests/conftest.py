import pytest

def pytest_addoption(parser):
    parser.addoption('--plot', action='store_true', help='Show plots', default=False)


@pytest.fixture
def plot(pytestconfig):
    return pytestconfig.getoption('plot')


@pytest.fixture
def norkyst():
    import xarray as xr
    return xr.open_dataset('https://thredds.met.no/thredds/dodsC/sea/norkyst800m/1h/aggregate_be')
