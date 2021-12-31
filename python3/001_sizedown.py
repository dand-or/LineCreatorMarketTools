from io import BytesIO
from PIL import Image
import zipfile
import os
import shutil

COMPRESS_QUALITY = 30

# def sizedown(path):
#     shutil.copy(path, path + '.bk')
#     img = Image.open(path)
#     img_p = img.convert('P')
#     img_p.save(path)

def sizedown(path):
    shutil.copy(path, path + '.bk')
    with open(path, 'rb') as inputfile:
        img = Image.open(inputfile)
        img = img.convert('RGB')
        io = BytesIO()
        img.save(io, 'JPEG', quality = COMPRESS_QUALITY)
    with open(path, mode='wb') as outputfile:
        outputfile.write(io.getvalue())

print("--start--")
sizedown('./a_22.png')
sizedown('./i_22.png')
print("--end😄--")
