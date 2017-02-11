from distutils.core import setup
import src._version

setup(
    # Basic info
    name         = 'viki',
    version      = src._version.__version__,
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
        'Development Status :: 2 - Pre-Alpha',

        'Intended Audience :: Developers',

        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: Apache Software License',

        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',

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
        'pytest',
        'gunicorn'
    ],

    # What does your project relate to?
    keywords = 'deployment setuptools development builds automation webhooks scheduler job-runner',

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    #entry_points={
        #'console_scripts': [
            #'viki=viki:main',
        #],
    #}
    scripts = ['vikid', 'viki']

)
