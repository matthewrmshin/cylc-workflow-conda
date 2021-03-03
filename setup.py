"""Build demo project."""

from ast import literal_eval
import os

from setuptools import setup, find_packages


PKGNAME = 'hello'
URL = 'https://github.com/matthewrmshin/cylc-workflow-conda/'


# Get the long description from the README file
HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, 'README.md'), encoding='utf-8',) as handle:
    LONG_DESCRIPTION = handle.read()
with open(
    os.path.join(HERE, PKGNAME, '__init__.py'),
    encoding='utf-8',
) as handle:
    for line in handle:
        items = line.split('=', 1)
        if items[0].strip() == '__version__':
            VERSION = literal_eval(items[1].strip())
            break
    else:
        raise RuntimeError('Cannot determine package version.')


setup(
    name=PKGNAME,
    version=VERSION,
    description='Cylc Work Flow With Tasks Running In A Conda Envvironment',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url=URL,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    project_urls={
        'Bug Reports': f'{URL}issues',
        'Source': URL,
    },

    packages=find_packages(),
    entry_points={
        'console_scripts': [
            f'hello = {PKGNAME}.main:main',
        ],
    },
    include_package_data=True,

    python_requires='>=3.6, <4',
    install_requires=[],
    setup_requires=[],
    tests_require=[],
    zip_safe=True,
)
