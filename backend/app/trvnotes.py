import json
import os
import config
import string
from contextlib import closing
import pymysql
from pymysql.cursors import DictCursor
import sqlite3

database = "mydatabase.db"

class TrvnotesController:

    def __init__ (self):
        self.conn = sqlite3.connect(database, timeout=10)
        self.cursor = self.conn.cursor()
        print("TrvnotesController created")

    def drop_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS trvnotes""")
        self.conn.commit()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE trvnotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            travel_id INTEGER NOT NULL,
            data TEXT NOT NULL,
            image INTEGER,
            FOREIGN KEY (travel_id) REFERENCES travels (id),
            FOREIGN KEY (image) REFERENCES images (id)
        )
        ''')
        self.conn.commit()


    def init_data(self):
        return 0
