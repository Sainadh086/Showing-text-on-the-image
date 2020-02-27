#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:50:59 2020

@author: sainadh
"""

import cv2

img = cv2.imread('simpsons_frame0.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
l1 = [i for i in range(26)]
l1 = set(l1)
row_count = img_gray.shape[0]
column_count = img_gray.shape[1]
for i in range(row_count):
    for j in range(column_count):
        if(img_gray[i][j] not in l1):
            img_gray[i][j] = 255
import matplotlib.pyplot as plt
plt.imshow(img_gray)
cv2.imwrite('img_text.png',img_gray)

