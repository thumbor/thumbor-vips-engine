#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/thumbor/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com thumbor@googlegroups.com

import pytest
from thumbor.context import Context
from thumbor.engines import BaseEngine

from thumbor_vips_engine.engine import Engine
from thumbor_vips_engine.testing import EngineTestSuite


class VipsEngineTestCase(EngineTestSuite):
    @pytest.fixture(autouse=True)
    def engine(self, context: Context) -> BaseEngine:
        return Engine(context)
