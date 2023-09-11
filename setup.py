import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "text-summarizer-project"
AUTHOR_USER_NAME = "nyaksha06"
SRC_REPO = "text summarizer"
AUTHOR_EMAIL = "nyaksha06@gmail.com"

setuptools.setup(
    name="text-summarizer-project",
    version=__version__,
    author="nyaksha06",
    author_email= "nyaksha06@gmail.com",
    description="A small Python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/nyaksha06/text-summarizer-project",
    project_urls={
        "Bug Tracker": f"https://github.com/nyaksha06/text-summarizer-project/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
