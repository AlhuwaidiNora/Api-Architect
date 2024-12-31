from setuptools import setup, find_packages

setup(
    name="api-architect",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "pytest>=6.2.5",
        "requests>=2.26.0",
        "python-dotenv>=0.19.0",
    ],
)
