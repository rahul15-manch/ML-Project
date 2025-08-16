from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> list[str]:
    """
    Reads a requirements file and returns a list of valid packages.
    Ignores '-e .' and empty lines.
    """
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            req = line.strip()  # removes whitespace and \n
            if req and req != "-e .":  # ignore empty lines and editable install
                requirements.append(req)
    return requirements

setup(
    name="MLProject",  # avoid spaces in package name
    version="0.0.1",
    author="Rahul",
    author_email="rahulmanchanda015@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
