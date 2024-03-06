import setuptools

with open("AvraePycharm/readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="avrae-pycharm",
    version="0.0.1",
    author="Bryce Hadsell",
    author_email="bryce.hadsell@gmail.com",
    description="Avrae application for PyCharm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Corvux89/Avrae-Pycharm",
    packages=setuptools.find_packages(exclude=("tests",)),
    scripts=["avrae.py"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)