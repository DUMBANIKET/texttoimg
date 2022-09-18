from PIL import Image,ImageDraw,ImageFont

# img=Image.open('OIP.jfif')
img=Image.new('RGB',(200,300),color=(255,255,255))
print(img.size)
d=ImageDraw.Draw(img)
# font = ImageFont.truetype(font='path/to/your/font.ttf', size=42)
txt='''laul biro this is just a test for some  stupid reason idk i am just testing till where it exceeds'''
fnt=ImageFont.truetype("arial.ttf",15)
d.text((30,30),txt,font=fnt,fill=(0, 0,0))
img.save('static/images/yo.png')
