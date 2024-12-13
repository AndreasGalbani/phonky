from setuptools import setup, find_packages

setup(
    name='phonky',
    version='0.1.0',
    py_modules=['tsm'],
    packages=find_packages(),
    package_data={
        'pyarmor_runtime_000000': ['pyarmor_runtime.pyd'],
    },
)
