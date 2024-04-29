def create_email(nombre, apellido):
    '''Esta funcion crea una correo electrónico a partir de la funcion process_class que crea una lista de cada alumno.
        PARAMETROS
            Entrada:
             como parametro de entrada son los nombres y el primer apellido de los alumnos de la lista creada con la funcion process_class
            Salida:
             como parametro de salida devuelve el correo electrónico que se crea con la inicial y las 5 primeras letras del apellido más el dominio del correo'''
    correo = nombre[0] + apellido[:5] + '@educacion.navarra.es'
    return correo

create_email('Alejandro', 'Martinez')