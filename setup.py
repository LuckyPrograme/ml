from setuptools import setup, find_packages

setup(
    name="gemini-olymp-fast",
    version="0.1",
    packages=find_packages(),
    install_requires=["google-generativeai"],
    entry_points={
        "console_scripts": [
            "gem=gemini_olymp.cli:main"
        ]
    },
)
