from setuptools import setup, find_packages

setup(
    name="roman_to_int",
    version="0.0.5",
    author="James",
    description="An module that converts roman numerals to integers",
    packages=find_packages(),
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    
)
