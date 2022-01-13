from setuptools import setup, find_packages

VERSION = '0.1.0'

setup(
    name='4gewinnt',
    version=VERSION,
    license='MIT',
    description='4gewinnt-Spiel',
    author='Stefan Seidler und Sükrü Kakici',
    author_email='s50862@edu.campus02.at',
    url='https://github.com/stefanseidler182/4gewinnt_seidler_kakici',
    packages=find_packages(exclude=('tests', 'docs')),
    python_requires='>=3.8'
)