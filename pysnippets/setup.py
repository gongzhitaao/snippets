from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pysnippets',
    version='0.1.0',
    description='Scattered python snippets',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gongzhitaao/snippets/pysnippets',
    author='gongzhitaao',
    author_email='zhitaao.gong@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='snippets',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[],
    extras_require={
        'test': ['pytest'],
    },
)
