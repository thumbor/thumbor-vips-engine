#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor vips engine
# https://github.com/thumbor/thumbor-vips-engine

# Apache License
# Version 2.0, January 2004
# http://www.apache.org/licenses/

import pytest

from thumbor_vips_engine.engine import Engine


@pytest.mark.asyncio
async def test_can_create_image(context, default_image, snapshot):
    engine = Engine(context)

    engine.create_image(default_image)

    assert engine is not None
    assert engine.image is not None
    contents = engine.read(".jpg", 95)
    assert contents == snapshot


@pytest.mark.asyncio
async def test_can_get_size(context, default_image):
    engine = Engine(context)
    engine.create_image(default_image)
    assert engine is not None
    assert engine.image is not None

    size = engine.size

    assert size == (300, 400)


@pytest.mark.asyncio
async def test_can_resize(context, default_image, snapshot):
    engine = Engine(context)
    engine.create_image(default_image)
    assert engine is not None
    assert engine.image is not None

    engine.resize(300, 200)

    contents = engine.read(".jpg", 95)
    assert contents == snapshot


@pytest.mark.asyncio
async def test_can_crop(context, default_image, snapshot):
    engine = Engine(context)
    engine.create_image(default_image)
    assert engine is not None
    assert engine.image is not None

    engine.crop(10, 20, 200, 350)

    contents = engine.read(".jpg", 95)
    assert contents == snapshot
    assert engine.size == (190, 330)
