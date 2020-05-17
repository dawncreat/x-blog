import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="X-BLOG",
    version="0.1",
    author="xiaojueguan",
    author_email="xiaojueguan@gmail.com",
    description="A blog web application package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/albertjone/x-blog",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Framework :: Django :: 2.1"
    ],
    python_requires='>=3.6',
)
