from setuptools import setup

with open('docs/README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='wildbits',
    version='0.5',
    author='NiceneNerd',
    author_email='macadamiadaze@gmail.com',
    description='A GUI frontend for Leoetlino\'s Python tools for Breath of the Wild modding',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/NiceneNerd/Wild-Bits/',
    include_package_data = True,
    packages = ['wildbits'],
    entry_points = {
        'gui_scripts': [
            'wildbits = wildbits.__init__:main'
        ]
    },
    classifiers = [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.7'
    ],
    python_requires = '>=3.7',
    install_requires = [
        'pyYaml',
        'sarc',
        'rstb',
        'aamp',
        'byml',
        'wszst_yaz0',
        'PySide2'
    ]
)