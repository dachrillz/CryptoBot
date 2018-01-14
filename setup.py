from setuptools import setup


setup(name='FinanceEuler',
      version='0.1',
      description='Chrilles\' and magnus\' cryptobot!',
      url='https://github.com/dachrillz/CryptoBot',
      author='Christoffer, Magnus',
      author_email='olschr2@gmail.com',
      license='None so far...',
      dependency_links=['https://github.com/mementum/backtrader'],
      packages=['cryptobot'],
      install_requires=[
          'backtrader', 'matplotlib'
      ],
      zip_safe=False)