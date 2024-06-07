from PIL import Image
from django.test import TestCase
from Tool import ImageByte

# Create your tests here.

image_path = "1.jpg"
image = Image.open(image_path)
byte_data = ImageByte.image2byte(image)
print(byte_data)
print(type(byte_data))
image2 = ImageByte.byte2image(byte_data)
image2.show()
