# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 02:05:43 2021

@author: Romil
"""

import numpy as np
import cv2
import os
i="res"
n='t'
d='.jpg'
path=i+n+d
img=cv2.imread(path,1)
#%%

#%%
p=2
s=4
img1=img*(p)
img2=img*(s)
#img=cv2.resize(img, (600, 512))
#img1=cv2.resize(img1, (600, 512))  
cv2.imshow("Expoure time 4",img2)
cv2.imshow("Expoure time 2",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
#%%
cv2.imwrite("Expoure time1by2.jpg",img2)
cv2.imwrite("Expoure time2.jpg",img1)