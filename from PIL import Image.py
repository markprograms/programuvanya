from PIL import Image
from PIL import ImageFilter

with Image.open("photo.jpg") as original:
    print(original.size)
    print(original.format)
    print(original.mode)
    pic_gray=original.convert("L")
    pic_blured=original.filter(ImageFilter.BLUR)
    pic_up = original.transpose(Image.ROTATE_90)
    pic_gray.save("gray.jpg")
    #original.show()
    #pic_blured.show()
    pic_gray.show()
    #pic_up.show()