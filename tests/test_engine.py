#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/thumbor/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com thumbor@googlegroups.com

from typing import Optional

import pytest
from thumbor.config import Config
from thumbor.context import Context, ServerParameters
from thumbor.engines import BaseEngine
from thumbor.importer import Importer

from thumbor_vips_engine.engine import Engine
from thumbor_vips_engine.testing import EngineTestSuite


class VipsEngineTestCase(EngineTestSuite):
    @pytest.fixture(autouse=True)
    def engine(self, context: Optional[Context]) -> Optional[BaseEngine]:
        return Engine(context)

    @pytest.fixture(autouse=True)
    def context(self) -> Optional[Context]:
        cfg = Config()

        importer = Importer(cfg)
        importer.import_modules()
        server = ServerParameters(
            8889, "localhost", "thumbor.conf", None, "info", None
        )
        server.security_key = cfg.SECURITY_KEY

        return Context(server, cfg, importer)
