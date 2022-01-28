#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/thumbor/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com thumbor@googlegroups.com

import unicodedata
from os.path import abspath, dirname, join
from typing import Optional, Tuple

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.single_file import SingleFileSnapshotExtension
from thumbor.config import Config
from thumbor.context import Context, ServerParameters
from thumbor.engines import BaseEngine
from thumbor.importer import Importer

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
    def engine(
        self,
        context: Optional[Context],  # pylint: disable=unused-argument
    ) -> BaseEngine:
        return None

    @pytest.fixture(autouse=True)
    def config(self) -> Config:
        return Config()

    @pytest.fixture(autouse=True)
    def context(self, config: Config) -> Context:
        importer = Importer(config)
        importer.import_modules()
        server = ServerParameters(
            8889, "localhost", "thumbor.conf", None, "info", None
        )
        server.security_key = config.SECURITY_KEY

        return Context(server, config, importer)

    @pytest.fixture(autouse=True)
    def default_image(self) -> bytes:
        return _get_image(DEFAULT_IMAGE_PATH)

    @pytest.fixture(autouse=True)
    def face_image(self) -> bytes:
        return _get_image(FACE_IMAGE_PATH)

    @pytest.fixture
    def snapshot(self, snapshot: SnapshotAssertion) -> SnapshotAssertion:
        return snapshot.use_extension(JPEGImageExtension)

    def test_can_create_image(
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

    @pytest.mark.parametrize(
        "buffer",
        [
            None,
            "",
        ],
    )
    def test_create_image_fails_with_invalid_buffer(
        self,
        engine: BaseEngine,
        buffer: Optional[bytes],
    ) -> None:
        try:
            engine.create_image(buffer)
            raise AssertionError("Should not have gotten this far")
        except RuntimeError as error:
            assert str(error) == "Image buffer can't be null or empty.", str(
                error
            )

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

    def test_can_get_size(
        self, engine: BaseEngine, default_image: bytes
    ) -> None:
        engine.create_image(default_image)

        size = engine.size

        assert size == (300, 400)

    def test_size_fails_if_no_image_created(self, engine: BaseEngine) -> None:
        try:
            engine.size  # pylint: disable=pointless-statement
            raise AssertionError("Should not have gotten this far")
        except RuntimeError as error:
            assert (
                str(error) == "Image must be loaded before verifying size."
            ), str(error)

    @pytest.mark.parametrize(
        "dimensions,expected",
        [
            ((10, 20, 410, 420), (400, 400)),
            ((0, 0, 0, 0), (800, 533)),
            ((300, 300, 200, 200), (800, 533)),
        ],
    )
    def test_can_crop(
        self,
        face_image: bytes,
        engine: BaseEngine,
        snapshot: SnapshotAssertion,
        dimensions: Tuple[int, int, int, int],
        expected: Tuple[int, int],
    ) -> None:
        engine.create_image(face_image)  # 800x533

        engine.crop(*dimensions)

        contents = engine.read(".jpg", 95)
        assert engine.size == expected
        assert contents == snapshot

    @pytest.mark.parametrize(
        "dimensions,expected",
        [
            ((800, 533), (800, 533)),
            ((401, 267), (401, 267)),
            ((100, 400), (100, 67)),
            ((0, 0), (800, 533)),
            ((0, 1), (1, 1)),
            ((1, 0), (1, 1)),
        ],
    )
    def test_can_resize(
        self,
        face_image: bytes,
        engine: BaseEngine,
        snapshot: SnapshotAssertion,
        dimensions: Tuple[int, int],
        expected: Tuple[int, int],
    ) -> None:
        engine.create_image(face_image)

        engine.resize(dimensions[0], dimensions[1])

        contents = engine.read(".jpg", 95)
        assert engine.size == expected, engine.size
        assert (
            contents == snapshot
        ), f"Snapshot failed for resize to {dimensions}"

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
