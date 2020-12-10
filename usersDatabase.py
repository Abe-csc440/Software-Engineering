"""
    User profiles & helpers
    ~~~~~~~~~~~~~~~~~~~~~~
"""
import sqlite3


class UserProfile(object):

    def __init__(self, database):
        self.conn = sqlite3.connect('users.db')

    '''def create_schema(self):
        createTable = """CREATE TABLE IF NOT EXISTS profiles(
        NAME TEXT PRIMARY KEY,
        FULLNAME TEXT NOT NULL, 
        EMAIL TEXT NOT NULL 
        );"""
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute(createTable)
        self.conn.commit()'''

    def add_profile(self, name, fullName, email):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO profiles values (?,?,?)', (name, fullName, email))
        self.conn.commit()

    def get_profile(self, name):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM profiles WHERE name=?', (name,))
        result = cursor.fetchone()
        if not result:
            return None
        return Profile(result[0], result[1], result[2])

    def delete_profile(self, name):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM profiles WHERE name=?', (name,))
        self.conn.commit()


class Profile(object):
    def __init__(self, name, fullName, email):
        self.name = name
        self.fullName = fullName
        self.email = email
