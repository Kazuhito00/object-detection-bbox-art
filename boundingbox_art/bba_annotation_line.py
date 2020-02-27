#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import cv2 as cv

from boundingbox_art.cvdrawtext import CvDrawText


def bba_annotation_line(
        image,
        p1,
        p2,
        color=(255, 255, 255),
        thickness=None,  # unused
        font='boundingbox_art/cvdrawtext/font/mplus-1c-regular.ttf',
        text=None,
        fps=None,  # unused
        animation_count=None,  # unused
):

    draw_image = copy.deepcopy(image)

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    rectangle_width = x2 - x1
    rectangle_height = y2 - y1

    font_size = int(rectangle_width * (1 / 10))

    cv.circle(
        draw_image, (int((x1 + x2) / 2), int((y1 + y2) / 2)),
        int(rectangle_width / 40),
        color,
        thickness=-1)
    cv.line(draw_image, (int((x1 + x2) / 2), int((y1 + y2) / 2)),
            (x2 - int(rectangle_width / 10), y1 + int(rectangle_height / 10)),
            color, int(rectangle_width / 80))
    cv.line(draw_image,
            (x2 - int(rectangle_width / 10), y1 + int(rectangle_height / 10)),
            (x2 + int(rectangle_width / 2), y1 + int(rectangle_height / 10)),
            color, int(rectangle_width / 80))

    if (font is not None) and (text is not None):
        draw_image = CvDrawText.puttext(
            draw_image, text,
            (x2 - int(rectangle_width / 10),
             y1 + int(rectangle_height / 10) - int(font_size * 1.5)), font,
            font_size, color)

    return draw_image
