import json
import os
import config
import string
from contextlib import closing
import pymysql
from pymysql.cursors import DictCursor
import sqlite3

database = "mydatabase.db"

class OrganizationsController:
    
    # Вся информация организаций

    data_set = [
        {
            "id": '0',
            "title": "Комитет общественных связей и молодежной политики города Москвы", 
            "logo": "http://127.0.0.1:5000/static/images/icons/img-10.svg",
            "text": "kv ipsum dolor sit amet, consectetur adipisicing elit. Maxime iure adipisci fuga tenetur repudiandae explicabo ad voluptas unde distinctio? Sint laudantium quae minus nesciunt repellendus doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.", 
            "right_part": {
                "image": "http://127.0.0.1:5000/static/images/woman.png",
                "title": "Драгунова Екатерина Вячеслаовна",
                "desc": "Председатель коммитета общественных сязей и молодежной политики города Москвы,"
            },
            "address": [
                "121099, Г. Москва",
                "ул. Новый Арбат, д.36",
                "19 этаж, кабинет 1928"
            ], 
            "phones": [
                "+7 (495) 633-60-02",
                "+7 (495) 633-60-02 - Офис",
                "+7 (495) 633-60-02 - Пресс-служба"
            ],
            "email": "kow@mos.ru",
            "link": "https://www.mos.ru/kos",
            "timetable": "ПН-ЧТ – 08:00 - 17:00 ПТ – 08:00 - 15:45 СБ-ВС – выходной"
        },
        {
            "id": '1',
            "title": "Комитет общественных связей и молодежной политики города Москвы", 
            "logo": "http://127.0.0.1:5000/static/images/icons/img-10.svg",
            "text": "kv ipsum dolor sit amet, consectetur adipisicing elit. Maxime iure adipisci fuga tenetur repudiandae explicabo ad voluptas unde distinctio? Sint laudantium quae minus nesciunt repellendus doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.", 
            "right_part": {
                "image": "http://127.0.0.1:5000/static/images/woman.png",
                "title": "Драгунова Екатерина Вячеслаовна",
                "desc": "Председатель коммитета общественных сязей и молодежной политики города Москвы,"
            },
            "address": [
                "121099, Г. Москва",
                "ул. Новый Арбат, д.36",
                "19 этаж, кабинет 1928"
            ], 
            "phones": [
                "+7 (495) 633-60-02",
                "+7 (495) 633-60-02 - Офис",
                "+7 (495) 633-60-02 - Пресс-служба"
            ],
            "email": "kow@mos.ru",
            "link": "https://www.mos.ru/kos",
            "timetable": "ПН-ЧТ – 09:00 - 17:00 ПТ – 08:00 - 15:45 СБ-ВС – выходной"

        },
    ]

    # пример того, как должны возвращаться заголовки (в link помещается id этой организации)
    organizations_titles = [
        {
            "variable": "A",
            "elements": [
                {
                    "text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
                    "link": "1"
                },
                {
                    "text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
                    "link": "3"
                }
            ]
        },
        {
            "variable": "B",
            "elements": [
                {
                    "text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
                    "link": "2"
                },
                {
                    "text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
                    "link": "5"
                },
                {
                    "text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
                    "link": "8"
                }
            ]
        },
    ]

    

    def __init__ (self):
        self.conn = sqlite3.connect(database, timeout=10)
        self.cursor = self.conn.cursor()
        print("OrganizationsController created")

    def drop_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS organizations""")
        self.conn.commit()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE organizations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            image INTEGER NOT NULL,
            address TEXT NOT NULL,
            phones TEXT NOT NULL,
            email TEXT NOT NULL,
            link TEXT NOT NULL,
            barcode TEXT NOT NULL,
            timetable TEXT NOT NULL,
            FOREIGN KEY (image) REFERENCES images (id)
        )
        ''')
        self.conn.commit()

    def get_organization_titles (self):
        self.cursor.execute('''
        SELECT title FROM organizations
        ''')

        return self.cursor.fetchall()


    def get_all_organizations (self): 
        return self.data_set


    def get_single_organization (self, id):
        # находит и возвращает организацию по id
        return self.data_set[id]


    def create_new_organization (self, data):
        # в data придет вся необходимая информация для добавления новой организации
        return True


    def update_organization (self, data):
        # в data придет информация которую нужно обновить. минимум 1 какое-то поле, максимум все поля
        return True


    def delete_organization (self, id):
        # удаляет организацию по id
        return True