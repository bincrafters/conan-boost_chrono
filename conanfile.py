#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostChronoConan(base.BoostBaseConan):
    name = "boost_chrono"
    version = "1.67.0"
    url = "https://github.com/bincrafters/conan-boost_chrono"
    lib_short_names = ["chrono"]
    options = {"shared": [True, False]}
    default_options = "shared=False"    
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_core",
        "boost_integer",
        "boost_move",
        "boost_mpl",
        "boost_predef",
        "boost_ratio",
        "boost_static_assert",
        "boost_system",
        "boost_throw_exception",
        "boost_type_traits",
        "boost_typeof",
        "boost_utility",
        "boost_winapi"
    ]


