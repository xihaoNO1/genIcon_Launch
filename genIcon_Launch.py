#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from PIL import  Image

def getIconSize():
    return [(40,40),(60,60),(80,80),(58,58),(87,87),(120,120),(180,180),(48,48),(72,72),(96,96),(114,114),(1024,1024)]

def getLaunchImageSize():
    return [(320,480),(640,960),(640,1136),(750,1334),(1242,2208),(1125,2436),(480,800),(720,1280),(1080,1920)]


def genIcon():
    iconArr = getIconSize()
    for size in iconArr:
        genImg(size)

def genLaunchImg():
    launchArr = getLaunchImageSize()
    for size in launchArr:
        genImg(size)

def genImg(size):
    '''根据max的启动图标生成大小为size的启动图'''
    path = os.getcwd()
    path_max = path+'/max.png'
    img_max = Image.open(path_max).convert('RGBA')
    if int(size[0]) == int(size[1]):
        img_new = img_max.resize(size,Image.ANTIALIAS)
    else:
        img_max = img_max.resize((int(size[0]/2),int(size[0]/2)),Image.ANTIALIAS)
        img_new = Image.new('RGB', size, '#ffffff')
        location = (int(size[0]/4), int(size[1]/2 - size[0]/4))
        img_new.paste(img_max, location)
    img_new.save('./%s*%s.png' % size,quality=95)

def getAllImg():
    genIcon()
    genLaunchImg()


if __name__ == '__main__':
    getAllImg()
