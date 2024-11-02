import qrcode
import image
qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5,
)

data = "https://youtu.be/Nnop2walGmM?si=k70GR_ezM4hLeNqM",



qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="Blue",back_color = "yellow")
img.save("QR.png")