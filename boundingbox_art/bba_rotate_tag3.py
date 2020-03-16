#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import cv2 as cv


def bba_rotate_tag3(
        image,
        p1,
        p2,
        color=(255, 255, 205),
        thickness=None,  # unused
        font=None,  # unused
        text=None,  # unused
        fps=10,
        animation_count=0,
        color2=(205, 255, 255),
        color3=(255, 205, 255),
):
    draw_image = copy.deepcopy(image)

    animation_count = int(135 / fps) * animation_count

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    radius = int((y2 - y1) * (5 / 10))
    ring_thickness = int(radius / 15)
    cv.ellipse(draw_image, (int((x1 + x2) / 2), int(
        (y1 + y2) / 2)), (radius, radius), 0 + animation_count * 1.5, 0, 90,
               color, ring_thickness)

    radius = int((y2 - y1) * (4.5 / 10))
    ring_thickness = int(radius / 15)
    cv.ellipse(draw_image, (int((x1 + x2) / 2), int(
        (y1 + y2) / 2)), (radius, radius), 0 + animation_count * 2.5, 0, 90,
               color2, ring_thickness)

    radius = int((y2 - y1) * (4 / 10))
    ring_thickness = int(radius / 15)
    cv.ellipse(draw_image, (int((x1 + x2) / 2), int(
        (y1 + y2) / 2)), (radius, radius), 0 + animation_count * 3.5, 0, 90,
               color3, ring_thickness)

    return draw_image
