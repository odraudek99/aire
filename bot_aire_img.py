from selenium import webdriver
from PIL import Image
import StringIO

driver = webdriver.PhantomJS()
#driver = webdriver.Firefox()


driver.set_window_size(1366, 728) # optional
driver.get('http://www.aire.df.gob.mx/default.php?map=Yw==')
driver.save_screenshot('original.png')
 
screen = driver.get_screenshot_as_png()

driver.quit()
box = (627, 285, 1172, 594)
height=401
width=709
new_width  = 709
new_height = new_width * height / width 
new_height = 402
new_width  = new_height * width / height
im = Image.open(StringIO.StringIO(screen))
region = im.crop(box)
region = region.resize((new_width,new_height), Image.ANTIALIAS)
region.save('/home/odraudek99/aire/calidad.png', 'PNG', optimize=True, quality=95)


box2 = (189,204, 599,615)

im2 = Image.open(StringIO.StringIO(screen))
region2= im2.crop(box2)
region2.save('/home/odraudek99/aire/mapa.png', 'PNG', optimize=True, quality=95)

print ('termina python 1')


driver = webdriver.PhantomJS()
#driver = webdriver.Firefox()
driver.set_window_size(1366, 728) # optional
driver.get('https://www.google.com.mx/search?q=hora&ie=utf-8&oe=utf-8&gws_rd=cr&ei=3TVDV46rMZXmyAK8woeoAw')
driver.save_screenshot('hora.png')
screen = driver.get_screenshot_as_png()
driver.quit()
box = (144,248,427, 345)
im2 = Image.open(StringIO.StringIO(screen))
region2= im2.crop(box)
region2.save('/home/odraudek99/aire/hora1.png', 'PNG', optimize=True, quality=95)
print ('termina python')
