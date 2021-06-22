"""Python library build"""
from setuptools import setup, find_packages
import versioneer

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

with open('install_requires.txt') as f:
    required = f.read().splitlines()

gwastoolkit_version = versioneer.get_version()
gwastoolkit_cmdclass = versioneer.get_cmdclass()
# gwastoolkit_cmdclass['build_sphinx'] = BuildDoc

setup(
    name='gwastoolkit',
    version=gwastoolkit_version,
    cmdclass=gwastoolkit_cmdclass,
    description='Library contains connectors to several data sources and check functions.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/byeungchun",
    author='Byengchun Kwon',
    author_email='byeungchun.kwon@gmail.com',
    packages=find_packages(
        exclude=("test")
    ),
    install_requires=required,
    include_package_data=True,
    # These command_options are optional and override the settings in conf.py:
    command_options={
        'build_sphinx': {
            'version': ('setup.py', gwastoolkit_version),
            'source_dir': ('setup.py', 'docs')}}
            # 'build_dir':('setup.py', 'docs/_build')}}    
    )