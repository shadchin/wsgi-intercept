
from setuptools import setup, find_packages

VERSION = '1.12.1'

CLASSIFIERS = """
Environment :: Web Environment
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Topic :: Internet :: WWW/HTTP :: WSGI
Topic :: Software Development :: Testing
""".strip().splitlines()


META = {
    'name': 'wsgi_intercept',
    'version': VERSION,
    'author': 'Titus Brown, Kumar McMillan, Chris Dent, Sasha Hart',
    'author_email': 'cdent@peermore.com',
    'description':
        'wsgi_intercept installs a WSGI application in place of a '
        'real URI for testing.',
    # What will the name be?
    'url': 'http://pypi.python.org/pypi/wsgi_intercept',
    'long_description': open('README').read(),
    'license': 'MIT License',
    'classifiers': CLASSIFIERS,
    'packages': find_packages(),
    'install_requires': [
        'six',
    ],
    'extras_require': {
        'testing': [
            'pytest>=2.4',
            'httplib2',
            'requests>=2.0.1',
            'urllib3>=1.11.0,<2.0.0',
        ],
        'docs': [
            'sphinx',
        ],
    },
}

if __name__ == '__main__':
    setup(**META)
