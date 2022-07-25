import setuptools

with open("README.md", "r") as rf:
    long_description = rf.read()

setuptools.setup(
    name="min_package",
    version="1.0",
    author="Sung Keem",
    author_email="keem@keem.net",
    description="Package setup demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/keemsunguk/min_package.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    include_package_data=False,
)

#  change include_package_data=True when UnitTest data need to be included
# package_data={'': ['data/test_data.json']},