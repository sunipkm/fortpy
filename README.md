# Example: Python Bindings for FORTRAN
This example illustrates building a FORTRAN loadable module using `f2py` from `numpy`.
The build system used is `meson` and `ninja`, which makes this compatible with Python 3.12 onward.

### To build
```sh
$ pip install . --config-settings=builddir=build
```
The above command will build the project, with build files in `./build` which is useful
for debugging. Remove the `--config-settings` option if not debugging.

### To test
```sh
$ python test.py
```