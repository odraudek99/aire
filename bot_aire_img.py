from selenium import webdriver
from PIL import Image
import StringIO
import signal

### inicio json
import json
import urllib
import re


url = "http://www.aire.df.gob.mx/js/delegaciones/paths.js"

f = urllib.urlopen(url)
myfile = f.read()


ll = re.split('\n',myfile)

#print myfile

#print("tamanio: "+ str(len (ll)) )

file = open('datos.json', 'w+')


json = "["
file.write(json)

tamanio = len(ll)
count = 0

for chunk in ll:
    #print "chunk1: "+str(chunk)
    if "name:" in chunk and "zona25" in chunk :
        print("No aplica")
    elif "name:" in chunk :
        #print ("name+1")
        cadena = chunk.replace("\"+\"\\n\"+\"", "_").replace("\"+\"", "_").replace("\"", "").replace(",", "").replace("\t", "").replace("name: ", "").replace("name: ", "").replace("\n", "").replace("\r", "");

        objeto = re.split("_",cadena);

        if count > 0 and count + 1 < tamanio:
                json = json + ", "
                #primerLinea = False
        count =+1
        linea = str("{ \"Localidad\": \""+str(objeto[0]) +
                            "\", \"Estatus\": \""+str(objeto[1]) +
                            "\", \"Numero\": \""+str(objeto[2]) +
                            "\", \"Contaminante\": \""+str(objeto[3])+"\"}")

        json = json + linea
        file.write(linea)


        #print(json)
        '''print ("{Localidad: "+str(objeto[0]) +
                ", Estatus: "+str(objeto[1]) +
                ", Numero: "+str(objeto[2]) +
                ", Contaminante: "+str(objeto[3])+"}")'''




objetoVacio = str("{ \"Localidad\": \"\"" +
                    ", \"Estatus\": \"\""+
                    ", \"Numero\": \"\""+
                    ", \"Contaminante\": \"\"}")

file.write(objetoVacio)
#json = json + objetoVacio

file.write("]")
json = json + "]"
json = json.replace("\n", "")

file.close()


file2 = open('datos2.json', 'w')
file2.write(json)

file2.close()

print ("***termina json")
#print ("Mi JSON: "+json)




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









