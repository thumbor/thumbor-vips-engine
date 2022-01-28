<p align="center">
<img src="https://raw.github.com/thumbor/thumbor/master/logo-thumbor.png" />
</p>

<h3 align="center">thumbor-vips-engine</h3>

<p align="center">
⚡blazing fast image processing engine for thumbor using libvips
</p>

<p align="center">
  <img src='https://github.com/thumbor/thumbor-vips-engine/workflows/build/badge.svg' />
  <a href='https://coveralls.io/github/thumbor/thumbor-vips-engine?branch=main'><img src='https://coveralls.io/repos/github/thumbor/thumbor-vips-engine/badge.svg?branch=main' alt='Coverage Status' /></a>
</p>
<p align="center">
  <a href='https://github.com/thumbor/thumbor-vips-engine/pulls' target='_blank'>
    <img src='https://img.shields.io/github/issues-pr-raw/thumbor/thumbor-vips-engine.svg'/>
  </a>
  <a href='https://github.com/thumbor/thumbor-vips-engine/issues' target='_blank'>
    <img src='https://img.shields.io/github/issues-raw/thumbor/thumbor-vips-engine.svg'/>
  </a>
  <a href='https://pypi.python.org/pypi/thumbor-vips-engine' target='_blank'>
    <img src='https://img.shields.io/pypi/v/thumbor-vips-engine.svg'/>
  </a>
  <a href='https://pypi.python.org/pypi/thumbor-vips-engine' target='_blank'>
    <img src='https://img.shields.io/pypi/dm/thumbor-vips-engine.svg'/>
  </a>
</p>

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

If you still need help, please [raise an issue](https://github.com/thumbor/thumbor-vips-engine/issues).

## 👀 Thumbor

[thumbor-vips-engine](https://github.com/thumbor/thumbor-vips-engine) stands on the shoulders of [thumbor](https://github.com/thumbor/thumbor)! If you are not familiar with [thumbor](https://github.com/thumbor/thumbor), please check the [docs](https://thumbor.readthedocs.io/en/latest/) or you can see a demo at http://thumborize.me/

## 👍 Contribute

thumbor-vips-engine is an open-source project with many contributors. Join them
[contributing code](https://github.com/thumbor/thumbor-vips-engine/blob/master/CONTRIBUTING.md) or
[contributing documentation](https://github.com/thumbor/thumbor-vips-engine/blob/master/CONTRIBUTING.md).

Join the chat at https://gitter.im/thumbor/thumbor

## License

Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/
