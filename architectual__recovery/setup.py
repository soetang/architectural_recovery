from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

version = "0.0.1"
include_data_patterns = ["*.yaml", "*.yml"]

setup(
    name="archrcover",
    version=version,
    description="Python Package for ...",
    py_modules=find_packages(where="src"),
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={'': include_data_patterns},
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7.6",
        "Programming Language :: Python :: 3.8.13",
        "Programming Language :: Python :: 3.9.12",
        "Programming Language :: Python :: 3.10.4",
        "License :: proprietary",
        "Operating System :: OS Independent",
    ],
    url="https://dev.azure.com/pfa/Data%20Science/_git/architectual__recovery",
    author="bso",
    install_requires=required,
    author_email="bso@pfa.dk",
)
