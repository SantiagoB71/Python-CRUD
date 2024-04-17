import mysql.connector

def connect():
    database = mysql.connector.connect(
        host = "10.17.70.39", 
        user = "usuario1", 
        passwd = "Ucc2022Ser", 
        database = "notebook",
        port = 3306
    )

    cursor = database.cursor(buffered = True)

    return [database,cursor]