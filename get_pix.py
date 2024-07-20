import numpy as np
from PIL import Image
def get_image(image:str):
    im = Image.open(image)
    white_pix = [i for i in im.getdata() if i == (255,255,255)]
    black_pix = [i for i in im.getdata() if i == (0,0,0)]
    white_count = len(white_pix)
    black_count = len(black_pix)

    return  white_count, black_count


