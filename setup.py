from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Math_genius",
    version="0.1.0",
    author="Álvaro Bravo López",
    author_email="alvaritobralo@gmail.com",
    description="Math_genius is a small python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlvaroB12/Math_genius",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy'
        'sympy'
        'scipy'
    ],
    include_package_data=True,
    keywords="math python library",
    project_urls={
        'Bug Reports': 'https://github.com/AlvaroB12/Math_genius/issues',
        'Source': 'https://github.com/AlvaroB12/Math_genius',
    },
)
