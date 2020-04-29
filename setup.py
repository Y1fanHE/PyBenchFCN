import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyBenchFCN", # Replace with your own username
    version="0.0.2",
    author="Yifan He",
    author_email="he.yifan.xs@alumni.tsukuba.ac.jp",
    description="A library for optimization benchmark functions in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

