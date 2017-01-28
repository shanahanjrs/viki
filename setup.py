from distutils.core import setup
import os

setup(
    name         = 'viki',
    version      = '0.0.1',
    author       = 'John Shanahan',
    author_email = 'shanahan.jrs@gmail.com',
    license      = 'tba',
    description  = 'Viki is a command line web hook reciever and developer assisstant '
    'that can execute tasks remotely or on demand.',
    url          = 'https://github.com/shanahanjrs/viki',
    packages     = [
        'viki'
    ],
    package_data = {
        'cheat.cheatsheets': [f for f in os.listdir('cheat/cheatsheets') if '.' not in f]
    },
    scripts          = ['bin/viki'],
    install_requires = [
        'flask >= 0.6.1',
    ]
)
