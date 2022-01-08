import numpy as np
import cv2

def img_bytes_2_cv(img_bytes):
    '''将图像字节流转换为cv2数组(BGR)格式'''
    nparr = np.fromstring(img_bytes, np.uint8)
    if nparr.any():
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img
    else:
        return None

def img_cv_2_bytes(img_cv):
    '''将cv2数组(BGR)转换为图像字节流'''
    img_encode = cv2.imencode('.jpg', img_cv)[1]
    data_encode = np.array(img_encode)
    str_encode = data_encode.tostring()
    return str_encode