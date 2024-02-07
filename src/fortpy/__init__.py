from .fortran import singrid # pylint: disable=import-error # type: ignore
import numpy as np
import xarray as xr

def sine_grid(x: np.ndarray = None, y: np.ndarray = None) -> xr.Dataset:
    if x is None:
        x = np.linspace(-np.pi, np.pi, 100)
    if y is None:
        y = np.linspace(-np.pi, np.pi, 200)
    # out = np.zeros((len(x), len(y)), dtype=np.float32, order='F') # keep if the output is `intent(inout)` in `singrid.f90`.
    # This can also be packed into a `xarray.Dataset` object, and then passed to `singrid` as `intent(inout)`.
    out = singrid(x, y) # `singrid` is a Fortran subroutine that takes `x` and `y` as input, and returns `out` as output (`intent(out)`).
    ds = xr.Dataset(data_vars={'data': (['x', 'y'], out)}, coords={'x': x, 'y': y})
    # singrid(x, y, ds['data'].values) # This is also possible if `singrid` is modified to accept `intent(inout)` for the third argument.
    return ds

__all__ = ['sine_grid']