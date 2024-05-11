# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# packages required (replaces requirements.txt)
required = [
    'pandas',
    'spacy',
    'scispacy',
    'spacy-entity-linker'
]

setup(
    name="medical-nlp",
    version="0.1",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=required,
    # dependency_links=[] add model links if desired here
)
