import io
import base64
from PIL import Image


def image2byte(image):
    '''
    图片转byte
    image: 必须是PIL格式
    image_bytes: 二进制
    '''
    # 创建一个字节流管道
    img_bytes = io.BytesIO()
    # 将图片数据存入字节流管道， format可以按照具体文件的格式填写
    image.save(img_bytes, format="JPEG")
    # 从字节流管道中获取二进制
    image_bytes = img_bytes.getvalue()
    return image_bytes


def byte2image(byte_data):
    '''
    byte转为图片
    byte_data: 二进制
    '''
    image = Image.open(io.BytesIO(byte_data))
    return image
