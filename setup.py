from distutils.core import setup

setup(name='PyAEM',
      version='1.0',
      description='Python Distribution Utilities',
      author='Greg Ward',
      author_email='gward@python.net',
      url='https://www.python.org/sigs/distutils-sig/',
      #packages=['PyAEM'],
      packages=setuptools.find_packages(where=".")
     )