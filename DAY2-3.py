 ggg# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:00:58 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

w = 80
h = 80
l = 80

x,y,z = mc.player.getTilePos()
mc.setBlocks(x,y,z,x+w,y+h,z+l,1,2)
mc.setBlocks(x+1,y+1,z+1,
             x+w-1,y+h-1,z+l-1,0)