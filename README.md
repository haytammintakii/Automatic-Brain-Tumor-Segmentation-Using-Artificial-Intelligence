# Automatic-Brain-Tumor-Segmentation-Using-Artificial-Intelligence
In this project we made a automatic brain tumor segmentation algorithm using deep learning model Unet model 
Brain tumor segmentation has created interest in research fields in recent decades. 
The precision of accurate segmentation of tumor through naked eye depends on the experience of the radiologist. 
A non-invasive Magnetic Resonance Imaging (MRI) technique is used to look at organs and structures inside human body. 
Despite numerous efforts and encouraging findings in medical imaging field, precise segmentation and abnormality in tissues is still a complex and difficult challenge due to number of potential sizes, position and image intensities of different type of tumor.
Our proposed methodology has two stages, initially the tumor is segmented manually using image processing techniques. The first stage then incorporates with deep learning stage to segment tumor from healthy part of brain. In the first stage we adopted basic thresholding with morphological operations to segment brain tumor as mask image to obtain a ground truth data. 
We trained our Deep Learning U-Net model on these mask images and obtain the segmented result of tumor.
