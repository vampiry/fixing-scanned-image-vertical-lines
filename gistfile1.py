#需要python版本3.9以上

import cv2
import numpy as np

# 讀取影像
img = cv2.imread('image.jpg')

# 將影像分割為三個通道
b, g, r = cv2.split(img)

# 對每個通道分別用閾值處理來找出光帶所在的位置
thresh_b = cv2.inRange(b, 200, 255)
thresh_g = cv2.inRange(g, 200, 255)
thresh_r = cv2.inRange(r, 200, 255)

# 對每個通道分別用雙邊濾波來減少光帶的亮度
bilateral_b = cv2.bilateralFilter(b, 15, 50, 15)
bilateral_g = cv2.bilateralFilter(g, 15, 50, 15)
bilateral_r = cv2.bilateralFilter(r, 15, 50, 15)

# 對每個通道分別用遮罩來合併原始影像和濾波後的影像
mask_b = thresh_b > 0
mask_g = thresh_g > 0
mask_r = thresh_r > 0
result_b = b.copy()
result_g = g.copy()
result_r = r.copy()
result_b[mask_b] = bilateral_b[mask_b]
result_g[mask_g] = bilateral_g[mask_g]
result_r[mask_r] = bilateral_r[mask_r]

# 將三個通道合併為一個全彩影像
result = cv2.merge([result_b, result_g, result_r])
cv2.imwrite('result.jpg', result)

# 顯示結果
cv2.imshow('Original', img)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

