# -*- encoding: utf-8 -*-
#
# Created on: Thu Sep 28 02:17:05 2017

import os
import atx

d = atx.connect(os.getenv("SERIAL"))
d.resolution = (1920, 1080)

while True:
    d.keep_screen()
    
    # try replay
    if d.click_exists("imgs/replay.1920x1080.png") == None:
        # still available?
        if d.exists("imgs/not_available.1920x1080.png"):
            d.delay(30.0)
        # mission start
        elif d.click_exists("imgs/start.1920x1080.png") != None:
            d.delay(1.0)
            d.free_screen()
            d.keep_screen()
            # check if hidden ticket is available
            if d.exists("imgs/hidden_available.1920x1080.png"):
                d.click_exists("imgs/yes_green.1920x1080.png")
            d.delay(60.0)
        # timeline start
        elif d.click_exists("imgs/fight.1920x1080.png") != None:
            d.delay(90.0)
    
    # wait and play again
    d.free_screen()
    d.delay(5.0)