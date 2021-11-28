#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor aws extensions
# https://github.com/thumbor/thumbor-aws

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2021 Bernardo Heynemann heynemann@gmail.com

from typing import Union

import pyvips
from pyvips.enums import Direction
from thumbor.engines import BaseEngine

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

    #  def __init__(self, context):
    #  super().__init__(context)

    @property
    def size(self) -> tuple[int]:
        if self.image is None:
            raise RuntimeError("Image must be loaded before verifying size.")

        return (self.image.width, self.image.height)

    def gen_image(
        self, size: tuple[int], color: Union[int, tuple[int]]
    ) -> pyvips.Image:
        image = pyvips.Image.Black(size[0], size[1], bands=3)
        image = image.draw_rect(color, 0, 0, size[0], size[1], fill=True)
        return image

    def create_image(self, buffer) -> pyvips.Image:
        self.image = pyvips.Image.new_from_buffer(
            buffer, "", access="sequential"
        )
        return self.image

    def crop(self, left, top, right, bottom):
        self.image = self.image.crop(left, top, right - left, bottom - top)

    def resize(self, width, height):
        if width > height:
            scale = height / self.image.height
        elif height > width:
            scale = width / self.image.width
        else:
            scale = 1.0

        self.image = self.image.resize(scale)

    def focus(self, points):
        pass

    def flip_horizontally(self):
        self.image = self.image.flip(Direction.HORIZONTAL)

    def flip_vertically(self):
        self.image = self.image.flip(Direction.VERTICAL)

    def rotate(self, degrees):
        """
        Rotates the image the given amount CCW.
        :param degrees: Amount to rotate in degrees.
        :type amount: int
        """
        raise NotImplementedError()

    def read_multiple(self, images, extension=None):
        raise NotImplementedError()

    def read(self, extension, quality):
        return self.image.write_to_buffer(FORMATS[extension], Q=quality)

    def get_image_data(self):
        raise NotImplementedError()

    def set_image_data(self, data):
        raise NotImplementedError()

    def get_image_mode(self):
        """Possible return values should be: RGB, RBG, GRB, GBR,
        BRG, BGR, RGBA, AGBR, ..."""
        raise NotImplementedError()

    def paste(self, other_engine, pos, merge=True):
        raise NotImplementedError()

    def enable_alpha(self):
        raise NotImplementedError()

    def image_data_as_rgb(self, update_image=True):
        raise NotImplementedError()

    def strip_exif(self):
        pass

    def convert_to_grayscale(
        self, update_image=True, alpha=True
    ) -> pyvips.Image:
        image = self.image.colourspace("b-w")
        if update_image:
            self.image = image

        # [TODO]: keep alpha

        return image

    def draw_rectangle(self, x, y, width, height):
        raise NotImplementedError()

    def strip_icc(self):
        pass

    def extract_cover(self):
        raise NotImplementedError()

    def has_transparency(self):
        raise NotImplementedError()

    def cleanup(self):
        pass
