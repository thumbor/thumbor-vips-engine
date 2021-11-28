#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor vips engine
# https://github.com/thumbor/thumbor-vips-engine

# Apache License
# Version 2.0, January 2004
# http://www.apache.org/licenses/

import pytest
from preggy import expect

from thumbor_vips_engine.engine import Engine


@pytest.mark.asyncio
async def test_can_create_image(context, default_image, snapshot):
    engine = Engine(context)

    engine.create_image(default_image)

    expect(engine).not_to_be_null()
    expect(engine.image).not_to_be_null()
    contents = engine.read(".jpg", 95)
    expect(contents).to_equal(snapshot)


@pytest.mark.asyncio
async def test_can_resize(context, default_image, snapshot):
    engine = Engine(context)
    engine.create_image(default_image)

    engine.resize(300, 200)

    expect(engine).not_to_be_null()
    expect(engine.image).not_to_be_null()
    contents = engine.read(".jpg", 95)
    expect(contents).to_equal(snapshot)
