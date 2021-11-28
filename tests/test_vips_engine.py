#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor vips engine
# https://github.com/thumbor/thumbor-vips-engine

# Apache License
# Version 2.0, January 2004
# http://www.apache.org/licenses/

from thumbor_vips_engine.engine import Engine


def test_can_create_image(context, default_image, snapshot):
    engine = Engine(context)

    engine.create_image(default_image)

    assert engine is not None
    assert engine.image is not None
    contents = engine.read(".jpg", 95)
    assert contents == snapshot


def test_can_get_size(context, default_image):
    engine = Engine(context)
    engine.create_image(default_image)
    assert engine is not None
    assert engine.image is not None

    size = engine.size

    assert size == (300, 400)


def test_can_resize(context, default_image, snapshot):
    engine = Engine(context)
    engine.create_image(default_image)
    assert engine is not None
    assert engine.image is not None

    engine.resize(300, 200)

    contents = engine.read(".jpg", 95)
    assert contents == snapshot


def test_can_crop(context, default_image, snapshot):
    engine = Engine(context)
    engine.create_image(default_image)
    assert engine is not None
    assert engine.image is not None

    engine.crop(10, 20, 200, 350)

    contents = engine.read(".jpg", 95)
    assert contents == snapshot
    assert engine.size == (190, 330)


def test_can_flip_horizontally(context, face_image, snapshot):
    engine = Engine(context)
    engine.create_image(face_image)
    assert engine is not None
    assert engine.image is not None

    engine.flip_horizontally()

    contents = engine.read(".jpg", 95)
    assert contents == snapshot


def test_can_flip_vertically(context, face_image, snapshot):
    engine = Engine(context)
    engine.create_image(face_image)
    assert engine is not None
    assert engine.image is not None

    engine.flip_vertically()

    contents = engine.read(".jpg", 95)
    assert contents == snapshot


def test_can_get_grayscale_and_not_update_image(context, face_image, snapshot):
    engine = Engine(context)
    engine.create_image(face_image)
    assert engine is not None
    assert engine.image is not None

    image = engine.convert_to_grayscale(False)

    assert image != engine.image
    contents = image.write_to_buffer(".JPEG", Q=95)
    assert contents == snapshot


def test_can_generate_image(context, snapshot):
    engine = Engine(context)
    assert engine is not None

    image = engine.gen_image((300, 200), (0, 255, 0))

    assert image != engine.image
    contents = image.write_to_buffer(".JPEG", Q=95)
    assert contents == snapshot
