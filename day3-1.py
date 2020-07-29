# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 09:33:48 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    hits = mc.events.pollBlockHits()
    
    if len(hits)>0:
        block = hits[0]
        x,y,z = block.pos.x,block.pos.y,block.pos.z
        mc.setBlock(x,y,z,41)