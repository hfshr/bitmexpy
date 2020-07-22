from setuptools import setup, find_packages

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="bitmexpy", 
    version="0.0.1",
    author="Harry Fisher",
    author_email="harryfisher21@gmail.com",
    description="python client for BitMEX's API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hfshr/bitmexpy",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pandas',
        'requests',
        'numpy',
        'datetime'
    ],
    python_requires=">=3.6",
)
