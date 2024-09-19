from setuptools import setup, find_packages # type: ignore

setup(
    name="expense-tracker",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "expense-tracker = expense_tracker.main:main"
        ],
    },
    include_package_data=True,
)