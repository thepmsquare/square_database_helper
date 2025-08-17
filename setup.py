from setuptools import find_packages, setup

package_name = "square_database_helper"

setup(
    name=package_name,
    version="2.6.1",
    packages=find_packages(),
    install_requires=[
        "pydantic>=2.9.2",
        "square_commons>=2.0.0",
    ],
    author="Parth Mukesh Mangtani",
    author_email="thepmsquare@gmail.com",
    description="helper to access the database layer for my personal server.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url=f"https://github.com/thepmsquare/{package_name}",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
