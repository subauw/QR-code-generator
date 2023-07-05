import pyqrcode
#pip install pyqrcode
import png
#pip install pypng
from pyqrcode import QRCode

# String which represent the qr code
source = "www.youtube.com"

# Generate QR Code
url = pyqrcode.create(source)

# Create and save the png file
url.png('myqr.png', scale = 6)