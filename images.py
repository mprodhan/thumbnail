from PIL import Image

image = Image.open('./images/c3p0.jpg')
'''
image when used to create a thumbnail and to use the thumbnail method,
be sure to use the original variable. In this case thumbnail is modifying 
the image of c3p0 via the image variable only.
'''
image.thumbnail((400, 400))
image.save("thumbnail.jpg")
print(image.size)