"""用Pythonp批量裁剪图片"""
 
from PIL import Image
import matplotlib.pyplot as plt
import os
 
# 定义待批量裁剪图像的路径地址
IMAGE_INPUT_PATH = 'E:/Project/Python/1'
# 定义裁剪后的图像存放地址
IMAGE_OUTPUT_PATH = 'E:/Project/Python/2'
# 定义裁剪图片左、上、右、下的像素坐标，具体位置自行调整
BOX_LEFT, BOX_UP, BOX_RIGHT, BOX_DOWN = 1000, 0, 2100, 2848
 
for each_image in os.listdir(IMAGE_INPUT_PATH):
    # 每个图像全路径
    image_input_fullname = IMAGE_INPUT_PATH + '/' + each_image
    # PIL库打开每一张图像
    img = Image.open(image_input_fullname)
    plt.figure("image_input_fullname")
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.axis('off')
    print(img.format, img.size, img.mode)
    # 从原始图像返回一个矩形区域，区域是一个4元组定义左上右下像素坐标
    box = (BOX_LEFT, BOX_UP, BOX_RIGHT + BOX_LEFT, BOX_DOWN + BOX_UP)
    # 进行roi裁剪
    roi_area = img.crop(box)
    plt.subplot(1, 2, 2)

    plt.imshow(roi_area)
    plt.axis('off')
    print(roi_area.format, roi_area.size, roi_area.mode)
    plt.show()
    # 裁剪后每个图像的路径+名称
    image_output_fullname = IMAGE_OUTPUT_PATH + "/" + each_image
    # 存储裁剪得到的图像
    roi_area.save(image_output_fullname)
    print('{0} crop done.'.format(each_image))