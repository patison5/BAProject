import json
import os
import config
import string
from contextlib import closing
import pymysql
from pymysql.cursors import DictCursor
import sqlite3

database = "mydatabase.db"

class PostersController:
    
    # Вся информация организаций
    data_set = [
        {
            "title": "Комитет общественных связей и молодежной политики города Москвы", 
            "logo": "http://127.0.0.1:5000/static/images/woman.png",
            "text": "kv ipsum dolor sit amet, consectetur adipisicing elit. Maxime iure adipisci fuga tenetur repudiandae explicabo ad voluptas unde distinctio? Sint laudantium quae minus nesciunt repellendus doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.", 
            "date": "22.02.12",
            "time": "13:00",
            "address": "Большой концертный зал",
            "img": "http://127.0.0.1:5000/static/images/afisha.png"
        },
        {
            "title": "Комитет общественных связей и молодежной политики города Москвы", 
            "logo": "http://127.0.0.1:5000/static/images/woman.png",
            "text": "kv ipsum dolor sit amet, consectetur adipisicing elit. Maxime iure adipisci fuga tenetur repudiandae explicabo ad voluptas unde distinctio? Sint laudantium quae minus nesciunt repellendus doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.", 
            "date": "22.02.12",
            "time": "13:00",
            "address": "Большой концертный зал",
            "img": "http://127.0.0.1:5000/static/images/afisha.png"
        },
        {
            "title": "Комитет общественных связей и молодежной политики города Москвы", 
            "logo": "http://127.0.0.1:5000/static/images/woman.png",
            "text": "kv ipsum dolor sit amet, consectetur adipisicing elit. Maxime iure adipisci fuga tenetur repudiandae explicabo ad voluptas unde distinctio? Sint laudantium quae minus nesciunt repellendus doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.", 
            "date": "22.02.12",
            "time": "13:00",
            "address": "Большой концертный зал",
        },
        {
            "title": "Комитет общественных связей и молодежной политики города Москвы", 
            "logo": "http://127.0.0.1:5000/static/images/woman.png",
            "text": "kv ipsum dolor sit amet, consectetur adipisicing elit. Maxime iure adipisci fuga tenetur repudiandae explicabo ad voluptas unde distinctio? Sint laudantium quae minus nesciunt repellendus doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.", 
            "date": "22.02.12",
            "time": "13:00",
            "address": "Большой концертный зал",
            "img": "http://127.0.0.1:5000/static/images/afisha.png"
        },
        {
            "title": "Комитет общественных связей и молодежной политики города Москвы", 
            "logo": "http://127.0.0.1:5000/static/images/woman.png",
            "text": "kv ipsum dolor sit amet, consectetur adipisicing elit. Maxime iure adipisci fuga tenetur repudiandae explicabo ad voluptas unde distinctio? Sint laudantium quae minus nesciunt repellendus doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.", 
            "date": "22.02.12",
            "time": "13:00",
        }
    ]

    

    def __init__ (self):
        self.conn = sqlite3.connect(database, timeout=10)
        self.cursor = self.conn.cursor()
        print("PostersController created")

    def drop_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS posters""")
        self.conn.commit()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE posters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            address TEXT NOT NULL,
            timetable TEXT NOT NULL,
            desc TEXT NOT NULL,
            image INTEGER,
            FOREIGN KEY (image) REFERENCES images (id)
        )
        ''')
        self.conn.commit()


    def get_all_afisha (self):
        # находит и возвращает организацию по id
        return self.data_set

    def get_single_afisha (self, id):
        # находит и возвращает организацию по id
        id = 0

        single_afisha = {
            "title":    self.data_set[id]['title'], 
            "logo":     self.data_set[id]['logo'], 
            "text":     self.data_set[id]['text'], 
            "date":     self.data_set[id]['date'],
            "time":     self.data_set[id]['time'],
            "address":  self.data_set[id]['address'],
            "img":      self.data_set[id]['img'],
        }

        return single_afisha


    def create_new_afisha (self, data):
        # в data придет вся необходимая информация для добавления новой организации
        return True


    def update_afisha (self, data):
        # в data придет информация которую нужно обновить. минимум 1 какое-то поле, максимум все поля
        return True


    def delete_afisha (self, id):
        # удаляет организацию по id
        return True