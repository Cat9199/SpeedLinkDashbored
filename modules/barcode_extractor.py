from PIL import Image
from pyzbar.pyzbar import decode

def extract_barcode_data(image):
    img = Image.open(image)
    decoded_objects = decode(img)
    if decoded_objects:
        return decoded_objects[0].data.decode('utf-8')
    return "No barcode found."
