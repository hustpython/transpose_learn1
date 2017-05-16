import glob
import numpy as np 
from cv2 import imread,imwrite,resize
import cv2
imgs = []
i =0
for fn in glob.glob("./wdly/*jpeg"):
    i+=1
    image =imread(fn)
    res =resize(image,(320,180),interpolation=cv2.INTER_CUBIC)
    cv2.imshow('iker',res)
    cv2.imwrite('./wdly_test/{}.jpeg'.format(i),res)
    #cv2.imshow('image',image)
    #cv2.waitKey(0)
    #imgs.append(imread(fn,-1))
#print imgs[0].shape
#img =np.concatenate(imgs,0)
#print img.shape
for fn in glob.glob("./wdly_test/[0-9]*jpeg"):
    print fn
    imgs.append(imread(fn,-1))
#print imgs[0].shape
img =np.concatenate(imgs,0)
img1 =img.reshape(4,3,180,320,3)
img0 =img1.swapaxes(2,1).reshape(720,960,3)
#print img1[0,1].shape\
cv2.imwrite('./wdly_test/img1.jpeg',img0)
img2 =img1.swapaxes(1,2).reshape(720,960,3)
#cv2.imwrite('./wdly_test/img2.jpeg',img2)
img3 = img.reshape(3,4,180,320,3)\
          .transpose(1,2,0,3,4) \
          .reshape(540,1280,3)
cv2.imwrite('./wdly_test/img3.jpeg',img3)
img1 =img.reshape(4,3,180,320,3)
mask =np.ones(img1.shape[:-1],dtype = bool)
mask[:,:,2:-2,2:-2]=False
img1[mask]= (255,255,0)
img4 =img1.swapaxes(1,2).reshape(720,960,3)
cv2.imwrite('./wdly_test/img4.jpeg',img4)