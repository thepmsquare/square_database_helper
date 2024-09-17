from setuptools import find_packages, setup

package_name = "square_database_helper"

setup(
    name=package_name,
    version="1.0.2",
    packages=find_packages(),
    install_requires=["requests>=2.31.0"],
    author="thePmSquare",
    author_email="thepmsquare@gmail.com",
    description="helper to access the database layer for my personal server.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url=f"https://github.com/thepmsquare/{package_name}",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
)
