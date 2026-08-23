"""
    Gnaww Developer API

    Reviewed public print-intelligence contract for direct HTTP, CLI, SDK and MCP consumers. Capability fit is not price, live availability, producer acceptance or an order.

    The version of the OpenAPI document: 0.1
    Gnaww SDK

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "gnaww-sdk"
VERSION = "0.1.0"
PYTHON_REQUIRES = ">= 3.11"
REQUIRES = [
    "urllib3 >= 2.1.0, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2.11",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Official Python SDK for the Gnaww print intelligence API.",
    author="Jawwws Ltd",
        url="https://github.com/jawwws/gnaww-sdk-python",
    license="MIT",
    keywords=["OpenAPI", "gnaww-sdk", "Gnaww Developer API"],
    install_requires=REQUIRES,
    python_requires=PYTHON_REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    Reviewed public print-intelligence contract for direct HTTP, CLI, SDK and MCP consumers. Capability fit is not price, live availability, producer acceptance or an order.
    """,  # noqa: E501
    package_data={"gnaww_sdk": ["py.typed"]},
)
