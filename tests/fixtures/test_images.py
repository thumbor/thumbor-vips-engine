#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor vips engine
# https://github.com/thumbor/thumbor-vips-engine

# Apache License
# Version 2.0, January 2004
# http://www.apache.org/licenses/


import unicodedata
from os.path import abspath, dirname, join

import pytest


def get_abs_path(img):
    return abspath(join(dirname(__file__), img))


VALID_IMAGE_PATH = get_abs_path("alabama1_ap620é.jpg")
SVG_IMAGE_PATH = get_abs_path("Commons-logo.svg")
TOO_SMALL_IMAGE_PATH = get_abs_path("20x20.jpg")
TOO_HEAVY_IMAGE_PATH = get_abs_path("Giunchedi%2C_Filippo_January_2015_01.jpg")
DEFAULT_IMAGE_PATH = get_abs_path("image.jpg")
ALABAMA1_IMAGE_PATH = get_abs_path("alabama1_ap620%C3%A9.jpg")
SPACE_IMAGE_PATH = get_abs_path("image%20space.jpg")
INVALID_QUANTIZATION_IMAGE_PATH = get_abs_path("invalid_quantization.jpg")
ANIMATED_IMAGE_PATH = get_abs_path("animated.gif")
NOT_SO_ANIMATED_IMAGE_PATH = get_abs_path("animated-one-frame.gif")


def get_image(img):
    encode_formats = ["NFD", "NFC", "NFKD", "NFKC"]
    for encode_format in encode_formats:
        try:
            path = unicodedata.normalize(encode_format, img)
            with open(path, "rb") as stream:
                body = stream.read()
                break
        except IOError:
            pass
    else:
        raise IOError(f"{img} not found")
    return body


@pytest.fixture()
def valid_image():
    return get_image(VALID_IMAGE_PATH)


@pytest.fixture()
def svg_image():
    return get_image(SVG_IMAGE_PATH)


@pytest.fixture()
def too_small_image():
    return get_image(TOO_SMALL_IMAGE_PATH)


@pytest.fixture()
def face_image():
    return get_image(TOO_HEAVY_IMAGE_PATH)


@pytest.fixture()
def default_image():
    return get_image(DEFAULT_IMAGE_PATH)


@pytest.fixture()
def alabama1():
    return get_image(ALABAMA1_IMAGE_PATH)


@pytest.fixture()
def space_image():
    return get_image(SPACE_IMAGE_PATH)


@pytest.fixture()
def invalid_quantization():
    return get_image(INVALID_QUANTIZATION_IMAGE_PATH)


@pytest.fixture()
def animated_image():
    return get_image(ANIMATED_IMAGE_PATH)


@pytest.fixture()
def not_so_animated_image():
    return get_image(NOT_SO_ANIMATED_IMAGE_PATH)
