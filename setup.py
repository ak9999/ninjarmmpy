import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ninjarmmpy",
    version="0.2.0",
    author="Abdullah 'AJ' Khan",
    author_email="aj@ajkhan.me",
    description="Unofficial API client wrapper around v2 of the NinjaRMM API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ak9999/ninjarmmpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests>=2.23.0'
    ],
    python_requires='>=3.7',
)
