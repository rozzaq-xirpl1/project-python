import qrcode
import image
qr = qrcode.QRCode(
    version = 15, # versi qrcode
    box_size = 10, # untuk ukuran qrcode
    border = 5 # ukuran putih-putihnya qrcode
)

data = "https://youtu.be/oC0MQxG7N4w?si=6cBdoOS7NFTGYoG7"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black", back_color = "white") # setting warna qrcode
img.save("image.jpg")