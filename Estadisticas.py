from Init_BD import *

def top_15():
    '''
    Funcion que utiliza una query y una view para buscar los 15 artistas con mas reproducciones en la view ArtistStats.

    Parametros:
        No recibe parametros.
    
    Retorno:
        No posee.
    '''
    stringQuery = r'''
        SELECT TOP (15) [artist_name], [Total_top_15]
        FROM [Tarea1DB].[dbo].[ArtistStats] ORDER BY [Total_top_15] DESC
        '''

    execute_query(stringQuery, "busqueda finalizada\n")
    results = Query.fetchall()
    for n, i in enumerate(results):
        print(f"{n+1}. {i[0]} con {i[1]} reproducciones")

def peak_position():
    '''
    Funcion que utiliza una query y una view para buscar la posicion mas alta alcanzada por un artista en la view ArtistStats.

    Parametros:
        No recibe parametros.

    Retorno:
        No posee.
    '''
    stringQuery = r'''
        SELECT artist_name, peak_position FROM [Tarea1DB].[dbo].[ArtistStats] WHERE [artist_name] = '{0}'
        '''
    artist = input("ingresa el nombre del artista o presiona enter para cancelar la operacion: ")
    if(artist == ""):
        return
    
    execute_query(stringQuery.format(artist), "")
    results = Query.fetchall()
    if(len(results) == 0):
       print("artista no encontrado")
       return
       
    print(f"la posicion mas alta alcanzada por {results[0][0]} es {results[0][1]}")

def avg_streams():
    '''
    Funcion que utiliza una query y una view para buscar el promedio de reproducciones de un artista en la view ArtistStats.

    Parametros:
        No recibe parametros.

    Retorno:
        No posee.
    '''
    stringQuery = r'''
        SELECT artist_name, dbo.Promedio(num_songs, sum_streams) FROM [Tarea1DB].[dbo].[ArtistStats] WHERE [artist_name] = '{0}'
        '''
    artist = input("ingresa el nombre del artista o presiona enter para cancelar la operacion: ")
    if(artist == ""):
        return
    
    execute_query(stringQuery.format(artist), "")
    results = Query.fetchall()
    if(len(results) == 0):
        print("artista no encontrado")
        return

    print(f"promedio de reproducciones de {results[0][0]} es {results[0][1]}")
