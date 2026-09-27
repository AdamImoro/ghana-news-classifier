
from setuptools import setup, find_packages
from typing import List 

requirements_list = []

def get_requirement(file_path:str)->List[str]:
    """
        This function return list of requirements
    """
    with open(file=file_path) as file:
        try:
            #Read lines 
            lines = file.readlines()

            #Reading each line 
            for line in lines:
                requirement =line.strip()

                # ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirements_list.append(requirement)

        except FileNotFoundError:
            print("Requirements.txt  not found!")
    return requirements_list



setup(
    name="ghana-news-classifier",
    version="0.0.1",
    author='imoro',
    author_email='imoroadam895@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt')
)