from setuptools import setup, find_packages

setup(
    name='omicron',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    version='0.0.0',
    entry_points='''
    [console_scripts] 
    omicron=omicron:cli
    '''
)