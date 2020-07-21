import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bitmexpy", # Replace with your own username
    version="0.0.1",
    author="Harry Fisher",
    author_email="harryfisher21@gmail.com",
    description="python client for BitMEX's API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hfshr/bitmexpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)