from setuptools import setup, find_packages

setup(
    name="schema-md",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "click>=8.0,<9.0",
        "Jinja2>=3.0,<4.0",
        "mysql-connector-python>=8.0,<9.0",
    ],
    entry_points={
        "console_scripts": ["schema-md=schema_md.cli:main",],
    },
)
