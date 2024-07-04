# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from os import path
# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# packages required (replaces requirements.txt)
required = [
    'pandas',
    'spacy',
    'scispacy',
    'spacy-entity-linker',
    'scikit-learn',
    'matplotlib',
    'spacy-streamlit'
]

setup(
    name="medical_nlp",
    version="0.1",
    package_dir={'': 'src'},
    packages=["medical_nlp"],
    py_modules=['medical_nlp'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=required,
    # dependency_links=[] add model links if desired here
)
