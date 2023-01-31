import qrcode

def generate_qr_code(data, file_path):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code data
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(file_path)

# Example usage
generate_qr_code("Hello, World!", "qr_code.png")
