from setuptools import setup, find_packages
import sys
import os

def_path = '.'
package_paths = [def_path, os.path.dirname(os.path.abspath(__file__))]

for package_path in package_paths:
    if package_path not in sys.path:
        sys.path.append(package_path)


from hatchery import __version__, __author__, __email__


with open(os.path.join(def_path, "README.md"), "rb") as fh:
    long_description = fh.read().decode("utf-8")

with open(os.path.join(def_path, "requirements.txt"), "r") as fh:
    requirements = fh.readlines()

# data_files

setup(
    name="hatchery",
    version=__version__,
    author=__author__,
    author_email=__email__,
    license='MIT',
    description="Visualization of hatchery data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Em2see/hatchery",
    packages=find_packages(where=def_path),
    package_dir={"": def_path},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={
        'hatchery': [
            r'server\templates\*.html',
        ]
    },
    entry_points={
        'console_scripts': [
            'hatchery=hatchery:cli'
        ]
    },
    include_package_data=True,
    python_requires='>=3.6',
    cmdclass={},
    install_requires=requirements,
    setup_requires=['wheel'],
    extras_require={
        'docs': [
            'sphinx',
            'sphinx_rtd_theme'
        ]
    },
)

