import pyodbc

try:
    #connection = pyodbc.connect('DRIVER={SQL Server};SERVER=JONATHAN\SQLEXPRESS;DATABASE=Tarea1DB;Trusted_Connection=yes;')
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-J536784K\SQLEXPRESS;DATABASE=Tarea1DB;Trusted_Connection=yes;')
    Query = connection.cursor()
    print("conexión exitosa")
except Exception as e:
    print(e)
    exit()


def execute_query(query, message):
    '''
    Funcion que sirve para evitar problemas con el manejo de querys en SQL SERVER. Finaliza el programa en caso de error

    Parametros:
        query (str): Query que irá en el archivo.
        message (str): Mensaje que indica si el programa fue ejecutado correctamente.

    Retorno:
        No posee. Termina el programa en caso de error.
    '''
    try:
        Query.execute(query)
        print(message)
    except Exception as e:
        print(e)
        exit()


def search_song():
    '''
    Funcion que busca una canción en la tabla repositorio_musica.

    Parametros:
        No posee.

    Retorno:
        results (list): Lista que contiene la información de la canción encontrada.
    '''
    results = []

    while len(results) == 0:
        name = input(
            "Ingresa el nombre de la canción o presiona enter para cancelar la operacion: ")
        if (name == ""):
            return []

        stringQuery = r'''
            SELECT * FROM repositorio_musica
            WHERE song_name = '{0}'
            '''

        execute_query(stringQuery.format(name.replace("'", "''")),
                      "-----busqueda finalizada-----")
        results = Query.fetchall()

        if len(results) == 0:
            print("cancion no encontrada")

    for i, row in enumerate(results):
        print(f"{i+1}. {row[3]} de {row[2]}")

    if len(results) > 1:
        option = int(input("Selecciona el numero de la canción correcta: "))-1
        results = [results[option]]

    return results[0]
