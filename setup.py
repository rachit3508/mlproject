from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function return the list of packages required to install this package
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n",'') for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements

setup(name='mlproject',
    version='0.0.1',
    description='End to End ML Project',
    author='Rachit Singh',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
    )