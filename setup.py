import glob
import setuptools
import os

from uaclient import config

NAME = 'ubuntu-advantage-tools'


def get_version():
    major_minor, subrev, commitish  = config.get_version().split('-')
    return major_minor


_dir = os.path.dirname(os.path.realpath(__name__))
with open(os.path.join(_dir, 'requirements.txt')) as stream:
    INSTALL_REQUIRES = stream.readlines()

TEST_REQUIRES = [
    'coverage',
    'flake8',
    'pylint',
    'testtools',
]

setuptools.setup(
    name=NAME,
    version=get_version(),
    packages=setuptools.find_packages(exclude=['*.testing', 'tests.*', '*.tests', 'tests']),
    data_files=[('/etc/ubuntu-advantage', ['uaclient.conf']),
                ('/etc/update-motd.d', glob.glob('update-motd.d/*')),
                ('/usr/share/keyrings', glob.glob('keyrings/*'))],
    install_requires=INSTALL_REQUIRES,
    extras_require=dict(test=TEST_REQUIRES),
    author='Ubuntu Server Team',
    author_email='ubuntu-server@lists.ubuntu.com',
    description=('Manage Ubuntu Advantage support entitlements: esm, fips'
                 ' and livepatch'),
    license='GPLv3',
    url='https://ubuntu.com/advantage',
    entry_points={'console_scripts': ['ubuntu-advantage=uaclient.cli:main',
                                      'ua=uaclient.cli:main']}
)
