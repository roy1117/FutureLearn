from PIL import Image

#Open image using Image module
im = Image.open("sample_black_white.bmp")
#Show actual Image
im.show()
#Show rotated Image
im = im.rotate(45)
im.show()