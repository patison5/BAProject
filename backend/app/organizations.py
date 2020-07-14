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
        }
    ]
    

    def __init__ (self):
        self.conn = sqlite3.connect(database, timeout=10)
        self.cursor = self.conn.cursor()
        print("OrganizationsController created")

    def drop_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS organizations""")
        self.conn.commit()

    def create_table(self):
        self.drop_table()

        self.cursor.execute('''
        CREATE TABLE organizations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            image INTEGER,
            text TEXT,
            address TEXT,
            phones TEXT,
            email TEXT,
            link TEXT,
            barcode TEXT,
            timetable TEXT,
            FOREIGN KEY (image) REFERENCES images (id)
        )
        ''')
        self.conn.commit()

        self.cursor.execute('''
        INSERT INTO organizations (
            title,
            image,
            text,
            address,
            phones,
            email,
            link,
            barcode,
            timetable
        )
        VALUES (?,?,?,?,?,?,?,?,?)''', (
            "Комитет общественных связей и молодежной политики города Москвы", 
            "http://127.0.0.1:5000/static/images/icons/img-10.svg", 
            "kv ipsum dolor sit amet, consectetur adipisicing elit. Maxime iure adipisci fuga tenetur repudiandae explicabo ad voluptas unde distinctio? Sint laudantium quae minus nesciunt repellendus doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.",
            json.dumps([
                "121099, Г. Москва",
                "ул. Новый Арбат, д.36",
                "19 этаж, кабинет 1928"
            ]),
            json.dumps([
                "+7 (495) 633-60-02",
                "+7 (495) 633-60-02 - Офис",
                "+7 (495) 633-60-02 - Пресс-служба"
            ]),
            "kow@mos.ru",
            "https://www.mos.ru/kos",
            "barcode",
            "ПН-ЧТ – 09:00 - 17:00 ПТ – 08:00 - 15:45 СБ-ВС – выходной")
        )
        self.conn.commit()

        self.cursor.execute('''
        INSERT INTO organizations (
            title,
            image,
            text,
            address,
            phones,
            email,
            link,
            barcode,
            timetable
        )
        VALUES (?,?,?,?,?,?,?,?,?)''', (
            "Комитет общественных связей и молодежной политики города Москвы", 
            "http://127.0.0.1:5000/static/images/icons/img-10.svg", 
            "kv ipsum dolor sit amet, consectetur adipisicing elit. Maxime iure adipisci fuga tenetur repudiandae explicabo ad voluptas unde distinctio? Sint laudantium quae minus nesciunt repellendus doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.",
            json.dumps([
                "121099, Г. Москва",
                "ул. Новый Арбат, д.36",
                "19 этаж, кабинет 1928"
            ]),
            json.dumps([
                "+7 (495) 633-60-02",
                "+7 (495) 633-60-02 - Офис",
                "+7 (495) 633-60-02 - Пресс-служба"
            ]),
            "kow@mos.ru",
            "https://www.mos.ru/kos",
            "barcode",
            "ПН-ЧТ – 09:00 - 17:00 ПТ – 08:00 - 15:45 СБ-ВС – выходной")
        )
        self.conn.commit()

    def get_organization_titles (self):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute('''
            SELECT id, title FROM organizations
        ''')


        data = cdb.fetchall();

        print(data)
        json = []

        for item in data:
            json.append({
                "variable": "A",
                "elements": [{
                    "id":   item[0],
                    "text": item[1],
                }]
            })


        return json


    def get_all_organizations (self): 
        return self.data_set


    def get_single_organization (self, id):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        # cdb.execute('''
        #     SELECT * FROM organizations
        #     WHERE id = ?
        # ''', (str(id)))

        cdb.execute('''
            SELECT *
            FROM organizations
            INNER JOIN images
            ON organizations.image = image.id
            WHERE id = ?
        ''', (str(id)))


        data = cdb.fetchone();
        print(data)

        return {
            "id":           data[0],
            "title":        data[1], 
            "logo":         data[2],
            "text":         data[3], 
            "address":      json.loads(data[4]), 
            "phones":       json.loads(data[5]),
            "email":        data[6],
            "link":         data[7],
            "barcode":      data[8],
            "timetable":    data[9]
        }


    def create_new_organization (self, data):
        # в data придет вся необходимая информация для добавления новой организации
        return True


    def update_organization (self, data):
        # в data придет информация которую нужно обновить. минимум 1 какое-то поле, максимум все поля
        return True


    def delete_organization (self, id):
        # удаляет организацию по id
        return True