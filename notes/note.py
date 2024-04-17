import connection 

connector= connection.connect()
database = connector[0]
cursor = connector[1]


class note:
    def __init__(self, user_id, title = "", description = ""):
        self.user_id = user_id
        self.title = title
        self.description = description 

    def store(self):
        
        sql = "INSERT INTO notes VALUES (null, %s, %s, %s, NOW())"
        note = (self.user_id, self.title, self.description)

        try: 
            cursor.execute(sql, note)
            database.commit()

            response =  [cursor.rowcount, self]

        except:
            response = [0, self]

        return response 

    def show(self):

        sql = f"SELECT * FROM notes WHERE user_id = {self.user_id}"

        cursor.execute(sql)
        notes = cursor.fetchall()

        for note in notes:
            print("\n*******************************")
            print(note [2])
            print(note [3])
            print("\n*******************************")
            
            
    def delete(self):
        sql = f"DELETE FROM  notes WHERE user_id= {self.user_id} AND title LIKE '%{self.title}%' "
        
        cursor.execute(sql)
        database.commit()
        
        return [cursor.rowcount, self]


