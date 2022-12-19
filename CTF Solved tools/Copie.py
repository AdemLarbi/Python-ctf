from PIL import Image

img=Image.open("./ch9.png","r")
buff=""
flag=""
l,h=img.size
pix=img.load()

for x in range(0,h,2):
    r,g,b=pix[x,0]
    buff+=str(r&1)+str(g&1)+str(b&1)

for i in range(len(buff)/17):
    flag+=chr(int(buff[i*8:i*8+8],2))
   
    print flag






