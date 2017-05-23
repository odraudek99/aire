from selenium import webdriver
from PIL import Image
import StringIO
import signal

### inicio json
import json
import urllib
import re
import numpy

class Medicion(object):
    localidad = ""
    estatus = ""
    numero = ""
    contaminante = ""
    fill =""


    def __init__(self, localidad="", estatus="", numero="", contaminante=""):
        self.localidad = localidad
        self.estatus = estatus
        self.numero = numero
        self.contaminante = contaminante

    def setFill(self, fill):
        self.fill=fill

    def toString(self):

        return ("{\"localidad\": "  +   "\""+self.localidad.strip() +"\"" +
                ", \"estatus\": "   +   "\"" + self.estatus.strip() +"\"" +
                ", \"numero\": "    + "\"" + self.numero.strip()+ "\""+
                ", \"contaminante\":"   +   "\"" + self.contaminante.strip()+ "\"" +
                ", \"fill\": "+"\""+self.fill.strip() +"\"}")

url = "http://www.aire.df.gob.mx/js/delegaciones/paths.js"

f = urllib.urlopen(url)
myfile = f.read()

ll = re.split('\n',myfile)

print("tamanio: "+ str(len (ll)) )
file = open('datos2.json', 'w')

json = "["
file.write(json)

tamanio = len(ll)
count = 0


mediciones = []

for chunk in ll:
    if "name:" in chunk and "zona25" in chunk :
        print("No aplica")
        continue
    linea = ""



    if "name:" in chunk :
        medicion = Medicion()
        #print ("name+1")
        cadena = chunk.replace("\"+\"\\n\"+\"", "_").replace("\"+\"", "_").replace("\"", "").replace(",", "").replace("\t", "").replace("name: ", "").replace("name: ", "").replace("\n", "").replace("\r", "");

        objeto = re.split("_",cadena);

        medicion = Medicion(objeto[0],objeto[1],objeto[2],objeto[3])

        mediciones.append(medicion)

    elif "fill:" in chunk :
        cadena = chunk.replace("\"+\"\\n\"+\"", "|").replace("\"+\"", "|").replace("\"", "").replace(",", "").replace("\t", "").replace("fill:","").replace("\r", "");
        medicion.setFill(str(cadena))

print ("len mediciones: "+str(len(mediciones)))

for med in mediciones :
    print (med.toString())
    file.write(str(med.toString())+", ")

medicion = Medicion()
file.write(str(medicion.toString()))

file.write("]")

file.close()




## end json

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

driver.service.process.send_signal(signal.SIGTERM)
driver.quit()
print ('termina ejecucion python...')









