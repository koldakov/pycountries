from pathlib import Path

from setuptools import find_packages, setup


def _get_file(name: str):
    return (Path(__file__).parent / name).read_text()


setup(
    long_description=_get_file("README.md"),
    long_description_content_type="text/markdown",
    package_dir={
        "": "src",
    },
    packages=find_packages(
        where="src",
    ),
)
