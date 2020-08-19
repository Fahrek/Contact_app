import os


CARPETA   = 'contactos/' # carpeta de contactos
EXTENSION = '.txt'     # Extensión de archivos


#Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre    = nombre
        self.telefono  = telefono
        self.categoria = categoria


def app():
    # Revisa si la carpeta existe o no
    crear_directorio()
    
    # Muestra el menu de opciones
    mostrar_menu()
    
    # Preguntar al usuario la acción a realizar
    preguntar = True
    while preguntar:
        opcion = int(input('Opción: '))
        
        # Ejecutar acciones
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
        elif opcion == 6:
            exit()
        else:
            print('Opción no válida, intente de nuevo...')

            
def agregar_contacto():
    
    print('Introduce los datos del nuevo contacto...')
    nombre_contacto = input('Nombre: ')
     
    # Revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto)
     
    if not existe:
         
        # Crear archivo 'contactos/Juan.txt'
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            
            # Resto de campos
            telefono_contacto  = input('Teléfono: ')
            categoria_contacto = input('Categoría: ')
            
            # Instanciar clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            
            # Escribir en el archivo
            archivo.write('Nombre: '    + contacto.nombre   + '\n')
            archivo.write('Teléfono: '  + contacto.telefono + '\n')
            archivo.write('Categoría: ' + contacto.categoria)
            
            # Mostrar mensaje de éxito
            print(" ------------------------------- ")
            print("| contacto creado correctamente |") 
            print(" ------------------------------- ")
            
    else:
        print('Este contacto ya existe')
        
    # Reiniciar la app
    app()
 

def editar_contacto():
    nombre_anterior = input('Introduce el nombre del contacto: ')
    
    # Revisar si el archivo ya existe antes de editarlo
    existe = existe_contacto(nombre_anterior)
    
    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
        
            # Resto de los campos
            nombre_contacto    = input('Nuevo nombre: ')
            telefono_contacto  = input('Nuevo teléfono: ')
            categoria_contacto = input('Nueva categoría: ')
            
            # Instanciar clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            
            # Escribir en el archivo
            archivo.write('Nombre: '    + contacto.nombre   + '\n')
            archivo.write('Teléfono: '  + contacto.telefono + '\n')
            archivo.write('Categoría: ' + contacto.categoria)
            
            # Cerramos archivo
            archivo.close()
            
            # Renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
            
            # Mostrar mensaje de éxito
            print(" -------------------------------- ")
            print("| contacto editado correctamente |") 
            print(" -------------------------------- ")
            
    else:
        print('Ese contacto no existe')        

    # Reiniciar la aplicación
    app()
   
   
def mostrar_contactos():
    archivos = os.listdir(CARPETA)
    
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    
    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                # Imprime los contenidos
                print(linea.rstrip())
            # Imprime un separador entre contactos
            print('\r\n')   
  
  
def buscar_contacto():
    nombre = input('Buscar: ')
    
    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\nInformación de contacto:')
            print('---------------------------\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
            
    except IOError:
        print('El archivo no existe')
        print(IOError)
        
    # Reiniciar la app
    app()


def eliminar_contacto():
    nombre = input('Eliminar: ')
   
    try:
        os.remove(CARPETA + nombre + EXTENSION)
        
        # Mostrar mensaje de éxito
        print(" -------------------------------- ")
        print("| contacto editado correctamente |") 
        print(" -------------------------------- ")
        
    except IOError:    
        print('No existe ese contacto')
        print(IOError)
        
    # Reiniciar la app
    app()
        
        
def mostrar_menu():
    print("""
          Seleccione una opción:\n
          1. Agregar nuevo contacto
          2. Editar conctacto
          3. Ver contacto
          4. Buscar contacto
          5. Eliminar contacto
          6. Salir
          """)
    
    
def crear_directorio():
    if not os.path.exists(CARPETA):
        # Crear la carpeta
        os.makedirs(CARPETA)
        
    # else:
    #     print('La carpeta ya existe')


def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)


app()