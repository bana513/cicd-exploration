from setuptools import find_packages, setup  # type: ignore

DESCRIPTION = "CI/CD Exploration"

setup(
    name="cicd-exploration",
    version="0.1",
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    author_email="info@banatech.eu",
    package_dir={"": "src"},
    packages=find_packages("src"),
    package_data={"": ["*.py"]},
    install_requires=[],
)
