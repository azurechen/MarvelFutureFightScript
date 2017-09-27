# -*- encoding: utf-8 -*-
#
# Created on: Thu Sep 28 02:17:05 2017

import os
import atx

d = atx.connect(os.getenv("SERIAL"))
d.resolution = (1920, 1080)

# any mission
while True:
    if d.exists("imgs/start.1920x1080.png"):
        d.click_image("imgs/start.1920x1080.png")
        d.delay(25.0)
    elif d.exists("imgs/replay.1920x1080.png"):
        d.click_image("imgs/replay.1920x1080.png")
    d.delay(5.0)