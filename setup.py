import setuptools

setuptools.setup(
    name="PythonSaver",
    version="0.0.1",
    author="Ellek Linton",
    author_email="ellek.linton@gmail.com",
    description="Python Object saver by Ellek",
    long_description="Longer description",
    long_description_content_type="text/markdown",
    url="git+https://github.com/elleklinton/Python-Saver",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved",
        "Operating System :: OS Independent",
    ],
    dependency_links=[
        'git+https://github.com/elleklinton/Python-Saver-0.0.1',
    ]
)


