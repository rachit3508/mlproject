from setuptools import setup,find_packages

def package_requirements(file_path):
    lines=[]
    with open(file_path, "r") as file:
        lines = file.readlines()
        if '\n' in lines:
            lines.remove('\n')
        if '-e .' in lines:
            lines.remove('-e .')
    
    return lines

setup(
    name='mlproject',
    version='0.1',
    description='This is my first package of end to end project',
    author='Rachit Singh',
    author_email='rachitsingh150@gmail.com',
    packages=find_packages(),
    requires=package_requirements('requirements.txt')
)