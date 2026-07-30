import qrcode

url = input("Enter form URL: ").strip() or "https://YOUR-SITE.com/form.html"
qr = qrcode.make(url)
qr.save("qr-code.png")
print(f"QR code saved to qr-code.png for: {url}")
