import pyqrcode
import matplotlib

str = input('>>>')

qrcode = pyqrcode.create(str)
qrcode.png('my_qrcode.png', scale=6)

qrcode.show()