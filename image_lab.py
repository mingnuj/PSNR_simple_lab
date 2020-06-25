import cv2
import numpy as np
import os
from collections import defaultdict
from utils import downsampling, upsampling, psnr

image_path = [os.path.join("images", x) for x in os.listdir("images")]

# down to up bilinear cubic
# up do down cubic bilinear

down_interpolation = cv2.INTER_LINEAR
up_interpolation = cv2.INTER_CUBIC

print("filename\tup2down\tdown2up\n")
for path in image_path:
    image = cv2.imread(path)
    up2down = downsampling(upsampling(image, up_interpolation), down_interpolation)
    down2up = upsampling(downsampling(image, down_interpolation), up_interpolation)
    print("{} \t\t {} \t\t {}".format(path[7:], psnr(image, up2down), psnr(image, down2up)))