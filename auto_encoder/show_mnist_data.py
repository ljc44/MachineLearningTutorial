#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2.cv2 as cv2
# Created by C.L.Wang
#
import matplotlib
import scipy.misc as misc

matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

image = mnist.train.images

pixels = np.array(image[0])  # 784维的数据
pixels = pixels.reshape((28, 28))  # 转换成28*28维的矩阵

# -------------------- scipy模式 -------------------- #
misc.imsave('./IMAGE_data/scipy.png', pixels)  # scipy的存储模式
# -------------------- scipy模式 -------------------- #

# -------------------- matplotlib模式 -------------------- #
plt.gray()  # 转变为灰度图片
plt.imshow(pixels)
plt.savefig("./IMAGE_data/plt.png")
# plt.show()
# -------------------- matplotlib模式 -------------------- #

# -------------------- opencv模式 -------------------- #
pixels = pixels * 255  # 数据是0~1的浮点数
cv2.imwrite("./IMAGE_data/opencv.png", pixels)
# cv2.imshow('hah', pixels)
# cv2.waitKey(0)
# -------------------- opencv模式 -------------------- #
