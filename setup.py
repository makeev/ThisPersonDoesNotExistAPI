import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="thispersondoesnotexist", # Replace with your own username
    version="1.0.2",
    author="MM",
    author_email="mihail.makeev@gmail.com",
    description="API to thispersondoesnotexist.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/makeev/ThisPersonDoesNotExistAPI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'aiohttp',
        'aiofiles'
    ]
)
