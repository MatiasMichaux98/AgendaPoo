import psycopg2

from ContactoPersonal import Contactopersonal
from ContactoTrabajo import Contactotrabajo


def obtener_conexion():
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
        6. Ver Contactos Favoritos
        7. Salir
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
             MENÚ CONTACTOS
        ==============================
        1. Contacto Personal
        2. Contacto Trabajo
        3. Salir
        ==============================
        """)


def Agregar_ContactoPersonal(contacto):
    conexion, cursor = obtener_conexion()
    if conexion and cursor:
        try:
            cursor.execute('''
                INSERT INTO "contactopersonal"(nombrecompleto, email, numero, pais, genero, favorito)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id 
            ''', (contacto.nombrecompleto, contacto.email, contacto.numero,
                contacto.pais, contacto.genero, contacto.favorito))

            conexion.commit()
            print("ContactoPersonal agregado exitosamente!!!")

        except Exception as e:
            conexion.rollback()
            print(f"Error al agregar el contacto {e}")
        finally:
            cerrar_session(conexion, cursor)


def agregar_ContactoTrabajo(contacto):
    conexion , cursor = obtener_conexion()
    if conexion and cursor:
        try:
            cursor.execute("""
            INSERT INTO "contactotrabajo"(nombreCompleto, email, numero,empresa,instagram,favorito)
            VALUES (%s,%s,%s,%s,%s)
            RETURNING id
            """,(contacto.nombrecompleto , contacto.email, contacto.numero,
                contacto.empresa, contacto.instagram,contacto.favorito))
            conexion.commit()
            print(f"ContactoTrabajo agregado exitosamente!!! ")
            
        except Exception as e:
            conexion.rollback()
            print(F"Error al agregar el contacto {e}")
        finally:
            cerrar_session(conexion,cursor)


def mostrar_contactosPersonal():
    conexion, cursor = obtener_conexion()
    if conexion and cursor:
        try:
            cursor.execute('SELECT * FROM "contactopersonal" ORDER BY "id" ASC')
            contactos = cursor.fetchall()
            for row in contactos:
                contacto_personal = Contactopersonal(row[0], row[1], row[2], row[3], row[4], row[5],row[6])  
                contacto_personal.mostrar_info()
        except Exception as e:
            print(f"Error al mostrar contactos {e}")
        finally:
            cerrar_session(conexion,cursor)

def mostrar_contactosTrabajo():
    conexion, cursor = obtener_conexion()
    if conexion and cursor:
        try:
            cursor.execute('SELECT * FROM "contactotrabajo" ORDER BY "id" ASC')
            contactos = cursor.fetchall()
            for row in contactos:
                contacto_trabajo = Contactotrabajo(row[0], row[1], row[2], row[3], row[4], row[5],row[6])
                contacto_trabajo.mostrar_info()
        except Exception as e:
            print(f"Error al mostrar contactos {e}")
        finally:
            cerrar_session(conexion,cursor)

def actualizar_contactosPersonal():
    conexion , cursor = obtener_conexion()
    if conexion and cursor:
        try:
            contacto_id = (input("Ingrese el ID del contacto a modificar: "))
        except ValueError:
                print("ID INCORRECTO. Por favor,Intentelo nuevamente.")

        cursor.execute('SELECT * FROM "contactopersonal" WHERE id = %s', (contacto_id,))
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
                UPDATE "contactopersonal"
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
    conexion , cursor = obtener_conexion()
    if conexion and cursor:
        try:
            contactoId = input("Digite el ID del contacto a modificar: -> ")
        except ValueError:
            print(f"Error id incorrecto, vuelva a intentar!!")

        cursor.execute('SELECT * FROM "contactotrabajo" WHERE id = %s', (contactoId))
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
                print("Actualizacion contactotrabajo exitosa!!!")
                conexion.commit()
            except Exception as e: 
                print(f"Error al actulizar contacto!! {e} ")
            finally:
                cerrar_session(conexion, cursor)
def eliminar_contactoPersonal():
    conexion, cursor = obtener_conexion()
    if conexion and cursor:
        id = input("Digite un id a eliminar: --> ")
        cursor.execute('SELECT * FROM "contactopersonal" WHERE id = %s ' ,(id))
        if cursor.fetchone() is None:
            print(f"Error el id {id} no existe en la base de datos ")
            return 
        try:
            query = '''DELETE from "contactopersonal" WHERE id = %s'''
            parametro = (id)
            cursor.execute(query,parametro)
            print("Contacto eliminado exitosamente!!!")
            conexion.commit()
        except Exception as e:
            print(f"error al eliminar usuario {e}")
        finally:
            cerrar_session(conexion, cursor)  
def eliminar_contactoTrabajo():
    conexion, cursor = obtener_conexion()
    if conexion and cursor:
        id = input("Digite un id a eliminar: --> ")
        cursor.execute('SELECT * FROM "contactotrabajo" WHERE id = %s ' ,(id))
        if cursor.fetchone() is None:
            print(f"Error el id {id} no existe en la base de datos ")
            return 
        try:
            query = '''DELETE from "contactotrabajo" WHERE id = %s'''
            parametro = (id)
            cursor.execute(query,parametro)
            print("Contacto eliminado exitosamente!!!")
            conexion.commit()
        except Exception as e:
            print(f"error al eliminar usuario {e}")
        finally:
            cerrar_session(conexion, cursor)        

def agregar_FavoritoPersonal():
    conexion , cursor = obtener_conexion()
    if conexion and cursor:
        try:
            fav_id = input("Digite un id para agregar a favorito: --> ")
        except ValueError:
                print("Error, vuelva a intentar!! ")
        cursor.execute('SELECT * FROM "contactopersonal" WHERE id = %s',(fav_id))
        if cursor.fetchone() is None:
            print(f"Erro el id {fav_id} no existe en la base de datos ")
            return
        else: 
            try:
                query=('UPDATE "contactopersonal" SET favorito= True WHERE id= %s ')
                paramentros=(fav_id )
                cursor.execute(query, paramentros)
                print(f"Contacto con el id {fav_id} agregado a favorito con exito!!! ")
                conexion.commit()
            except Exception as e:
                print(f"Error al agregar a favorito {e}")
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
                    favorito = False 
                    contacto = Contactopersonal(None, nombreCompleto, email, numero, pais, genero,favorito)
                    Agregar_ContactoPersonal(contacto)  
                    menu_opciones()
                    break
                elif numero_opc2 == "2":
                    nombreCompleto = input("Ingrese el nombre completo: ").upper()
                    email = input("Ingrese el email: ").upper()
                    numero = input("Ingrese el número: ").upper()
                    empresa = input("Ingrese La empresa: ").upper()
                    instagram = input("Ingrese el instagram: ").upper()
                    favorito = False
                    contacto = Contactotrabajo(None,nombreCompleto, email, numero, empresa, instagram,favorito)
                    agregar_ContactoTrabajo(contacto)
                    menu_opciones()
                    break
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
        elif numero_opc == "4":
            while True:
                menu_opciones3()
                numero_opc5 = input("Digite una opcion: --> ")
                if numero_opc5 == "1":
                    eliminar_contactoPersonal()
                elif numero_opc5 == "2":
                    eliminar_contactoTrabajo()
                elif numero_opc5 == "3":
                    print("Volviendo al MenuMain!!")
                    menu_opciones()
                    break
                else:
                    print("Opcion incorrecta , vuelva a intentar ")
        elif numero_opc == "5":
            while True:
                menu_opciones3()
                numero_opc6 = input("Digite una opcion: --> ")
                if numero_opc6 == "1":
                    agregar_FavoritoPersonal()
                elif numero_opc6 == "2":
                    pass
                elif numero_opc6 == "3":
                    print("Volviendo al MenuMain!! ")
                    menu_opciones()
                    break
                else:
                    print("opcion incorrecta,vuelva a intentar ")

        else:
             print("Error vuelva a digitar un numero ")


            

MenuMain()