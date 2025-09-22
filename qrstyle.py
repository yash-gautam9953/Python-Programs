import qrcode 
from PIL import Image
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=20,border=5)

qr.add_data("Hii im yash gautam and my mother name jsgATHDFWQJASFTDFSDSCX DBHAGSF")
qr.make(fit=True)
img=qr.make_image(fill_color="white",back_color="purple")
img.save("yash.png")