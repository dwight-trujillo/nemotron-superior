from setuptools import setup, find_packages

setup(
    name="nemotron-superior",
    version="2.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.115.0",
        "uvicorn>=0.34.0",
        "pydantic>=2.10.0",
        "sqlalchemy>=2.0.0",
    ],
    python_requires=">=3.8",
)
