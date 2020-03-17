from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="claymore",
    version="0.1.0",
    author="Theo Henson",
    author_email="theodorehenson@protonmail.com",
    description="encrypted p2p chat client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tteeoo/claymore",
    packages=setuptools.find_packages(),
    install_requires=["pycryptodome"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            'claymore = claymore:main',
        ],
    },
)
