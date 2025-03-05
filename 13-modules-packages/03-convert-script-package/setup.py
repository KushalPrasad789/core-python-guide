from setuptools import setup, find_packages

setup(
    name="my_package",                # Package name
    version="0.1",                     # Version
    packages=find_packages(),          # Auto-detect package
    install_requires=[],               # Dependencies (if any)
    entry_points={                     # Command-line script (optional)
        "console_scripts": [
            "greet=my_package.my_script:greet",
        ]
    },
)
