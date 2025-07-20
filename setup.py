from setuptools import setup, find_packages

setup(
    name='coeirocore',
    version='3.11.1',
    url="https://github.com/hydriod/coeiroink_core",
    author="shirowanisan (original), hydriod (modifications)",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        "espnet @ git+https://git@github.com/espnet/espnet@bf02dd8c365547165c68e9b5067537086871c8e3",
        "pydantic>=2.11.7",
    ]
)
