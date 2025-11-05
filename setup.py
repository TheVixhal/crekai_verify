from setuptools import setup, find_packages

setup(
    name="crekai_verify",
    version="1.0.0",
    author="CrekAI Dev Team",
    description="Universal CrekAI Verification Package",
    packages=find_packages(),
    install_requires=["requests"],
    python_requires=">=3.7",
)
