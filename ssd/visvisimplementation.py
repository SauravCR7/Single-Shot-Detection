# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 21:03:33 2018

@author: Saurav
"""

import imageio
import visvis as vv

reader = imageio.get_reader('<video0>')
t = vv.imshow(reader.get_next_data(), clim=(0, 255))
for im in reader:
    vv.processEvents()
    t.SetData(im)