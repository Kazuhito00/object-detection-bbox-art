#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import numpy as np
import cv2 as cv

from boundingbox_art.cvdrawtext import CvDrawText


def bba_sound_only_monolith(
        image,
        p1,
        p2,
        color=None,  # unused
        thickness=None,  # unused
        font='boundingbox_art/cvdrawtext/font/Chicago.ttf',
        text=None,
        fps=None,  # unused
        animation_count=None,  # unused
        number=1,
):

    draw_image = copy.deepcopy(image)
    image_width, image_height = draw_image.shape[1], draw_image.shape[0]

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    rectangle_width = x2 - x1
    rectangle_height = y2 - y1

    font_size = int((y2 - y1) * (3 / 9))

    cv.rectangle(
        draw_image,
        (x1 - int(rectangle_width / 20), y1 - int(rectangle_height / 20)),
        (x2 + int(rectangle_width / 20), y2 + int(rectangle_height / 20)),
        (35, 24, 22),
        thickness=-1)

    if (font is not None) and (text is not None):
        draw_image = CvDrawText.puttext(
            draw_image, text,
            (int(((x1 + x2) / 2) - (font_size / (3.5 - (len(text) * 0.4)))),
             int(((y1 + y2) / 2) - (font_size / 0.65))), font,
            int(font_size / 2.5), (212, 0, 58))

    draw_image = CvDrawText.puttext(draw_image, str(format(
        number, '02')), (int(((x1 + x2) / 2) - (font_size / 1.6)),
                         int(((y1 + y2) / 2) - (font_size / 0.8))), font,
                                    font_size, (212, 0, 58))
    draw_image = CvDrawText.puttext(
        draw_image, 'SOUND', (int(((x1 + x2) / 2) - (font_size / 1.5)),
                              int(((y1 + y2) / 2) - (font_size / 3.5))), font,
        int(font_size / 2.5), (212, 0, 58))
    draw_image = CvDrawText.puttext(
        draw_image, 'ONLY', (int(((x1 + x2) / 2) - (font_size / 1.9)),
                             int(((y1 + y2) / 2) + (font_size / 10))), font,
        int(font_size / 2.5), (212, 0, 58))

    return draw_image
