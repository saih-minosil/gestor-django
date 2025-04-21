import os
import re
import datetime
import xml.sax
import datetime
from vsad_bd import insertar_valores,iniciar_conexion,finalizar_conexion,borrar_valores
from handlers import ObsHandler
import xml.sax
import shutil
import mysql.connector

class UnprocesedException(Exception):
    pass

#CONFIGURACION BASICA
#CARPETAS
DIRECTORIO_DATOS='/mnt/DatosVsad/Carga_modelos'
DIR_XML=DIRECTORIO_DATOS+'/xml'
DIR_BACK=DIRECTORIO_DATOS+'/bck'
DIR_LOG=DIRECTORIO_DATOS+'/log'
DIR_OLD=DIRECTORIO_DATOS+'/old'
TIEMPO_BORRADO=datetime.timedelta(days=4)
HOST_MYSQL="10.31.156.174"
USER_MYSQL="vsad_new"
PASSWORD_MYSQL="CeCuSaIh2025"
#USER_MYSQL="vsad_new" #ADMIN DESDE TODAS LAS IPS; USAR EL OTRO
#PASSWORD_MYSQL="CeCuSaIh2025"

FORMATO_FECHA_ARCHIVOS="%Y%m%d%H%M" #Para los nombres de archivo
FORMATO_FECHA_NORMAL="%d/%m/%Y %H:%M:%S" #Formato español de fecha

#Globales (no muy buena práctica pero util en este caso)
archivo_log=None #para no andarlo pasando en cada llamada a log

def inicializar_log(): #Avre el archivo para los logs
    global archivo_log
    
def finalizar_log():
    logear(f"Proceso finalizado en el instante {datetime.datetime.now().strftime(FORMATO_FECHA_NORMAL)}")
    archivo_log.close()

def logear(cadena):
    global archivo_log
    print(cadena,file=archivo_log)
    print(cadena)

def procesar_archivo(con,parser,carpeta,archivo):
    logear(f"Procesando archivo {archivo}")
    try:
        f = open(os.path.join(carpeta, archivo), 'r')
    except Exception as e:
        logear(f"No se ha podido abrir el archivo {archivo} : {e}")
        return
    try:
        parser.parse(f)
        values=parser.getContentHandler().getValues()
        for key,serie in values.items():
            id_serie = key
            fecha_pred = datetime.datetime.strptime(archivo[0:12], "%Y%m%d%H%M")
            insertar_valores(con, id_serie, serie, fecha_pred.timestamp())
    except mysql.connector.errors.IntegrityError as e:
        logear(f"Ya hay datos introducidos para la fecha {datetime.datetime.strptime(archivo[0:12],'%Y%m%d%H%M')} ")
    except mysql.connector.errors.Error as e:
        logear(f"Error al Escrbir en la base de datos {e} ")
        raise UnprocesedException('Unprocessed','Unprocessed')
    except Exception as e:
        logear(f"Error al procesar el archivo {archivo}: {e} ")
        raise UnprocesedException('Unprocessed','Unprocessed')
    finally:
        parser.getContentHandler().reset()
        f.close()

def mover_archivo(archivo,origen, destino):
    orig=os.path.join(origen,archivo)
    dest=os.path.join(destino,archivo)
    logear(f"Moviendo el archivo {orig} a {dest}")
    try:
        #dest=shutil.move(orig, dest)
        if os.path.isfile(dest):
            logear(f"{dest} ya existe, borrando")
            os.remove(dest)
        dest=shutil.move(orig, destino)
        #os.remove(orig)
        print(f"Archivo movido con exito a {dest}")
    except Exception as e:
        logear(f"Error al mover el archivo {orig} a {dest} \nError: {e}")

def limpiar_bd(con):
    filas_borradas=borrar_valores(con,TIEMPO_BORRADO)
    logear(f"{filas_borradas} filas borradas")



def main():
    global archivo_log
    with open(os.path.join(DIR_LOG,f"log{datetime.datetime.now().strftime(FORMATO_FECHA_ARCHIVOS)}.txt"),'w') as archivo:
        archivo_log=archivo           
        try:
            con = iniciar_conexion(HOST_MYSQL,USER_MYSQL,PASSWORD_MYSQL)
        except Exception as e:
            logear(f"No se ha podido conectar a la base de datos en  {HOST_MYSQL} con usuario {USER_MYSQL}: \n {e} \n Comprueba que la BB.DD esté activa y que el usuario tenga permisos para acceder desde la IP del host")
            return
        parser = xml.sax.make_parser()
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        Handler = ObsHandler()
        parser.setContentHandler(Handler)


        obs={};hist={};pron={};timestamps={};antiguos=[]
        #######################################   PROCESAR DIRECTORIO ##############################################################################
        with os.scandir(DIR_XML) as lista_ficheros:
            for fichero in lista_ficheros: #PARA CADA FICHERO DE XML
                valid = re.search(r"\d{12}SimulationResults_\w{3}\w?.xml",fichero.name)
                if valid :
                    fecha=re.search(r"\d{12}",fichero.name).group() #Extrae fecha y tipo del nombre
                    tipo=re.search("FOR|HIST|OBS",fichero.name).group()
                    fecha=datetime.datetime.strptime(fecha,"%Y%m%d%H%M")
                    ts=int(fecha.timestamp())
                    if datetime.datetime.now()-fecha < datetime.timedelta(days=3): #Menos de 3 dias de antiguedad
                        if tipo=='OBS':                     #Guarda los nombres en las correspondientes tablas
                            obs[ts]=fichero.name
                        elif tipo=='HIST':
                            hist[ts]=fichero.name
                        elif tipo=='FOR':
                            pron[ts]=fichero.name
                        timestamps[ts]=1               #Guarda los timestamps como keys en una tabla (Asi se guardan todos sin repeticiones)
                    else:
                        antiguos.append(fichero.name) #Añade a antiguos para borrado/movido
                else:
                    logear(f"{fichero.name} no es un nombre valido, será ignorado")
            timestamps=list(timestamps.keys()) #Crea una lista ordenada con los timestamps
            timestamps.sort()
            procesar = []
            if not timestamps:
                logear("No se han encontrado archivos")
            else:
                ultimo_t=timestamps[-1] #Comprueba si ha pronostico en el ultimo timestamp

                #######################################   PROCESAR TABLAS TIMESTAMP-NOMBRE_FICHERO ##############################################################################
                anterior_ts=timestamps[0]
                for t in timestamps: #para cada timestamp
                    if not t in obs:  #Comprueba si faltan archivos
                        logear(f"Falta el archivo de observaciones : {datetime.datetime.fromtimestamp(t).strftime('%Y%m%d%H%M')}SimulationResults_OBS.xml")
                    else:
                        procesar.append(obs[t])
                    if not t in hist:
                        logear(f"Falta el archivo de historicos : {datetime.datetime.fromtimestamp(t).strftime('%Y%m%d%H%M')}SimulationResults_HIST.xml")
                    else:
                        procesar.append(hist[t])
                    if t-anterior_ts > 10800:     #Comprueba si hay un hueco de mas de 3 horas con el anterior
                        logear(
                            f"Hay un hueco de mas de tres horas entre observaciones \n"
                            f"Entre las {datetime.datetime.fromtimestamp(anterior_ts).strftime('%d/%m/%Y %H:%M')} "
                            f"y las {datetime.datetime.fromtimestamp(t).strftime('%d/%m/%Y %H:%M')}")
                    anterior_ts=t
                if not ultimo_t in pron:
                    logear(
                        f"Falta el archivo de pronosticos : {datetime.datetime.fromtimestamp(ultimo_t).strftime('%Y%m%d%H%M')}SimulationResults_FOR.xml")
                else:
                    procesar.append(pron[ultimo_t])
            #######################################   PROCESAR ARCHIVOS ##############################################################################
            print(procesar)
            for archivo in procesar:
                try:
                    procesar_archivo(con,parser,DIR_XML,archivo)   #PROCESA
                    mover_archivo(archivo,DIR_XML,DIR_BACK)         #Y mueve a BACK
                except UnprocesedException as e:
                    pass    
            logear("Limpiando BB.DD")
            limpiar_bd(con) #Limpia antiguos de la BB.DD
            for archivo in pron.values():                                #Los antiguos los mueve a old
                if archivo!=pron[ultimo_t] :
                    mover_archivo(archivo,DIR_XML,DIR_OLD)
            for archivo in antiguos:
                mover_archivo(archivo,DIR_XML,DIR_OLD) #Ya llevna el .xml?
        finalizar_conexion(con)    
    
    

if __name__ == '__main__':
    main()
