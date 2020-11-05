import psycopg2
from datos_conexion import dc

conexion=psycopg2.connect(**dc)

cursor = conexion.cursor()

sql = 'insert into empleado(nombre,email) values(%s,%s)'

parametros=('valeria', 'valeriatavera@usantotoma.edu.co')

cursor.execute(sql,parametros)

conexion.commit()

cursor.close()
conexion.close()