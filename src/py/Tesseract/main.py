from PIL import Image
import pytesseract
import numpy as np
import pathlib

dir = f"{pathlib.Path.home()}/Downloads"

filename = f"{dir}/image_01.jpg"
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)

print(text)