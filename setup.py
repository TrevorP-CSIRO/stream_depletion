from setuptools import find_packages, setup

setup (
    name='StreamDepletionPy',
    packages=find_packages(include=['StreamDepletion','StreamDepletion.Examples']),
    version='0.1.0',
    description="A library of 8 stream depletion solutions + examples",
    author='Trevor Pickett', 
    author_email='trevor.pickett@csiro.au'

)