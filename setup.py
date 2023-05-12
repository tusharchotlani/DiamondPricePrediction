from setuptools import find_packages,setup
from typing import List

#HYPEN_E_DOT='-e .'                       ( we can use '-e.'to install packages using pip command otherwise we can run directly setup file)

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

       ## if HYPEN_E_DOT in requirements:
         #  requirements.remove(HYPEN_E_DOT)

        return requirements


setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Tushar',
    author_email='tusharchotlani07@gmail',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()

)