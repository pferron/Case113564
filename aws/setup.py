# This file needs to be run from the root of the project

import pathlib

import pkg_resources
from setuptools import setup


install_requires = []

with pathlib.Path("requirements.txt").open() as requirements_txt:
    install_requires.extend(
        [
            str(requirement)
            for requirement in pkg_resources.parse_requirements(requirements_txt)
        ]
    )

setup(
    name="xen-deploy",
    version="1.0",
    install_requires=install_requires,
    description="Deployment specific python module",
    author="Abhishek",
    packages=["xendeploy"],
)
