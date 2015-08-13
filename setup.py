#!/usr/bin/env python

from setuptools import setup

setup(name="molmass",
    version="2015.01.29",
    description="Calculate the molecular mass (average, monoisotopic, and nominal), the elemental composition, and the mass distribution spectrum of a molecule given by its chemical formula, relative element weights, or sequence.",
    author="Christoph Gohlke",
    author_email="cgohlke@uci.edu",
    url="https://github.com/dmccloskey/molmass",
    packages=["sequencing_utilities"],
    #entry_points={"console_scripts":
    #            ["makegff = sequencing_utilities.makegff:main",
    #                "sam2bam = sequencing_utilities.sam2bam:main",
    #                "mapped_percentage = sequencing_utilities.mapped_percentage:main"]},
    #classifiers=[
    #'Development Status :: 5 - Production/Stable',
    #'Environment :: Console',
    #'Intended Audience :: Science/Research',
    #'Operating System :: OS Independent',
    #'Programming Language :: Python :: 3.4',
    #'Programming Language :: Cython',
    #'Programming Language :: Python :: Implementation :: CPython',
    #'Topic :: Scientific/Engineering',
    #'Topic :: Scientific/Engineering :: Bio-Informatics'
    #],
    platforms="GNU/Linux, Mac OS X >= 10.7, Microsoft Windows >= 7",
    )
