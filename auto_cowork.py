# -*- encoding: utf-8 -*-
#
# Created on: Wed Sep 27 19:14:47 2017

import os
import atx

d = atx.connect(os.getenv("SERIAL"))
d.resolution = (1920, 1080)

# team game
while True:
    # enter the lobby and choose a hero
    if d.exists("imgs/lobby.1920x1080.png"):
        d.delay(1.0)
        if d.exists("imgs/get_award.1920x1080.png"):
            d.click_image("imgs/get_award.1920x1080.png")
            d.click_image("imgs/fetch.1920x1080.png", timeout=10.0)
            d.click_image("imgs/yes.1920x1080.png", timeout=10.0)
        else:
            d.click(118, 900)
            d.click_image("imgs/match_start.1920x1080.png", timeout=10.0)
            d.delay(30.0)
            d.click_image("imgs/next.1920x1080.png", timeout=60.0)
    d.delay(5.0)