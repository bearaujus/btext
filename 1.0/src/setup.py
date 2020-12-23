import sys
from os import path
from setuptools import setup, find_packages

if 'install' in sys.argv:
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')

curdir = path.abspath(path.dirname(__file__))
with open(path.join(curdir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

name = 'btext'
version = '1.0'
description = 'Bear Au Jus Text (btext) is a tool used for processing a text/string, optimized for data science and data analytics. btext can also implemented with pandas dataframe.'
url = 'https://github.com/haryobagas/btext'
author = 'Bear Au Jus - ジュースとくま'
author_email = 'haryobagasasyafah6@gmail.com'

list_classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
    'Natural Language :: English',
    'Topic :: Utilities',
]

list_install_requirements = [
    'textcleaner',
]

list_keywords = [
    'btext',
    'bearaujus',
    'bearaujus btext',
    'basic string',
    'text procesing',
    'text cleaning',
    'text normalization',
    'text lemming',
    'string procesing',
    'string cleaning',
    'string normalization',
    'string lemming',
    'text procesing in pandas',
    'text cleaning in pandas',
    'text normalization in pandas',
    'text lemming in pandas',
    'string procesing in pandas',
    'string cleaning in pandas',
    'string normalization in pandas',
    'string lemming in pandas',
    'data analysis',
    'data cleaning',
    'data science',
    'data analysis in pandas',
    'data cleaning in pandas',
    'data science in pandas',
]

setup (
    name = name,
    version = version,
    description = description,
    long_description = long_description,
    long_description_content_type='text/markdown',
    url = url,
    author = author,
    author_email = author_email,
    license = 'MIT',
    classifiers = list_classifiers,
    keywords = list_keywords,
    packages = find_packages(),
    install_requires = list_install_requirements
)

