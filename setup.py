from setuptools import setup, find_packages
import viki

setup(
    name=viki.__name__,
    version=viki.__version__,
    url=viki.__url__,
    author=viki.__author__,
    author_email=viki.__author_email__,
    license=viki.__license__,
    description=viki.__description_long__,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    install_requires=[
        'requests'
    ],
    keywords=viki.__keywords__,
    include_package_data=True,
    packages=find_packages(),
    scripts=['bin/viki'],
    entry_points = {
        'console_scripts': [
            'viki = viki.bin.viki:main'
            ]
        }
)
