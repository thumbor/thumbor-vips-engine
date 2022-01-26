#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/thumbor/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com thumbor@googlegroups.com

import unicodedata
from os.path import abspath, dirname, join
from typing import Optional

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.single_file import SingleFileSnapshotExtension
from thumbor.context import Context
from thumbor.engines import BaseEngine

FACE_IMAGE_PATH = abspath(join(dirname(__file__), "face_photo.jpg"))
DEFAULT_IMAGE_PATH = abspath(join(dirname(__file__), "image.jpg"))


def _get_image(img: str) -> bytes:
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


class JPEGImageExtension(SingleFileSnapshotExtension):
    @property
    def _file_extension(self) -> str:
        return "jpg"


class EngineTestSuite:
    @pytest.fixture(autouse=True)
    def engine(self, context: Optional[Context]) -> Optional[BaseEngine]:
        return None

    @pytest.fixture(autouse=True)
    def context(self) -> Optional[Context]:
        return None

    @pytest.fixture(autouse=True)
    def default_image(self) -> bytes:
        return _get_image(DEFAULT_IMAGE_PATH)

    @pytest.fixture(autouse=True)
    def face_image(self) -> bytes:
        return _get_image(FACE_IMAGE_PATH)

    @pytest.fixture
    def snapshot(self, snapshot: SnapshotAssertion) -> SnapshotAssertion:
        return snapshot.use_extension(JPEGImageExtension)

    def test_can_create_engine(
        self,
        default_image: bytes,
        engine: BaseEngine,
        snapshot: SnapshotAssertion,
    ) -> None:
        engine.create_image(default_image)

        assert engine is not None
        assert engine.image is not None
        contents = engine.read(".jpg", 95)
        assert contents == snapshot

    def test_can_get_size(
        self, engine: BaseEngine, default_image: bytes
    ) -> None:
        engine.create_image(default_image)

        size = engine.size

        assert size == (300, 400)

    def test_can_generate_blue_image(
        self,
        engine: BaseEngine,
        snapshot: SnapshotAssertion,
    ) -> None:
        img = engine.gen_image((40, 30), (0, 0, 255))
        engine.image = img

        assert img is not None
        assert img.width == 40
        assert img.height == 30
        assert engine.read(".jpg", 95) == snapshot

    def test_can_resize(
        self,
        face_image: bytes,
        engine: BaseEngine,
        snapshot: SnapshotAssertion,
    ) -> None:
        engine.create_image(face_image)

        engine.resize(401, 267)

        contents = engine.read(".jpg", 95)
        assert engine.size == (401, 267), engine.size
        assert contents == snapshot

    def test_can_crop(
        self,
        face_image: bytes,
        engine: BaseEngine,
        snapshot: SnapshotAssertion,
    ) -> None:
        engine.create_image(face_image)

        engine.crop(10, 20, 410, 420)

        contents = engine.read(".jpg", 95)
        assert engine.size == (400, 400)
        assert contents == snapshot

    def test_can_flip_horizontally(
        self,
        face_image: bytes,
        engine: BaseEngine,
        snapshot: SnapshotAssertion,
    ) -> None:
        engine.create_image(face_image)

        engine.flip_horizontally()

        contents = engine.read(".jpg", 95)
        assert contents == snapshot

    def test_can_flip_vertically(
        self,
        face_image: bytes,
        engine: BaseEngine,
        snapshot: SnapshotAssertion,
    ) -> None:
        engine.create_image(face_image)

        engine.flip_vertically()

        contents = engine.read(".jpg", 95)
        assert contents == snapshot

    def test_can_get_grayscale_and_not_update_image(
        self,
        face_image: bytes,
        engine: BaseEngine,
        snapshot: SnapshotAssertion,
    ) -> None:
        engine.create_image(face_image)

        image = engine.convert_to_grayscale(False)

        assert image != engine.image
        contents = image.write_to_buffer(".JPEG", Q=95)
        assert contents == snapshot
