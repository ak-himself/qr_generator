'''
import qrcode as qr

link = input("link or text : ")
img = qr.make(link)

save=input("name with.png : ")
img.save(save)
'''


import qrcode
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(version =1,error_correction = qrcode.constants.ERROR_CORRECT_H,box_size = 20,border = 4)
link = input("link or text : ")
qr.add_data(link)
qr.make(fit=True)

img=qr.make_image(fill_color = "red", back_color="white")

save=input("name with.png : ")
img.save(save)

