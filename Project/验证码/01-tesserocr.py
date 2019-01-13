import tesserocr

from PIL import Image

image = Image.open('3.jpg')

# 将图片转为灰度图。
image = image.convert('L')
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table,'1')
# image.show()
result = tesserocr.image_to_text(image)
print(result)


# image = image.convert('1')

# image.show()
# result = tesserocr.image_to_text(image)
# print(result)