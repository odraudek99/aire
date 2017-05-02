from selenium import webdriver
from PIL import Image
import StringIO

driver = webdriver.PhantomJS()
#driver = webdriver.Firefox()


#driver.set_window_size(1366, 728) # optional

driver.get('http://www.aire.df.gob.mx/default.php?map=Yw==')
driver.save_screenshot('original.png')
screen = driver.get_screenshot_as_png()


box_mapa = (4,160, 417,564)
im2 = Image.open(StringIO.StringIO(screen))
mapa= im2.crop(box_mapa)
mapa.save('/home/odraudek99/aire/mapa.png', 'PNG', optimize=True, quality=95)
print ('termina imagen mapa')


box_calidad = (439,163, 986,546)
im = Image.open(StringIO.StringIO(screen))
calidad= im.crop(box_calidad)
calidad.save('/home/odraudek99/aire/calidad.png', 'PNG', optimize=True, quality=95)
print ('termina imagen calidad')


driver.get('http://24timezones.com/es_husohorario/mexico_city_hora_actual.php')
driver.save_screenshot('hora_cdmx.png')
screen = driver.get_screenshot_as_png()

box = (34,186,248,286)
im2 = Image.open(StringIO.StringIO(screen))
region2= im2.crop(box)
region2.save('/home/odraudek99/aire/hora1.png', 'PNG', optimize=True, quality=95)
print ('termina imagen HORA CDMX')

driver.quit()
print ('termina ejecucion python...')









