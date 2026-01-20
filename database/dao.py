from database.DB_connect import DBConnect
from model.artist import Artist

class DAO:

    @staticmethod
    def get_all_artists():

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT *
                FROM artist a
                """
        cursor.execute(query)
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'])
            result.append(artist)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_artists_by_album(num_album):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """
        SELECT A.id, A.name
        FROM artist A, album AL
        WHERE A.id = AL.artist_id
        GROUP BY A.id
        HAVING COUNT(*) >= %s"""
        cursor.execute(query, (num_album,))
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'])
            result.append(artist)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_weighted_edges_by_artists(a1, a2):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = None
        query = """
        SELECT  COUNT(*) as weight
        from (select t1.genre_id , a1.id 
        from artist a1, album al1, track t1
        where a1.id = al1.artist_id and t1.album_id = al1.id and a1.id = 27
        group by a1.id, t1.genre_id) as TABELLA1,
        (selecT t2.genre_id, a2.id
        from artist a2, album al2, track t2
        where a2.id = al2.artist_id and t2.album_id = al2.id and a2.id = 6
        group by a2.id, t2.genre_id) as TABELLA2 
        where TABELLA1.genre_id = TABELLA2.genre_id;"""
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result


