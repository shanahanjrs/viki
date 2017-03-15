from setuptools import setup, find_packages
import Viki.viki

setup(
    name='viki',
    version=viki.__version__,
    url='https://vikiautomation.com',
    author='John Shanahan',
    author_email='shanahan.jrs@gmail.com',
    license='Apache',
    description='Viki is a command line web hook reciever and developer assisstant '
    'that can execute tasks remotely or on demand.',
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
    keywords='deployment setuptools development builds automation webhooks scheduler job-runner',
    include_package_data=True,
    packages=find_packages(),
    scripts=['viki/viki.py']
)
