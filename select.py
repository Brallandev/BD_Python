import psycopg2
from datos_conexion import dc

#1 Conexion a la base de datos
conexion=psycopg2.connect(**dc)

#2 creacion del cursor
cursor=conexion.cursor()

#3 ejecutala sentencia sql
cursor.execute('select * from empleado ')

#4 obtencion de todos los registros
registros=cursor.fetchall()

print(registros)

for registro in registros:
    id = registro[0]
    nombre = registro[1]
    email= registro[2]
    print("{}. {} -Email:{}".format(id,nombre,email))

#6 cerrar cursor y conexion
cursor.close()
conexion.close()
