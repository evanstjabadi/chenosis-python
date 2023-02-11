from setuptools import find_packages, setup

setup(
    name="chenosis",
    python_requires=">=3.7",
    author="Evans Tjabadi",
    version="0.1.0",
    description="A python client for MTN's Chenosis platform: https://chenosis.io.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3",
    ],
    url="https://github.com/evanstjabadi/chenosis-python",
    packages=find_packages(exclude=["tests"]),
    package_data={"chenosis": ["py.typed"]},
    include_package_data=True,
    zip_safe=False,
    install_requires=["httpx~=0.23.3"],
)
