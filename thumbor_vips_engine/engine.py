#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor aws extensions
# https://github.com/thumbor/thumbor-aws

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2021 Bernardo Heynemann heynemann@gmail.com

from typing import List, Optional, Tuple, Union

import pyvips
from pyvips.enums import Direction
from thumbor.engines import BaseEngine
from thumbor.point import FocalPoint

FORMATS = {
    ".tif": "PNG",  # serve tif as png
    ".jpg": ".JPEG",
    ".jpeg": ".JPEG",
    ".gif": "GIF",
    ".png": "PNG",
    ".webp": "WEBP",
}


class Engine(BaseEngine):  # pylint: disable=too-many-public-methods
    image: pyvips.Image = None

    def create_image(self, buffer: bytes) -> pyvips.Image:
        if buffer is None or buffer == "":
            raise RuntimeError("Image buffer can't be null or empty.")

        # TODO: Get from thumbor context whether access needs to be random
        self.image = pyvips.Image.new_from_buffer(buffer, "", access="random")

        return self.image

    def gen_image(
        self, size: Tuple[int, int], color: Union[int, Tuple[int, int, int]]
    ) -> pyvips.Image:
        image = pyvips.Image.Black(size[0], size[1], bands=3)
        image = image.draw_rect(color, 0, 0, size[0], size[1], fill=True)

        return image

    @property
    def size(self) -> Tuple[int, int]:
        if self.image is None:
            raise RuntimeError("Image must be loaded before verifying size.")

        return (int(self.image.width), int(self.image.height))

    def crop(self, left: int, top: int, right: int, bottom: int) -> None:
        if right <= left or bottom <= top:
            return

        self.image = self.image.crop(left, top, right - left, bottom - top)

    def resize(self, width: int, height: int) -> None:
        scale = 1.0

        if width == 0:
            width = self.size[0]

        if height == 0:
            height = self.size[1]

        if width > height:
            scale = float(height) / self.image.height
        elif height > width:
            scale = float(width) / self.image.width

        self.image = self.image.resize(scale)

    def focus(self, points: List[FocalPoint]) -> None:
        pass

    def flip_horizontally(self) -> None:
        self.image = self.image.flip(Direction.HORIZONTAL)

    def flip_vertically(self) -> None:
        self.image = self.image.flip(Direction.VERTICAL)

    def rotate(self, degrees: int) -> None:
        """
        Rotates the image the given amount CCW.
        :param degrees: Amount to rotate in degrees.
        :type amount: int
        """
        self.image = self.image.rot(degrees)

    def read_multiple(
        self, images: List[bytes], extension: Optional[str] = None
    ) -> bytes:
        raise NotImplementedError()

    def read(self, extension: str, quality: int) -> bytes:
        return bytes(self.image.write_to_buffer(FORMATS[extension], Q=quality))

    def get_image_data(self) -> bytes:
        raise NotImplementedError()

    def set_image_data(self, data: bytes) -> None:
        raise NotImplementedError()

    def get_image_mode(self) -> str:
        """Possible return values should be: RGB, RBG, GRB, GBR,
        BRG, BGR, RGBA, AGBR, ..."""
        raise NotImplementedError()

    def paste(
        self, other_engine: BaseEngine, pos: int, merge: bool = True
    ) -> None:
        raise NotImplementedError()

    def enable_alpha(self) -> None:
        raise NotImplementedError()

    def image_data_as_rgb(
        self, update_image: bool = True
    ) -> Tuple[str, bytes]:
        raise NotImplementedError()

    def strip_exif(self) -> None:
        pass

    def convert_to_grayscale(
        self, update_image: bool = True, alpha: bool = True
    ) -> pyvips.Image:
        image = self.image.colourspace("b-w")

        if update_image:
            self.image = image

        # [TODO]: keep alpha

        return image

    def draw_rectangle(self, x: int, y: int, width: int, height: int) -> None:
        raise NotImplementedError()

    def strip_icc(self) -> None:
        pass

    def extract_cover(self) -> None:
        raise NotImplementedError()

    def has_transparency(self) -> bool:
        raise NotImplementedError()

    def cleanup(self) -> None:
        pass
