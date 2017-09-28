# -*- encoding: utf-8 -*-
#
# Created on: Wed Sep 27 19:14:47 2017

import os
import atx

d = atx.connect(os.getenv("SERIAL"))
d.resolution = (1920, 1080)

while True:
    d.keep_screen()
    
    # try next
    if d.click_exists("imgs/next.1920x1080.png") != None:
        d.delay(10.0)
    # enter the lobby
    elif d.exists("imgs/lobby.1920x1080.png"):
        d.delay(1.0)
        d.free_screen()
        # get awards
        if d.click_exists("imgs/get_award.1920x1080.png") != None:
            d.click_image("imgs/fetch.1920x1080.png", timeout=10.0, safe=True)
            d.click_image("imgs/yes.1920x1080.png", timeout=10.0, safe=True)
        # choose a hero and start
        else:
            d.click(118, 900)
            d.click_image("imgs/match_start.1920x1080.png", timeout=10.0, safe=True)
            d.delay(30.0)
    
    # wait and play again
    d.free_screen()
    d.delay(5.0)