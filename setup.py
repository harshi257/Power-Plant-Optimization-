from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """
    Reads requirements.txt and returns a clean list of dependencies
    """
    requirements = []
    with open(file_path, encoding="utf-8") as file_obj:
        for line in file_obj:
            line = line.strip()
            if line and not line.startswith("#") and not line.startswith("-e"):
                requirements.append(line)
    return requirements


setup(
    name="power-plant-optimization",
    version="0.1.0",
    author="Harshita Garg",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements("requirements.txt"),
)
