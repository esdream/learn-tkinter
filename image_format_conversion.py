from PIL import Image

image = Image.open('canvas_test.jpg')
image.save('canvas_test.gif', 'gif')
