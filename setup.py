try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'discription': 'TwoWorlds is a single player text adventure.',
    'author': 'Dennis Neumann',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'email',
    'version': '0.1',
    'install_requires': [''],
    'packages': ['TwoWorlds'],
    'scripts': [''],
    'name': 'TwoWorlds'
}

setup(**config)