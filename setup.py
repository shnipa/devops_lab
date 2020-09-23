from setuptools import setup, find_packages

setup(
    name="homeworl3",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snapshot = systeminfo.snapshot:main",
        ],
    },
    version="0.1",
    author="Mikita Shnipau",
    author_email="Mikita_Shnipau@epam.com",
    description="System"
)

