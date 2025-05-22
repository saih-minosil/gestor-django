import datetime
from vsad_bd import iniciar_conexion,finalizar_conexion
from vsad_datos import inicializar_log,logear,finalizar_log,procesar_archivo,mover_archivo
from handlers import ObsHandler
import xml.sax
import shutil

#CONFIGURACION BASICA
#CARPETAS
DIRECTORIO_DATOS='.'
DIR_XML=DIRECTORIO_DATOS+'/xml'
DIR_BACK=DIRECTORIO_DATOS+'/bck'
DIR_LOG=DIRECTORIO_DATOS+'/log'
DIR_FAIL=DIRECTORIO_DATOS+'/fail'
TIEMPO_BORRADO=datetime.timedelta(days=5)
HOST_MYSQL="10.31.156.174"
USER_MYSQL="jorge"
PASSWORD_MYSQL="0KDU1nod__"

FORMATO_FECHA_ARCHIVOS="%Y%m%d%H%M" #Para los nombres de archivo
FORMATO_FECHA_NORMAL="%d/%m/%Y %H:%M:%S" #Formato español de fecha

#Globales (no muy buena práctica pero util en este caso)
archivo_log=None #para no andarlo pasando en cada llamada a log

#------------------------------------------------------INICIO------------------------------------------------------
con = iniciar_conexion(HOST_MYSQL,USER_MYSQL,PASSWORD_MYSQL)
parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
Handler = ObsHandler()
parser.setContentHandler(Handler)
inicializar_log()

#-------------------------------------------------------- TESTS ------------------------------------------------------
#def logear(cadena):
print("probando loguear")
logear("Esto es una prueba")

#def procesar_archivo(con,parser,carpeta,archivo):
print("probando procesar_archivo")
procesar_archivo(con,parser,DIR_XML,"202503190119SimulationResults_OBS.xml")


#def mover_archivo(archivo,origen, destino):
# print("probando mover archivo correcto")
# mover_archivo("mover.hola",DIR_XML,DIR_BACK) #Existe
# print("probando mover archivo (ya esta en destino)")
# mover_archivo("mover.repetido",DIR_XML,DIR_BACK) #Ya esta en destino
# print("probando mover archivo (no existe)")
# mover_archivo("mover.adios",DIR_XML,DIR_BACK) #Ya esta en destino

#def limpiar_bd(con):
#limpiar_bd(con) DIFICIL PROBAR ESTO; NECESITO OTRA BB.DD


#---------------------------------------------------------FINALIZACION ------------------------------------------------
finalizar_log()
finalizar_conexion(con)