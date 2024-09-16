from setuptools import setup

setup(
    name='klayout_run',
    version='0.1',
    py_modules=['klayout_run', 'searchlogic'],
    install_requires=['pick'],
    entry_points={
        'console_scripts': [
            'klayout_run=klayout_run:main' 
        ]
    }
)
