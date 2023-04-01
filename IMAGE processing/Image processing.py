import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.io import imread
from skimage.color import rgb2gray
from skimage import exposure

img = cv2.imread("MRi4.png")
#plt.imshow(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#plt.imshow(gray,cmap ='gray')
ret, thresh = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)
ret, markers = cv2.connectedComponents(thresh)
marker_area = [np.sum(markers==m) for m in range(np.max(markers)) if m!=0] 
largest_component = np.argmax(marker_area)+1                    
brain_mask = markers==largest_component
brain_out = img.copy()
### Skull Masking
brain_out[brain_mask==False] = (0,0,0)
#plt.figure(figsize=(20, 15))
#plt.subplot(331)
plt.imshow(brain_out)
#%%

p2, p98 = np.percentile(brain_out, (97,98))
brain_out = exposure.rescale_intensity(brain_out, in_range=(p2, p98))
plt.imshow(brain_out)

#%%
from skimage.morphology import binary_opening, binary_closing, binary_erosion, binary_dilation, disk
im = rgb2gray(brain_out)
im[im <= 0.5] = 0
im[im > 0.5] = 1
im1 = binary_opening(im, disk(3))
plt.imshow(im1, cmap ='gray')





#%%


from skimage.morphology import remove_small_objects
rso_1 = rgb2gray(im1)
rso_1[rso_1 > 0.5] = 1 # create binary image by thresholding with fixed threshold
0.5
rso_1[rso_1 <= 0.5] = 0
#rso_1 = rso_1.astype(np.bool)

i = 2
for osz in [30]:
    im_rso_1 = remove_small_objects(rso_1, osz, connectivity=1)
   
    plt.figure(figsize=(20, 15))
    plt.subplot(334)
    
    plt.imshow(im_rso_1,cmap = 'gray')
    
"""
plt.imsave('MASK4.png',im_rso_1, cmap = 'gray')
"""
#%%
    
from skimage.morphology import remove_small_objects
im_2 = rgb2gray(im_rso_1)
im_2[im_2 > 0.5] = 1 # create binary image by thresholding with fixed threshold
0.5
im_2[im_2 <= 0.5] = 0
im_2 = im_2.astype(np.bool)

i = 2
for osz in [800]:
    im_02 = remove_small_objects(im_2, osz, connectivity=1)
   
    plt.figure(figsize=(20, 15))
    plt.subplot(334)
    plt.imshow(im_02,cmap = 'gray')    
#%%
#from skimage.color import rgb2gray
#
#from skimage.morphology import convex_hull_image
#from matplotlib import pyplot as plt
#im = rgb2gray(im_2)
#threshold = 0.5
#im[im < threshold] = 0 # convert to binary image
#im[im >= threshold] = 1
#chull = convex_hull_image(im)
#plt.imshow(chull,cmap ='gray')
#%%%
from skimage.morphology import binary_opening, binary_closing, binary_erosion, binary_dilation, disk
im = rgb2gray(im_rso_1)
im[im <= 0.5] = 0
im[im > 0.5] = 1
im2 = binary_closing(im, disk(20))
plt.imshow(im2, cmap ='gray')
"""
plt.imsave('Test_image/Test_13.png',im2, cmap = 'gray')
"""

    
#%%
    
import numpy as np
dil=im_02.astype(np.uint8)
kernel = np.ones((3,3),np.uint8)
mask = cv2.dilate(dil,kernel,iterations = 8)
plt.figure(figsize=(20, 15))
plt.subplot(336)
plt.imshow(mask,cmap ='gray')
"""
plt.imsave('MASKS/Series_5001_AX T2W_new 1 (10).png',mask, cmap = 'gray')
"""