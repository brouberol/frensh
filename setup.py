import re

from os.path import dirname, join, abspath
from setuptools import setup

VERSION = re.search(
    r"__version__\s=\s'(\d\.\d\.\d)'",
    open(abspath(join(dirname(__file__), 'frensh', 'frensh'))).read()
    ).group(1)

setup(
    name="frensh",
    version=VERSION,
    license='3-clause BSD',
    description='Le french shell',
    author="Balthazar Rouberol",
    author_email="brouberol@imap.cc",
    url='http://github.com/brouberol/frensh',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    scripts=['frensh/frensh'],
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Shells',
        ]
    )
