from setuptools import setup , find_packages
from io import open
from os import path

import pathlib



setup (
    name = 'directree',
    description = 'Directories tree generator',
    packages=['directree'],
    version='0.1.7',
    license='MIT',
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'directree=directree.__main__:run',
        ]
    },
    author='Samar Arora',
    keywords='directree, directories, tree',
    url='https://github.com/samar2170/directree',
    author_email='samararora99@gmail.com',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ]
)