from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    # Initialize an empty list
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        
        # Strip newline characters from each requirement
        requirements = [req.replace('\n', '') for req in requirements]
    
    # Remove HYPHEN_E_DOT if present
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    
    return requirements  # Return the list

setup(
    name='fault detection', 
    version='0.0.1',
    author='Mukul',
    author_email='mukularya@gmail.com',
    install_requires=get_requirements('requirements.txt'),  # Correctly call the function
    packages=find_packages()  # Proper call to find packages
)
