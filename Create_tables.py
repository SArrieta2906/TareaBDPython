from Init_BD import *
import csv


def create_tables():
    '''
    Funcion que crea tres tablas en la base de datos: 'repositorio_musica', 'reproduccion' y 'lista_favoritos', en caso de que no existan.
    Cada tabla tiene sus respectivas columnas, tambien crea la view 'ArtistStats' y la funcion 'Promedio'.

    Parametros:
        No posee.

    Retorno:
        No posee. Crea las tablas en la base de datos y realiza un commit a la base de datos.
    '''
    execute_query('''
            IF OBJECT_ID (N'repositorio_musica', N'U') IS NULL 
            CREATE TABLE repositorio_musica(
                id INTEGER PRIMARY KEY IDENTITY(1,1),
                position INTEGER,
                artist_name VARCHAR(50),
                song_name VARCHAR(100),
                days INTEGER,
                top_10 INTEGER,
                peak_position INTEGER,
                peak_position_time VARCHAR(7),
                peak_streams INTEGER,
                total_streams INTEGER
            );
        ''', "tabla 'repositorio_musica' creada")

    execute_query('''
            IF OBJECT_ID (N'reproduccion', N'U') IS NULL 
                BEGIN
                    CREATE TABLE reproduccion(
                        id INTEGER PRIMARY KEY,
                        song_name VARCHAR(100),
                        artist_name VARCHAR(50),
                        fecha_reproduccion DATE,
                        cant_reproducciones INTEGER,
                        favorito BIT
                        );
                END
        ''', "tabla 'reproduccion' creada")

    execute_query('''
            IF OBJECT_ID (N'lista_favoritos', N'U') IS NULL 
                BEGIN
                    CREATE TABLE lista_favoritos(
                        id INTEGER PRIMARY KEY,
                        song_name VARCHAR(100),
                        artist_name VARCHAR(50),
                        fecha_agregada DATE
                        );
                END
        ''', "tabla 'lista_favoritos' creada")

    execute_query('''
        CREATE OR ALTER VIEW [ArtistStats] AS
        SELECT artist_name, MIN(peak_position) peak_position, SUM(cast(top_10 as bigint)) Total_top_15, SUM(cast(total_streams as bigint))sum_streams, COUNT(*)num_songs
        FROM repositorio_musica 
        GROUP BY artist_name
        ''', "View 'ArtistStats' Creada")
    
    execute_query('''
        CREATE OR ALTER FUNCTION Promedio (@cantidad INTEGER, @suma INTEGER) 
        RETURNS INTEGER AS
        BEGIN
            DECLARE @avg INTEGER
            SET @avg = @suma/@cantidad
            RETURN @avg
        END 
        ''', "Funcion 'Promedio' Creada")

    connection.commit()


def insert_data():
    '''
    Funcion que lee un archivo CSV llamado 'song.csv', que contiene canciones y datos relacionados con ellas, e inserta los datos en la tabla 'repositorio_musica'.

    Parametros:
        No posee.

    Retorno:
        No posee. Inserta los datos en la base de datos y realiza un commit a la base de datos.
    '''
    with open('song.csv', newline='', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for row in reader:
            stringQuery = r'''
                    IF NOT EXISTS(SELECT * FROM repositorio_musica WHERE artist_name = '{1}' AND song_name = '{2}')
                    INSERT INTO
                        repositorio_musica(position, artist_name, song_name, days, top_10, peak_position, peak_position_time, peak_streams, total_streams)
                    VALUES
                        ({0}, '{1}', '{2}', {3}, {4}, {5}, '{6}', {7}, {8});
                    '''
            # Se eliminan los "'" de las canciones y de los artistas evitando problemas al insertar
            arr = row[0].split(";")
            arr[1] = arr[1].replace("'", "''").strip()
            arr[2] = arr[2].replace("'", "''").strip()
            # Se establece el formato al stringQuery y luego se ejecuta el query
            Query.execute(stringQuery.format(*arr))

    connection.commit()
