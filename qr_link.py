import qrcode

url = "insert your link here"

img = qrcode.make(url)
img.save("qrcode.png")