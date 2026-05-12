from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    
    """
    Function to return list of requirements

    """

    try:
        requirement_lst:List[str] = [ ]
        with open("requirements.txt",'r') as file:
            # to read lines 
            lines = file.readlines()
                # process each line
            for line in lines:
                requirement = line.strip()

                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    
    except FileNotFoundError:
        print('Requirement.txt file not found')

    return requirement_lst

setup(
    name = 'NetworkSecurity',
    version = "0.0.1",
    author = 'Ajit Yadav',
    packages = find_packages(),
    install_requires= get_requirements()
)
