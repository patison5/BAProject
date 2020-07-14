import json
import os
import config
import string
from contextlib import closing
import pymysql
from pymysql.cursors import DictCursor
import sqlite3

database = "mydatabase.db"

class ImagesController:
    
    # Вся информация организаций
    data_set = {
        "title": "Студия дизайна и полиграфии", 
        "logo": "http://127.0.0.1:5000/static/images/icons/img-10.svg",
        "text": "Студия дизайна и полиграфии оказывает широкий спектр услуг производства и печати: оперативная печать фото на документы, копирования/канирование, разработка и производство полиграфической продукции, разработка дизайна и фирменного стиля, а также верстка, брошюровка, печать визиток и многое другое", 
        "address": [
            "121099, Г. Москва",
            "ул. Новый Арбат, д.36",
        ], 
        "phones": [
            "+7 (495) 633-60-02",
        ],
        "email": "kow@mos.ru",
        "link": "https://www.mos.ru/kos",
        "barcode": "http://127.0.0.1:5000/static/images/icons/img-1.svg",
        "timetable": "ПН-ЧТ – 08:00 - 17:00 ПТ – 08:00 - 15:45 СБ-ВС – выходной",
        "images": [
            {
                "src": "http://127.0.0.1:5000/static/images/icons/Resurs_1.png",
                "desc": "Фото на документы"
            },
            {
                "src": "http://127.0.0.1:5000/static/images/icons/Resurs_1.png",
                "desc": "Поликлиника медицинского центра"
            },
            {
                "src": "http://127.0.0.1:5000/static/images/icons/Resurs_1.png",
                "desc": "Фото на документы"
            },
            {
                "src": "http://127.0.0.1:5000/static/images/icons/Resurs_1.png",
                "desc": "Фото на документы"
            },
        ] 
    }
    

    def __init__ (self):
        self.conn = sqlite3.connect(database, timeout=10)
        self.cursor = self.conn.cursor()
        print("ImagesController created")


    def drop_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS images""")
        self.conn.commit()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            src TEXT NOT NULL,
            desc TEXT
        )''')
        self.conn.commit()

    def drop_additional(self):
        self.cursor.execute("""DROP TABLE IF EXISTS org_images""")
        self.cursor.execute("""DROP TABLE IF EXISTS srv_images""")
        self.cursor.execute("""DROP TABLE IF EXISTS pst_images""")
        self.cursor.execute("""DROP TABLE IF EXISTS trv_images""")
        self.cursor.execute("""DROP TABLE IF EXISTS msc_images""")
        self.conn.commit()

    def create_additional(self):
        self.cursor.execute('''CREATE TABLE org_images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_id INTEGER,
            organization_id INTEGER,
            FOREIGN KEY (image_id) REFERENCES images (id),
            FOREIGN KEY (organization_id) REFERENCES organizations (id)
        )''')
        self.cursor.execute('''CREATE TABLE srv_images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_id INTEGER,
            service_id INTEGER,
            FOREIGN KEY (image_id) REFERENCES images (id),
            FOREIGN KEY (service_id) REFERENCES services (id)
        )''')
        self.cursor.execute('''CREATE TABLE pst_images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_id INTEGER,
            poster_id INTEGER,
            FOREIGN KEY (image_id) REFERENCES images (id),
            FOREIGN KEY (poster_id) REFERENCES posters (id)
        )''')
        self.cursor.execute('''CREATE TABLE trv_images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_id INTEGER,
            travel_id INTEGER,
            FOREIGN KEY (image_id) REFERENCES images (id),
            FOREIGN KEY (travel_id) REFERENCES travels (id)
        )''')
        self.cursor.execute('''CREATE TABLE msc_images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_id INTEGER,
            misc_id INTEGER,
            FOREIGN KEY (image_id) REFERENCES images (id),
            FOREIGN KEY (misc_id) REFERENCES misc (id)
        )''')
        self.conn.commit()

    def get_image_info (self):
        return self.data_set


    def update_image_info (self, data):
        # в data придет информация которую нужно обновить. минимум 1 какое-то поле, максимум все поля
        return True




    def init_data(self):

        self.cursor.execute(''' 
            INSERT INTO images(
                src,
                desc
            )
            VALUES(?,?) ''', (
                "http://127.0.0.1:5000/static/images/icons/img-10.svg",
                "desc",
            )
        )
        self.conn.commit()

        self.cursor.execute(''' 
            INSERT INTO org_images(
                image_id,
                organization_id
            )
            VALUES(?,?) ''', (
                1,
                1
            )
        )
        self.conn.commit()