#!/usr/bin/env python
import pocket

from distutils.core import setup


description = "Python SDK for Pocket."

setup(
    name='pocket',
    version=pocket.__version__,
    author='Gong Zibin',
    author_email='gzb1985@gmail.com',
    url='https://github.com/gzb1985/pocketpy',
    description=description,
    long_description=description,
    license='BSD',
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    packages=['pocket', ],
)
