import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="simulacion-problemas-clasicos",
    version="1.0.1",
    author="Kevin Guerra",
    description=("royecto final Sistemas Operativos 1 UMG"),
)
