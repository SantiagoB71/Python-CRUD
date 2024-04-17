import datetime
import hashlib
import connection as connect

connector= connect.connect()
database = connector[0]
cursor = connector[1]

class User:
    def __init__(self, email, password, name, lastName):
        self.name = name
        self.lastName = lastName
        self.email = email 
        self.password = password 

    def register(self):
        date = datetime.datetime.now()

        encrypt = hashlib.sha256()
        encrypt.update(self.password.encode('utf8'))

        sql = "INSERT INTO users VALUES (null, %s , %s, %s, %s, %s )"
        user = (self.name, self.lastName, self.email, encrypt.hexdigest(), date) 

        try: 
            cursor.execute(sql, user)
            database.commit() 
            response = [cursor.rowcount, self ]
        except: 
            response = [0, self] 

        return response

    def identify(self):
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"

        encrypt = hashlib.sha256()
        encrypt.update(self.password.encode('utf8'))

        user = (self.email, encrypt.hexdigest())

        cursor.execute(sql, user)

        result = cursor.fetchone()
        return result