import psycopg2
from datos_conexion import dc

conexion=psycopg2.connect(**dc)

cursor = conexion.cursor()

sql = 'insert into empleado(nombre,email) values(%s,%s)'

nombre=input('Ingere el nombre \n')
email=input('Ingrese el correo electronico \n')

parametros=(nombre,email)

cursor.execute(sql,parametros)

conexion.commit()

cursor.close()
conexion.close()