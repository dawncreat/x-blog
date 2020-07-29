from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="X-BLOG",
    version="0.1",
    packages=find_packages(),
    scripts=[],

    install_requires=[],

    package_data={

    }

    author="xiaojueguan",
    author_email="xiaojueguan@gmail.com",
    description="A blog web application package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="blog django python",
    url="https://github.com/albertjone/x-blog",
    project_urls = {
        "Bug Tracker": "https://github.com/albertjone/x-blog/issues",
        "Documentation": "https://github.com/albertjone/x-blog/blob/master/readme.md",
        "Source Code": "https://github.com/albertjone/x-blog"
    }

    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Framework :: Django :: 2.1"
    ],
    python_requires='>=3.6',
)
