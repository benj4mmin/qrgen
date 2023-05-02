# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import qrcode

ssid = ""
password = ""

# QR code content for Wi-Fi network
wifi_data = f"WIFI:T:WPA;S:{ssid};P:{password};;"

# Generate QR code image
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(wifi_data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Save QR code image as PNG file
img.save("wifi_qrcode.png")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
