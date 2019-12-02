from distutils.core import setup
from setuptools import find_packages


setup(
    name="statannot",
    version="0.2.1",
    packages=find_packages(),
    install_requires=open("requirements.txt").readlines(),
    python_requires='>=3.5',
    long_description=open("readme.md").read(),
    description="Python package to add statistical annotations on an existing boxplot generated by seaborn.",
)
