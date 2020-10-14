import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gsheet_plotter-nitika-kamboj
    version="0.0.1",
    author="Nitika Kamboj",
    author_email="nitika.kamboj92@gmail.com",
    description="A visualisation library written in Python to plot your Google Sheets.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0-License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
