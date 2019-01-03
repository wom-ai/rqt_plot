#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['sbgc_plot', 'sbgc_plot.data_plot'],
    package_dir={'': 'src'},
    scripts=['scripts/sbgc_plot']
)

setup(**d)
