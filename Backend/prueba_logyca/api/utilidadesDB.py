from django.db import connection

def getNumerosPrimos(query_):
    cursor = connection.cursor()
    cursor.execute(query_)
    return cursor.fetchall()