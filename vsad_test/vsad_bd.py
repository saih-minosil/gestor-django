import mysql.connector
import datetime
import mysql.connector

FORMATO_FECHA_MYSQL="%Y-%m-%d %H:%M:%S"

def iniciar_conexion(host,user,password):
    conexion = mysql.connector.connect(
      host=host,
      user=user,
      password=password
    )
    return conexion

def finalizar_conexion(con):
    con.close()

def insertar_valores(con,serie,values,fecha_pred_ts): #serie es el nombre exacto de la serie (P.E A001.Qobs A001.Iobs, A001_Discharge) values es un diccionaro timestamp-valor
    fecha_pred = datetime.datetime.fromtimestamp(fecha_pred_ts).strftime(FORMATO_FECHA_MYSQL)
    mycursor = con.cursor()
    sql_str = "INSERT INTO FEWS_FORECAST.FewsSeries (SeriesID,Fecha,Valor,Marcador,FechaForecast) VALUES (%s,%s,%s,%s,%s);"
    valores=[]
    for ts,value in values.items() :
        datestr=datetime.datetime.fromtimestamp(int(ts)).strftime(FORMATO_FECHA_MYSQL)
        valores.append((serie,datestr,value,0,fecha_pred))
    mycursor.executemany(sql_str,valores)
        #print(mycursor.rowcount, "record inserted.")
    con.commit()

def borrar_valores(con, delta): #Borra todos los valores con mas antiguedad que delta
    mycursor = con.cursor()
    sql_str = "DELETE FROM FEWS_FORECAST.FewsSeries WHERE Fecha < %s;"
    fecha_borrado=(datetime.datetime.now()-delta).strftime(FORMATO_FECHA_MYSQL)
    mycursor.execute(sql_str,(fecha_borrado,))
    return mycursor.rowcount


