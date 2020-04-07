from PIL import Image, __version__

EXIF_ORIENTATION = 0x0112
ROTATION = {3: Image.ROTATE_180, 6: Image.ROTATE_270, 8: Image.ROTATE_90}


def convert(input_filename, output_filename, image_format="PNG"):
    img = Image.open(input_filename)
    exif = img._getexif()
    if exif is not None:
        if EXIF_ORIENTATION in exif.keys():
            code = exif[EXIF_ORIENTATION]
            angle = ROTATION.get(code, None)
            print(f"filename: {input_filename};  EXIF rotation code: {code}")
            if angle is not None:
                img = img.transpose(angle)
    img.save(output_filename, format=image_format)


if __name__ == "__main__":
    print(f"PIL version: {__version__}")

    convert("A.JPG", "B.PNG")
    convert("B.PNG", "C.PNG")
