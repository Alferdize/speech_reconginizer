'''import base64
with open("C:\\Users\Anubhav\Desktop\\untitled2\image.png", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
print(str)'''
'''
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
path = 'C:\\Users\Anubhav\Desktop\\untitled2\image.png'
img = Image.open(path)
img = img.convert('RGBA')
pix = img.load()
for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pix[x, y][0] < 102 or pix[x, y][1] < 102 or pix[x, y][2] < 102:
            pix[x, y] = (0, 0, 0, 255)
        else:
            pix[x, y] = (255, 255, 255, 255)
img.save('temp.png')
i = "C:\\Users\\Anubhav\\Desktop\\untitled2\\project\\temp2.jpg"
text = pytesseract.image_to_string(Image.open('temp.png'))
# os.remove(‘temp.jpg’)
print(text)#print image_to_string(Image.open(‘find.jpg’))
'''
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
i = 'C:\\Users\Anubhav\Desktop\\untitled2\project\\testing\\temp.png'
im = Image.open(i) # the second one
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('temp2.jpg')
i = 'C:\\Users\Anubhav\Desktop\\untitled2\project\\temp2.jpg'
text = pytesseract.image_to_string(Image.open(i))
print(text)
