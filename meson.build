# SPDX-FileCopyrightText: 2023 Sunip K. Mukherjee
#
# SPDX-License-Identifier: Apache-2.0

project('fortpy', 'c',
  version : '1.0',
  license: 'BSD-3',
  meson_version: '>=0.64.0',
  default_options : ['warning_level=2'],
)

add_languages('fortran')

py_mod = import('python')
py = py_mod.find_installation(pure: false)
py_dep = py.dependency()

incdir_numpy = run_command(py,
  [
    '-c',
    'import numpy; print(numpy.get_include())'
  ],
  check: true
).stdout().strip()

incdir_f2py = run_command(py,
    ['-c', 'import numpy.f2py; print(numpy.f2py.get_include())'],
    check : true
).stdout().strip()

fortran_srcs = [
  'src/FORTRAN/singrid.f90', 
]

fortpy_source = custom_target('fortranmodule.c',
  input : fortran_srcs,
  output : ['fortranmodule.c', 
            'fortran-f2pywrappers.f', 
            # 'fortran-f2pywrappers2.f90' # enable when needed
          ],
  command : [py, '-m', 'numpy.f2py', '@INPUT@', '-m', 'fortran', '--lower']
)

py.install_sources(
    'src/fortpy/__init__.py',
    subdir: 'fortpy',
    pure: false,
)


inc_np = include_directories(incdir_numpy, incdir_f2py)

py.extension_module('fortran',
  fortran_srcs + [fortpy_source],
  incdir_f2py / 'fortranobject.c',
  include_directories: inc_np,
  dependencies : py_dep,
  install : true,
  subdir: 'fortpy'
)