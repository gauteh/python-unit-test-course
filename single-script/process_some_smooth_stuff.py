import xarray as xr
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import pytest

def smooth(F, d=3):
    """
    Smooth F with mean of size `d`.
    """
    assert len(F.shape) == 2, "Input array must be 2d"
    mask = np.ones((d, d)) / (d*d)
    F = signal.convolve2d(F, mask, mode='same', boundary='wrap')

    return F

def faulty_smooth(F, d=3):
    F = 2. * F  # subtle.
    return F

def main():
    print("I'm main!")

    ds = xr.open_dataset('https://thredds.met.no/thredds/dodsC/sea/norkyst800m/1h/aggregate_be')
    print(ds)

if __name__ == "__main__":
    main()

def test_smooth_const_almost():
    F = np.ones((10, 10))
    sF = smooth(F)
    assert F.shape == sF.shape
    np.testing.assert_almost_equal(F, sF)

@pytest.mark.xfail
def test_smooth_const_exactly():
    F = np.ones((10, 10))
    sF = smooth(F)
    np.testing.assert_equal(F, sF)

def test_load_data():
    ds = xr.open_dataset('https://thredds.met.no/thredds/dodsC/sea/norkyst800m/1h/aggregate_be')
    print(ds)

@pytest.mark.xfail
def test_faulty_smooth_w():
    ds = xr.open_dataset('https://thredds.met.no/thredds/dodsC/sea/norkyst800m/1h/aggregate_be')
    v = ds.v[32, 4, :, :]
    print(v.values[:])
    vS = faulty_smooth(v, d=15)

    assert np.nanvar(vS) < np.nanvar(v), "Variance of smoothed field should be less than original."

def test_smooth_w(plot):
    ds = xr.open_dataset('https://thredds.met.no/thredds/dodsC/sea/norkyst800m/1h/aggregate_be')
    v = ds.v[32, 4, :, :]
    print(v.values[:])
    vS = smooth(v, d=15)

    assert np.nanvar(vS) < np.nanvar(v), "Variance of smoothed field should be less than original."

    if plot:
        plt.figure()
        plt.imshow(v)
        plt.figure()
        plt.imshow(vS)
        plt.show()

