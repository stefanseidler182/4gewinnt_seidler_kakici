from setuptools import setup, find_packages

VERSION = '0.1.0'

setup(
    name='viergewinnt',
    version=VERSION,
    license='MIT',
    description='viergewinnt-Spiel',
    author='Stefan Seidler und Sükrü Kakici',
    author_email='s50862@edu.campus02.at',
    url='https://github.com/stefanseidler182/viergewinnt',
    packages=find_packages(exclude=('tests', 'docs')),
    python_requires='>=3.8'
)