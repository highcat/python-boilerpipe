from os.path import basename, exists, dirname, abspath, join
from distutils.core import setup

__version__ = '1.2.0.0'

setup(
    name='boilerpipe',
    version=__version__,
    packages=['boilerpipe', 'boilerpipe.extract'],
    package_data={
        'boilerpipe': [
            'data/boilerpipe-1.2.2/boilerpipe-core-1.2.2.jar',
            'data/boilerpipe-1.2.2/README',
            'data/boilerpipe-1.2.2/lib/*.jar',
        ],
    },
    install_requires=[
        'JPype1',
        'charade',
    ],
    author='Misja Hoebe',
    author_email='misja.hoebe@gmail.com',
    maintainer = 'Matthew Russell',
    maintainer_email = 'ptwobrussell@gmail.com',
    url = 'https://github.com/highcat/python-boilerpipe/',
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Natural Language :: English',
      ],
      keywords='boilerpipe',
      license='Apache 2.0',

    description='Python interface to Boilerpipe, Boilerplate Removal and Fulltext Extraction from HTML pages'
)
