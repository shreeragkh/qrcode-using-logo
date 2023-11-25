import qrcode
from PIL import Image
data = "https://www.instagram.com/shree.ragkh"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="white", back_color="black")
img.save("qr_code.png")
qr_code = Image.open("qr_code.png")
logo = Image.open("insta logo.png")
logo = logo.resize((60, 60))
pos = ((qr_code.width - logo.width) // 2, (qr_code.height - logo.height) // 2)
qr_code.paste(logo, pos)
qr_code.save("qr_code_with_logo1.png")