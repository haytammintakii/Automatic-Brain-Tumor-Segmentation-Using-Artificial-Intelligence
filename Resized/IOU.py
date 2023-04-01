# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 04:42:30 2021

@author: Romil
"""
import numpy as np
import cv2

gt=cv2.imread("Mask8.PNG",0)
seg=cv2.imread("predict8.PNG",0)
a = np.where(gt!=255, 1, gt)
a = np.where(gt==255, 0, a)
b = np.where(seg!=255, 1, seg)
b = np.where(seg==255, 0, b)
result1=a
result2=b
intersection = np.logical_and(result1, result2)
union = np.logical_or(result1, result2)
iou_score = np.sum(intersection) / np.sum(union)
print('IOU',iou_score*100)