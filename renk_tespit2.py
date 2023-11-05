#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
img=cv2.imread("karsiyaka-10-kasim-siyah-ataturk-formasi-331_min.jpeg")
img=cv2.resize(img,(400,300))
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.imshow("image",img)
cv2.imwrite("copy.jpg",img)
cv2.waitKey(500)

cv2.destroyAllWindows()

