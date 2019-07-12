#!/usr/bin/env python3
# coding: utf-8

"""
updates all packages installed by pip
"""

import pkg_resources
from subprocess import call
packages = [dist.project_name for dist in pkg_resources.working_set]
call(f'pip install --upgrade {" ".join(packages)}', shell=True)
