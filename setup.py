from setuptools import setup, find_packages
with open('README.md', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='clog',
    version='0.1.0',
    description='Cli tool',
    long_description=readme,
    author='Felipe Gusmao',
    author_email='felipe@pinguim.software',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['boto3'],
    entry_points={
        'console_scripts': [
            'clog=clog.cli:main',
        ],
    },
)
