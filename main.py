import psycopg2

from ContactoPersonal import Contactopersonal
from ContactoTrabajo import ContactoTrabajo

conexion = psycopg2.connect(
    user = 'postgres',
    host = "127.0.0.1",
    port = "5432",
    database = "AgendaPython",
    password = "admin"
)
cursor = conexion.cursor()

conexion.commit()

def menu_opciones():
        print("""
        ==============================
                MENÚ PRINCIPAL
        ==============================
        1. Crear Contacto 
        2. Mostrar Contactos
        3. Eliminar Contacto
        4. Agregar a Favorito
        5. Salir
        ==============================
        """)
def menu_opciones2():
        print("""
        ==============================
             MENÚ AGREGARCONTACTO
        ==============================
        1. Crear Contacto Personal
        2. Crear Contacto Trabajo
        3. Salir
        ==============================
        """)
def Agregar_ContactoPersonal(contacto):
    try:
        cursor.execute("""
            INSERT INTO "contactoPersonal"("nombreCompleto", email, numero, pais,genero)
            VALUES (%s,%s,%s,%s,%s)
            RETURNING id 
        """,(contacto.nombreCompleto, contacto.email, contacto.numero,
              contacto.pais, contacto.genero))

        conexion.commit()
        print("ContactoPersonal agregado exitosamente!!!")

    except Exception as e:
        conexion.rollback()
        print(f"Error al agregar el contacto {e}")
    finally:
        cursor.close()
        conexion.close()
def agregar_ContactoTrabajo(contacto):
    try:
        cursor.execute("""
        INSERT INTO "contactoTrabajo"("nombreCompleto", email, numero,empresa,instagram)
        VALUES (%s,%s,%s,%s,%s)
        RETURNING id
        """,(contacto.nombreCompleto , contacto.email, contacto.numero,
            contacto.empresa, contacto.instagram))
        conexion.commit()
        print(f"ContactoTrabajo agregado exitosamente!!! ")
    except Exception as e:
        conexion.rollback()
        print(F"Error al agregar el contacto {e}")
    finally:
        cursor.close()
        conexion.close()

def mostrar_contactos():
    try:
        cursor.execute('SELECT * FROM "contactoPersonal" ORDER BY "id" ASC')
        contactos = cursor.fetchall()
        for row in contactos:
            contacto_personal = Contactopersonal(row[0],row[1],row[2],row[3],row[4],row[5])
            contacto_personal.mostrar_info()
    except Exception as e:
        print(f"Error al mostrar contactos {e}")
    finally:
        cursor.close()
        conexion.close()

def MenuMain():
    banderas = True
    menu_opciones()
    while banderas:
        numero_opc = input("Digite un número: ")
        if numero_opc == "4":
            print("Salida con éxito !!")
            banderas = False
        elif numero_opc == "1":
            menu_opciones2()
            numero_opc2 = input("Digite un numero: --> ")
            if numero_opc2 == "1":
                nombreCompleto = input("Ingrese el nombre completo: ").upper()
                email = input("Ingrese el email: ").upper()
                numero = input("Ingrese el número: ").upper()
                pais = input("Ingrese el país: ").upper()
                genero = input("Ingrese el género F/M: ").upper()
                contacto = Contactopersonal(nombreCompleto, email, numero, pais, genero)
                Agregar_ContactoPersonal(contacto)#llama a la funcion 
                menu_opciones()
            elif numero_opc2 == "2":
                nombreCompleto = input("Ingrese el nombre completo: ").upper()
                email = input("Ingrese el email: ").upper()
                numero = input("Ingrese el número: ").upper()
                empresa = input("Ingrese La empresa: ").upper()
                instagram = input("Ingrese el instagram: ").upper()
                contacto = ContactoTrabajo(nombreCompleto, email, numero, empresa, instagram)
                agregar_ContactoTrabajo(contacto)#llama a la funcion 
                menu_opciones()
            elif numero_opc2 == "3":
                print("Salida con éxito !!")
                banderas =  False
            else:
                print("Opción incorrecta, elige otra")
        elif numero_opc == "2":
            mostrar_contactos()
            print("====================")
            menu_opciones()

MenuMain()