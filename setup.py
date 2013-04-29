from setuptools import setup

entry_points = """
    [paste.app_factory]
    main = realEstateApp:main
"""

requires = [
    'pyramid',
    'waitress',
    'sqlalchemy'
]

setup(name='realEstateApp',
      version='0.0.1',
      description='Real Estate General App',
      install_requires=requires,
      packages=['realEstateApp'],
      entry_points=entry_points
      )
