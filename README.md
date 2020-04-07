# Saving a rotated/transposed image in Pillow 7.1.0

It seems the orientation code is not updated when rotating/transposing an image in 
Pillow and then saving it.

## Test platform
Ubuntu 18.04 LTS
Python 3.8.0
Pillow 7.1.0

## Code
Here's the code:
```python
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
```

## Expected Behaviour

When calling the `convert` for the second time the orientation code is expected to be `1` for 
normal orientation.

## Observed Behaviour

File `B.PNG` has EXIF rotation code 8 (rotated 90 degrees).
Interestingly, `B.PNG` is displayed correctly by `Image Viewer` in Ubuntu.
`C.PNG` is displayed rotated 90 degrees.

