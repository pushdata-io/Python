import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pushdata-io",
    version="0.0.1",
    author="Ragnar Lonn",
    author_email="hello@pushdata.io",
    description="Client library for pushdata.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pushdata-io/Python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)