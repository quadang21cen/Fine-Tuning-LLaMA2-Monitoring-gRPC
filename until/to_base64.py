import base64
from PIL import Image
import io


def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        base64_data = base64.b64encode(image_data)
        base64_str = base64_data.decode("utf-8")
        return base64_str


def base64_to_image(base64_string, output_path):
    image_data = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(image_data))
    image.save(output_path)

image_path = 'C:\\Users\\quach\\Desktop\\Recent\\13767.jpg'
base64_string = image_to_base64(image_path)
