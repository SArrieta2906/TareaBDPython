from Init_BD import *
import datetime


def add_favorites():
    '''
    Funcion que agrega una cancion a la lista de favoritos en la base de datos. Si ya existe, actualiza su fecha.

    Parametros:
        No posee parametros.

    Retorno:
        No posee retorno. Actualiza la base de datos.
    '''
    results = search_song()
    if len(results) == 0:
        return
    stringQuery = r'''
        IF NOT EXISTS(SELECT * FROM lista_favoritos WHERE id = {0})
            BEGIN
                INSERT INTO
                lista_favoritos(id, song_name, artist_name, fecha_agregada)
                VALUES
                ({0}, '{1}', '{2}', CONVERT(date, '{3}', 23));

                UPDATE reproduccion
                SET favorito = 1
                WHERE id = {0}
            END
    '''
    date = input("\nIngresa la fecha actual en el formato (YYYY-MM-DD): ")
    while True:
        try:
            datetime.date.fromisoformat(date)
            break
        except:
            print("formato invalido")
            date = input("\nIngresa la fecha actual en el formato (YYYY-MM-DD): ")
            continue

    execute_query(stringQuery.format(
        results[0], results[3], results[2], date), "añadida a favoritos")
    connection.commit()


def delete_favorites():
    '''
    Funcion que elimina una cancion de la lista de favoritos en la base de datos.

    Parametros:
        No posee parametros.

    Retorno:
        No posee retorno. Actualiza la base de datos.
    '''
    results = []

    while len(results) == 0:
        name = input(
            "Ingresa el nombre de la canción o presiona enter para cancelar la operacion: ")
        
        if (name == ""):
            return

        stringQuery = r'''
            SELECT * FROM lista_favoritos
            WHERE song_name = '{0}'
            '''

        execute_query(stringQuery.format(name.replace("'", "''")), "-----busqueda finalizada-----")
        results = Query.fetchall()

        if len(results) == 0:
            print("cancion no se encuantra en favoritos")
            return

    if len(results) > 1:
        for i, row in enumerate(results):
            print(f"{i+1}. {row[1]} de {row[2]}")
        option = int(input("Selecciona el numero de la canción correcta: "))-1
        results = [results[option]]

    stringQuery = r'''
            DELETE FROM lista_favoritos
            WHERE id = {0}

            UPDATE reproduccion
            SET favorito = 0
            WHERE id = {0}
            '''

    execute_query(stringQuery.format(results[0][0]), "eliminada de favoritos")
    connection.commit()


def show_favorites():
    '''
    Función que muestra todas las canciones que se encuentran
    en la tabla lista_favoritos ordenadas alfabéticamente por el nombre de la canción.

    Parámetros:
        No recibe.

    Retorno:
        No posee.
    '''
    stringQuery = r'''
            SELECT * FROM lista_favoritos
            ORDER BY song_name
            '''
    Query.execute(stringQuery)
    result = Query.fetchall()

    print("Canciones favoritas:")
    for i in result:
        print(f"{i[1]} de {i[2]}")
