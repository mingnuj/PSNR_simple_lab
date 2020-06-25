import cv2
from collections import defaultdict
from utils import downsampling, upsampling, psnr

down_interpolation = {"Nearest": cv2.INTER_NEAREST, "Bilinear": cv2.INTER_LINEAR}
up_interpolation = {"Cubic": cv2.INTER_CUBIC, "Bilinear": cv2.INTER_LINEAR}

origin_image = cv2.imread("images/cat_1920x1280.jpg")

down2up = defaultdict()
up2down = defaultdict()

for i in down_interpolation.keys():
    for j in up_interpolation.keys():
        down2up["{}_{}".format(i, j)] = upsampling(downsampling(origin_image, down_interpolation[i]), up_interpolation[j])
        up2down["{}_{}".format(j, i)] = downsampling(upsampling(origin_image, up_interpolation[j]), down_interpolation[i])

for d2u in down2up.keys():
    print("Downsampling and upsampling\nMethod: {}, PSNR: {}\n".format(d2u, psnr(origin_image, down2up[d2u])))

for u2d in up2down.keys():
    print("Upsampling and downsampling\nMethod: {}, PSNR: {}\n".format(u2d, psnr(origin_image, up2down[u2d])))

