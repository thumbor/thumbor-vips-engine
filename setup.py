#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor vips engine
# https://github.com/thumbor/thumbor-vips-engine

# Apache License
# Version 2.0, January 2004
# http://www.apache.org/licenses/

from distutils.core import setup

try:
    from thumbor_vips_engine import __version__

except ImportError:
    __version__ = "0.0.0"

TESTS_REQUIREMENTS = [
    "autoimport==1.*,>=1.0.4",
    "black==21.*,>=21.12b0",
    "coverage==5.*,>=5.0.3",
    "flake8==3.*,>=3.7.9",
    "isort==4.*,>=4.3.21",
    "mypy>=0.931",
    "preggy==1.*,>=1.4.4",
    "pylint==2.*,>=2.4.4",
    "pytest==6.*,>=6.2.5",
    "pytest-asyncio==0.*,>=0.17.2",
    "pytest-cov==3.*,>=3.0.0",
    "pytest-tldr==0.*,>=0.2.1",
    "pytest-xdist==2.*,>=2.5.0",
    "pytest-sugar>=0.9.4,<1.0.0",
    "pytest-icdiff>=0.5,<1.0.0",
    "yanc==0.*,>=0.3.3",
    "pre-commit==2.*,>=2.17.0",
    "syrupy==1.*,>=1.7.3",
]

VIPS_REPO = "https://github.com/thumbor/thumbor-vips-engine"


setup(
    name="thumbor_vips_engine",
    version=__version__,
    description="thumbor libvips engine",
    long_description=f"""
## ⚙️ Installation

```bash
pip install thumbor-vips-engine
```

## 🎯 Features

- libvips based engine
- Conforms with thumbor 7 engine specs
- Python 3 compliant

## Usage

### Configuring thumbor

Configure your `thumbor.conf` file to point to `thumbor_vips_engine`:

```
ENGINE = "thumbor_vips_engine.engine"
```

### Troubles?

If you experience any troubles, try running:

```bash
thumbor-doctor
```

If you still need help, please
[raise an issue]({VIPS_REPO}/issues).

## 👀 Thumbor

[thumbor-vips-engine]({VIPS_REPO}) stands on
the shoulders of [thumbor](https://github.com/thumbor/thumbor)! If you are not
familiar with [thumbor](https://github.com/thumbor/thumbor),
please check the [docs](https://thumbor.readthedocs.io/en/latest/)
or you can see a demo at http://thumborize.me/

## 👍 Contribute

thumbor-vips-engine is an open-source project with many contributors. Join them
[contributing code]({VIPS_REPO}/blob/master/CONTRIBUTING.md) or
[contributing documentation]({VIPS_REPO}/blob/master/CONTRIBUTING.md).

Join the chat at https://gitter.im/thumbor/thumbor

## License

Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/
""",
    keywords=("imaging face detection feature thumbnail libvips vips"),
    author="Bernardo Heynemann",
    author_email="heynemann@gmail.com",
    url=VIPS_REPO,
    license="Apache2",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Multimedia :: Graphics :: Presentation",
    ],
    packages=["thumbor_vips_engine"],
    package_dir={"thumbor_vips_engine": "thumbor_vips_engine"},
    include_package_data=True,
    package_data={
        "thumbor_vips_engine": ["*.xml", "*.jpg", "*.jpeg", "*.gif", "*.png"],
    },
    install_requires=[
        "thumbor==7.*,>=7.0.3",
        "pycurl==7.*,>=7.44.1",
        "pyvips==2.*,>=2.1.16",
    ],
    extras_require={"tests": TESTS_REQUIREMENTS},
    entry_points={
        "console_scripts": [],
    },
)
