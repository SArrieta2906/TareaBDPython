from Init_BD import *
import datetime


def show_playback():
    '''
    Funcion que muestra las reproducciones ordenadas por fecha o por cantidad de veces reproducida.

    Parametros:
        No posee.

    Retorno:
        No posee.
    '''
    stringQuery = r'''
            SELECT * FROM reproduccion
            ORDER BY {0} {1}
            '''

    while True:
        print("Elija la forma en la que desea ordenar el registro de reproducciones:")
        print("1.fecha de reproduccion\n2.cantidad de veces reproducida\n3.cancelar operación")
        opcionParametro = input("opcion: ")

        if(opcionParametro == "3"):
            return

        print("\nelija una opcion")
        print("1.Ascendente\n2.Descentente")
        opcionOrden = input("opcion: ")

        match opcionOrden:
            case "1":
                opcionOrden = "ASC"
            case "2":
                opcionOrden = "DESC"
            case _:
                print("operacion invalida")
                break

        match opcionParametro:
            case "1":
                execute_query(stringQuery.format(
                    "fecha_reproduccion", opcionOrden), "")
            case "2":
                execute_query(stringQuery.format(
                    "cant_reproducciones", opcionOrden), "")
            case _:
                print("operacion invalida")
                break

        results = Query.fetchall()

        for i in results:
            print(
                f"{i[1]} de {i[2]}\nPrimera reproduccion:{i[3]}\nCantidad de reproducciones {i[4]}\n")


def add_and_update_song(song: tuple):
    '''
    Funcion que agrega una cancion a la tabla 'reproduccion' o actualiza la cantidad
     de veces que ha sido reproducidaen caso de que no exista.

    Parametros:
        song (tuple): Tupla con la informacion de la cancion (id, nombre, artista, duracion)

    Retorno:
        No posee.
    '''
    stringQuery = r'''
            IF NOT EXISTS(SELECT * FROM reproduccion WHERE id = {0})
                BEGIN
                    INSERT INTO
                    reproduccion(id, song_name, artist_name, fecha_reproduccion, cant_reproducciones, favorito)
                    VALUES
                    ({0}, '{1}', '{2}', CONVERT(date, '{3}', 23), {4}, {5});
                END
            ELSE
                BEGIN
                    UPDATE reproduccion
                    SET cant_reproducciones = cant_reproducciones + 1
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
    
    execute_query(stringQuery.format(song[0], song[3], song[2], date, 1, 0), f"\nsonando {song[3]} de {song[2]}")
    connection.commit()
