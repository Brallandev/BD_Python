import psycopg2

from datos_conexion import dc

conexion=psycopg2.connect(**dc)

cursor = conexion.cursor()

sql = 'select * from empleado where nombre=%s'

parametros=("")

cursor.execute(sql,parametros)

registros=cursor.fetchall()

print(registros)

cursor.close()
conexion.close()