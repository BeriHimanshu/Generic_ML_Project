from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads the requirements.txt file and returns a list of dependencies.
    '''
    requirements = []
    with open(file_path, 'r') as f:
        # Read lines and strip out the newline characters
        requirements = [line.replace("\n", "") for line in f.readlines()]
        
        # Remove '-e .' if it exists in the requirements file
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements

# Corrected function call (no "=" sign)
setup(
    name="Generic_ML_Project",
    version="0.0.1",
    author="Himanshu Beri",
    author_email="himanshuberi1606@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)