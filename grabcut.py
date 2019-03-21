import numpy as np
import cv2
from matplotlib import pyplot as plt
import sys
import os

import subprocess

if __name__ == '__main__' :

	filename = sys.argv[1]

	# get file name without file type
	filenotype = os.path.splitext(filename)[0]
	img = cv2.imread(filename)

	# launch a window to select region to grabcut
	cv2.namedWindow("Image",2)
	r = cv2.selectROI("Image", img, False, False)

	mask = np.zeros(img.shape[:2],np.uint8)

	bgdModel = np.zeros((1,65),np.float64)
	fgdModel = np.zeros((1,65),np.float64)
 
	rect = r
	cv2.grabCut(img,mask,rect,bgdModel,fgdModel,3,cv2.GC_INIT_WITH_RECT)
 
	mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
	img = img*mask2[:,:,np.newaxis]

	outputfile = str(filenotype)+str(r)+'.png'
 
	cv2.imwrite(outputfile, img)

	cv2.imwrite('grabcut-mask.jpg', mask2)

	# generate mask from grabcut output
	cmd = ['/usr/local/bin/mogrify', '-fuzz', '2%', '-fill', 'white', '-opaque', '#060606', 'grabcut-mask.jpg']

	subprocess.call(cmd, shell=False)

	# apply mask using imagemagick
	cmd = ['/usr/local/bin/convert', outputfile, 'grabcut-mask.jpg', '-alpha', 'off', '-compose', 'CopyOpacity', '-composite', '-trim', outputfile]

	subprocess.call(cmd, shell=False)

	# cleanup
	cmd = ['rm', 'grabcut-mask.jpg']

	subprocess.call(cmd, shell=False)
