import setuptools
import os

with open("README.rst", "r") as fh:
    long_description = fh.read()


with open ('requirements.txt', 'r') as file:
    install_requires = file.readlines()
install_requires = [x.strip() for x in install_requires]

setuptools.setup(
    name="pynomial",
    version="0.1",
    author="Silver Creek",
    author_email="austin.mcleod@silvercreeksoftware.com; mostafa.hadavand@silvercreeksoftware.com",
    description="pynomial",
    long_description=long_description,
    long_description_content_type="text/markup",
    url="https://github.com/Silver-Creek/pynomial.git",
    download_url="https://github.com/Silver-Creek/pynomial/archive/v0.1.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires = install_requires,
    zip_safe=False
)