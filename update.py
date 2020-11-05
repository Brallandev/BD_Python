import psycopg2
from datos_conexion import dc

conexion=psycopg2.connect(**dc)

cursor=conexion.cursor()

sql="update empleado set nombre='valeria tavera' where nombre='valeria' "

cursor.execute(sql)

conexion.commit()

cursor.close()
conexion.close()