# PSNR_simple_lab
Expreiment on the effect of upsampling and downsampling on PSNR

## interpolation_lab
Resizing ratio 4 times  
Used cat image for experiment  
- Downsampling -> Upsampling  
Rows: downsampling / Cols: upsampling  

| Methods   | Cubic     | Bilinear  |
|:---------:|:---------:|:---------:|
| Nearest   | 33.98     | 34.34     |
| Bilinear  | 36.40     | **36.41** |


- Upsampling -> Downsampling  
Rows: upsampling / Cols: downsampling  

| Methods   | Nearest    | Bilinear |
|:---------:|:---------:|:---------:|
| Cubic     | 39.48     | **59.41** |
| Bilinear  | 39.51     | 48.86     |

## image_lab
Using bilinear interpolation for downsampling and cubic interpolation for upsampling.
```
sunset_1920x1280.jpg      62.620354074876175  39.23925907715897
landscape_1920x1280.jpg   51.1161958904362    32.91367831781533
cat_1920x1280.jpg         59.41750016814367   36.409979974051566
cornflower_1920x1280.jpg  65.49260971234617   41.86114158199391
away_1920x1280.jpg 		    42.40824736366037 	29.4809014555575
```
If image is complex, PSNR is small.
