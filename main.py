from Create_tables import *
from Reproduccion import *
from Favoritos import *
from Search import *
from Estadisticas import *

def menu():
    '''
    Función que muestra el menú principal y ejecuta la opción elegida por el usuario.

    Parametros:
        No posee.

    Retorno:
        No posee.
    '''
    flag_continue = True
    while (flag_continue):
        print("\n0. Terminar el programa.\n1. Crear tablas.\n2. Poblar 'repositorio_musica'\n3. Mostrar canciones en reproducción.\n4. Añadir cancion a favoritos.\n5. Eliminar cancion de favoritos.\n6. Mostrar canciones favoritas.\n7. Reproducir una cancion.\n8. Buscar una cancion en la tabla Reproduccion.\n9. Mostrar todas las canciones escuchadas en los ultimos X dias.\n10. Buscar por nombre de cancion y por artista.\n11. Top 15 artistas con mayor cantidad total de veces en que sus canciones han estado en el top 10.\n12. Peak position de un artista.\n13. Promedio de streams totales.")
        option = input("\nIngresa la opcion que desees: ")
        match option:
            case "0":
                flag_continue = False
            case "1":
                create_tables()
            case "2":
                insert_data()
            case "3":
                show_playback()
            case "4":
                add_favorites()
            case "5":
                delete_favorites()
            case "6":
                show_favorites()
            case "7":
                results = search_song()
                add_and_update_song(results)
            case "8":
                search_reproduccion()
            case "9":
                songs_to_date()
            case "10":
                search_name_artist()
            case "11":
                top_15()
            case "12":
                peak_position()
            case "13":
                avg_streams()
            case _:
                print("Valor incorrecto. Intenta nuevamente.")


def main():
    '''
    Función principal que llama a la función menu()

    Parametros:
        No posee.

    Retorno:
        No posee.
    '''
    menu()


main()
connection.close()
