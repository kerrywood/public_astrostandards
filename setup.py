from setuptools import setup, find_packages
setup(
    name='public_astrostandards',
    version='0.1.0',
    description = 'Python harnesses for the open-source AstroStandards libraries',
    author = 'Kerry N. Wood',
    author_email = 'kerry.wood@asterism.ai',
    packages=find_packages(include=['public_astrostandards', 'public_astrostandards.*'])
)
