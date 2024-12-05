from setuptools import setup, find_packages

setup(
    name="filmdevagency",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "agency-swarm==0.4.1",
        "requests>=2.31.0",
        "pydantic>=2.0.0",
        "gradio>=4.0.0",
        "python-dotenv>=0.19.0",
    ],
    python_requires=">=3.7",
) 