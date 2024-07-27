import psycopg2

from ContactoPersonal import Contactopersonal
from ContactoTrabajo import Contactotrabajo


def obtner_conexion():
    try:
        conexion = psycopg2.connect(
            user = 'postgres',
            host = "127.0.0.1",
            port = "5432",
            database = "AgendaPython",
            password = "admin"
        )
        cursor = conexion.cursor()
        return conexion, cursor
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None, None

def cerrar_session(conexion, cursor):
    if cursor:
        cursor.close()
    if conexion:
        conexion.close()

def menu_opciones():
        print("""
        ==============================
                MENÚ PRINCIPAL
        ==============================
        1. Crear Contacto 
        2. Mostrar Contactos
        3. Editar Contactos
        4. Eliminar Contacto
        5. Agregar a Favorito
        6. Salir
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
def menu_opciones3():
        print("""
        ==============================
             MENÚ  MOSTRARCONTACTO
        ==============================
        1. Contacto Personal
        2. Contacto Trabajo
        3. Salir
        ==============================
        """)


def Agregar_ContactoPersonal(contacto):
    conexion, cursor = obtner_conexion()
    if conexion and cursor:
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
            cerrar_session(conexion,cursor)

def agregar_ContactoTrabajo(contacto):
    conexion , cursor = obtner_conexion()
    if conexion and cursor:
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
            cerrar_session(conexion,cursor)


def mostrar_contactosPersonal():
    conexion, cursor = obtner_conexion()
    if conexion and cursor:
        try:
            cursor.execute('SELECT * FROM "contactoPersonal" ORDER BY "id" ASC')
            contactos = cursor.fetchall()
            for row in contactos:
                contacto_personal = Contactopersonal(row[0], row[1], row[2], row[3], row[4], row[5])
                contacto_personal.mostrar_info()
        except Exception as e:
            print(f"Error al mostrar contactos {e}")
        finally:
            cerrar_session(conexion,cursor)

def mostrar_contactosTrabajo():
    conexion, cursor = obtner_conexion()
    if conexion and cursor:
        try:
            cursor.execute('SELECT * FROM "contactoTrabajo" ORDER BY "id" ASC')
            contactos = cursor.fetchall()
            for row in contactos:
                contacto_trabajo = Contactotrabajo(row[0], row[1], row[2], row[3], row[4], row[5])
                contacto_trabajo.mostrar_info()
        except Exception as e:
            print(f"Error al mostrar contactos {e}")
        finally:
            cerrar_session(conexion,cursor)

def actualizar_contactosPersonal():
    conexion , cursor = obtner_conexion()
    if conexion and cursor:
        try:
            contacto_id = (input("Ingrese el ID del contacto a modificar: "))
        except ValueError:
                print("ID INCORRECTO. Por favor,Intentelo nuevamente.")

        cursor.execute('SELECT * FROM "contactoPersonal" WHERE id = %s', (contacto_id,))
        if cursor.fetchone() is None:
            print(f"El ID {contacto_id} no existe en la base de datos.")
            return
        else:
            try:
                nombreCompleto = input("Digite nuevo Nombre:-> ")
                email = input("Digite nuevo Email:-> ")
                numero =  input("Digite nuevo Numero:-> ")
                pais = input("Digite nuevo Pais:-> ")
                genero = input("Digite nuevo Genero:-> ")

                query = '''
                UPDATE "contactoPersonal"
                SET "nombreCompleto" = %s, email = %s, numero = %s, pais = %s, genero = %s
                WHERE id = %s
            '''
                parametros = (nombreCompleto,email,numero,pais,genero,contacto_id)
                cursor.execute(query, parametros)
                print("Actualizacion de contacto exitosa!!")
                conexion.commit()
            except Exception as e:
                print(f"Error al actulizar contacto!! {e} ")
            finally:
                cerrar_session(conexion,cursor)
def actualizar_contactosTrabajo():
    conexion , cursor = obtner_conexion()
    if conexion and cursor:
        try:
            contactoId = input("Digite el ID del contacto a modificar: -> ")
        except ValueError:
            print(f"Error id incorrecto, vuelva a intentar!!")

        cursor.execute('SELECT * FROM "contactoTrabajo" WHERE id = %s', (contactoId))
        if cursor.fetchone() is None:
            print(f"Error el id: {contactoId} no existe en la base de datos:")
            return
        else:
            try:
                nombreCompleto = input("Digite nuevo Nombre:-> ")
                email = input("Digite nuevo Email:-> ")
                numero =  input("Digite nuevo Numero:-> ")
                empresa = input("Digite nuevo Empresa:-> ")
                instagram = input("Digite nuevo Instagram:-> ")

                query = '''
                    UPDATE "contactoTrabajo" SET "nombreCompleto" = %s, email=%s, numero=%s,empresa=%s,instagram=%s    
                '''
                parametros=(nombreCompleto, email,numero,empresa,instagram)

                cursor.execute(query,parametros)
                print("Actualizacion contactoTrabajo exitosa!!!")
                conexion.commit()
            except Exception as e: 
                print(f"Error al actulizar contacto!! {e} ")
            finally:
                cerrar_session(conexion, cursor)

            
            
def MenuMain():
    banderas = True
    menu_opciones()
    while banderas:
        numero_opc = input("Digite un número: --> ")
        if numero_opc == "6":
            print("Salida con éxito !!")
            banderas = False
        elif numero_opc == "1":
           while True:
                menu_opciones2()
                numero_opc2 = input("Digite un numero para crear : --> ")
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
                    contacto = Contactotrabajo(nombreCompleto, email, numero, empresa, instagram)
                    agregar_ContactoTrabajo(contacto)#llama a la funcion 
                    menu_opciones()
                elif numero_opc2 == "3":
                    print("volviendo al MenuMain!!")
                    break
                else:
                    print("Opción incorrecta, elige otra")
        elif numero_opc == "2":
            while True: 
                menu_opciones3()
                numero_opc3 = input("Digite un numero: --> ")
                if numero_opc3 == "1":
                    mostrar_contactosPersonal()
                elif numero_opc3 == "2":
                    mostrar_contactosTrabajo()
                elif numero_opc3 == "3":
                    print("volviendo al MenuMain!!")
                    menu_opciones()
                    break
                else:
                    print("Opcion Incorrecta, vuelve a intentar ")
        elif numero_opc == "3":
            while True:
                menu_opciones3()
                numero_opc4 = input("Digite un numero: --> ")
                if numero_opc4 == "1":
                    actualizar_contactosPersonal()
                elif numero_opc4 == "2":
                    actualizar_contactosTrabajo()
                elif numero_opc4 == "3":
                    print("volviendo al MenuMain!!")
                    menu_opciones()
                    break
                else:
                    print("Opcion Incorrecta , vuelve a intentar ")
        else:
             print("Error vuelva a digitar un numero ")

            

MenuMain()