import cv2
import numpy as np
import math

def downsampling(image, interpolation):
    return cv2.resize(image, None, fx=0.25, fy=0.25, interpolation=interpolation)

def upsampling(image, interpolation):
    return cv2.resize(image, None, fx=4, fy=4, interpolation=interpolation)

def psnr(img1, img2):
    mse = np.mean( (img1 - img2) ** 2 )
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))