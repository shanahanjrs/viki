from distutils.core import setup

setup(
    # Basic info
    name         = 'viki',
    version      = '0.0.1.dev1',
    url          = 'https://github.com/shanahanjrs/viki',

    # Author
    author       = 'John Shanahan',
    author_email = 'shanahan.jrs@gmail.com',

    # License
    license      = 'Apache',

    # Desc
    description  = 'Viki is a command line web hook reciever and developer assisstant '
    'that can execute tasks remotely or on demand.',

    classifiers  = [
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],

    # Dependencies
    install_requires = [
        'flask',
        'redis'
    ],

    # What does your project relate to?
    keywords = 'deployment setuptools development builds automation webhooks scheduler job-runner',

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # entry_points={
    #     'console_scripts': [
    #         'viki=viki:main',
    #     ],
    # }
    scripts = ['viki']

)
