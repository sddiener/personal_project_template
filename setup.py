"""
Setup file defining the package's attributes and properties.
"""

from pathlib import Path
from setuptools import find_packages, setup


def read_requirements() -> list[str]:
    """
    Reads the requirements.txt file and returns a list of required packages.

    Returns:
        List[str]: A list of package requirements.
    """
    requirements_file_path = Path(__file__).parent / 'requirements.txt'
    if not requirements_file_path.is_file():
        raise FileNotFoundError(f"{requirements_file_path} does not exist.")

    return requirements_file_path.read_text().splitlines()


setup(
    name='Project Name',
    version='1.0.0',
    description='This project ...',
    author='Stefan Diener',
    package_dir={'': 'src'},  # Root directory for packages set to 'src'
    packages=find_packages(where='src'),
    install_requires=read_requirements(),  # Rad dependencies from requirements.txt
    python_requires='>=3.11',
)
