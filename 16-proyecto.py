import os

CARPETA = 'contactos/'  # Carpeta de contactos
EXTENSION = '.txt'  # Extension de Archivos

# Contacto


class Contacto:
    def __init__(self, nombre, telefono, email, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.categoria = categoria


def app():
    # Revisa si la carpeta existe o no
    crear_directorio()

    # Menu de opciones
    mostrar_menu()

    # Preguntar al Usuario la accion a Realizar
    preguntar = True
    while preguntar:
        opcion = raw_input('Seleccionar una opcion:\r\n')
        opcion = int(opcion)

        # Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opcion no valida, intente nuevamente')


def eliminar_contacto():
    nombre = raw_input('Seleccione el contacto que desea eliminar: \r\n')
    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\n Contacto eliminado correctamente')
    except expression as identifier:
        print('No existe el contacto seleccionado')

    # Reiniciar la app
    app()
def buscar_contacto():
    nombre= raw_input('Seleccione el nombre que desea buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Informacion del contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError)

    # Reiniciar la app
    app()

def mostrar_contactos():
    archivos=os.listdir(CARPETA)
    archivos_txt=[i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                # Imprime el contenido
                print(linea.rstrip())
            # Separacion entre contactos
            print('\r\n')

def editar_contacto():
    print('Escribe el nombre del contacto a editar')
    nombre_anterior= raw_input('Nombre del contacto que desea editar:\r\n')

    # Revisar si el archivo ya existe antes de editarlo
    existe=existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

            # Edicion de campos
            nombre_contacto= raw_input('Agrega el nuevo Nombre del contacto:\r\n')
            telefono_contacto= raw_input('Agrega el nuevo Telefono del contacto:\r\n')
            email_contacto= raw_input('Agrega el nuevo Email del contacto:\r\n')
            categoria_contacto= raw_input('Agrega la nueva Categoria del contacto:\r\n')

            # Instanciar
            contacto=Contacto(nombre_contacto, telefono_contacto,
                              email_contacto, categoria_contacto)

            # Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Email: ' + contacto.email + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            archivo.close()

            # Reenombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION,
                      CARPETA + nombre_contacto + EXTENSION)

            # Mostrar Mensaje de Exito
            print('El contacto ha sido editado con exito')
    else:
        print('No es posible encontrar el contacto seleccionado')

    # Reiniciar la aplicacion
    app()

def agregar_contacto():
    print('Escribe los datos para agregar el nuevo Contacto')
    nombre_contacto= raw_input('Nombre del contacto:\r\n')

    # Revisar si el archivo ya existe antes de crearlo
    existe=existe_contacto(nombre_contacto)
    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

            # otros campos
            telefono_contacto= raw_input('Agregar Telefono: \r\n')
            email_contacto= raw_input('Agregar email:\r\n')
            categoria_contacto= raw_input('Agregar categoria:\r\n')

            # Instanciar la clase
            contacto=Contacto(nombre_contacto, telefono_contacto,
                              email_contacto, categoria_contacto)

            # Escribir el Archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Email: ' + contacto.email + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            # Mensaje de Exito
            print('\r\n Contacto creado exitosamente. \r\n')

    else:
        print('Ese contacto ya existe')

    # Reiniciar la app
    app()

def mostrar_menu():
    print('Seleccione del menu lo que desea hacer: ')
    print(' 1- Agregar Nuevo Contacto')
    print(' 2- Editar contacto')
    print(' 3- Ver Contacto')
    print(' 4- Buscar Contacto')
    print(' 5- Eliminar Contacto')

def crear_directorio():
    if not os.path.exists(CARPETA):
      # Crear la carpeta
     os.makedirs(CARPETA)

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)
app()