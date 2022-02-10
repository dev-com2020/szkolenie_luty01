import os
import sys
import subprocess
import pkg_resources
from pkg_resources import DistributionNotFound, VersionConflict

__all__ = ["kalkulator", "srednia","should_install_requirement","install_packages"]


print("""
    ______________________MÓJ PROGRAM v.0.1b______________________
    """)

# os.system('pip install pandas')


def should_install_requirement(requirement):
    should_install = False
    try:
        pkg_resources.require(requirement)
    except (DistributionNotFound, VersionConflict):
        should_install = True
    return should_install


def install_packages(requirement_list):
    try:
        requirements = [
            requirement
            for requirement in requirement_list
            if should_install_requirement(requirement)
        ]
        if len(requirements) > 0:
            subprocess.check_call([sys.executable, "-m", "pip", "install", *requirements])
        else:
            print("Requirements already satisfied.")

    except Exception as e:
        print(e)
