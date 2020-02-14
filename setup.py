import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yamlpp",
    version="1.0.1",
    author="Duncan Ogilvie",
    description="Simple YAML preprocessor, resolves anchors.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrexodia/yamlpp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["ruamel.yaml"],
    entry_points={
        "console_scripts": [
            "yamlpp = yamlpp.__main__:main"
        ]
    },
    )