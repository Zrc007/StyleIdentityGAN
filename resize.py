import os
import cv2 
path = r"./fid/cas/our/"
for filename in os.listdir(path):
    print (filename)
    image=cv2.imread(path + filename)
    res=cv2.resize(image,(512,512),interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(path + filename, res)