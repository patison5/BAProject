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
            "logo": "",
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
            timetable TEXT,
            logo INTEGER,
            barcode INTEGER,
            FOREIGN KEY (image)   REFERENCES images (id)
            FOREIGN KEY (logo)    REFERENCES images (id)
            FOREIGN KEY (barcode) REFERENCES images (id)
        )
        ''')
        self.conn.commit()


    def init_data(self):
        self.cursor.execute('''
        INSERT INTO organizations (
            title,
            logo,
            text,
            address,
            phones,
            email,
            link,
            timetable
        )
        VALUES (?,?,?,?,?,?,?,?)''', (
            "Комитет общественных связей и молодежной политики города Москвы", 
            1, # надо сделать инсерт этого в таблицу images (можно с пустым desc, но с определенным id, например 1) и после этого уже сюда написать этот id
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
            "ПН-ЧТ – 09:00 - 17:00 ПТ – 08:00 - 15:45 СБ-ВС – выходной")
        )
        self.conn.commit()

        self.cursor.execute('''
        INSERT INTO organizations (
            title,
            logo,
            text,
            address,
            phones,
            email,
            link,
            timetable
        )
        VALUES (?,?,?,?,?,?,?,?)''', (
            "Комитет общественных связей и молодежной политики города Москвы", 
            0, # надо сделать инсерт этого в таблицу images (можно с пустым desc, но с определенным id, например 1) и после этого уже сюда написать этот id
            "kv ipsum dolor sit amet, consectetur adipisicing elit. Maxime iure adipisci fuga tenetur repudiandae explicabo ad voluptas unde distinctio? Sint laudantium quae minus nesciunt repellendus doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.",
            json.dumps([
                "121099, Г. Москва"
            ]),
            json.dumps([
                "+7 (495) 633-60-02",
            ]),
            "kow@mos.ru",
            "https://www.mos.ru/kos",
            "ПН-ЧТ – 09:00 - 17:00 ПТ – 08:00 - 15:45 СБ-ВС – выходной")
        )
        self.conn.commit()


    def letter_index_in_data(self, data, letter):
        for i in range(len(data)):
            if data[i]["variable"] == letter:
                return i
        return -1


    def get_organization_titles (self):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute('''
            SELECT id, title FROM organizations
        ''')

        data = cdb.fetchall();

        json = []
        for element in data:
            letter_of_element = element[1][0]
            print("letter_of_element")
            print(letter_of_element)
            letter_index = self.letter_index_in_data(json, letter_of_element)
            if letter_index != -1:
                json[letter_index]["elements"].append(
                    {
                        "id": element[0],
                        "title": element[1]
                    }
                )
            else:
                tmp_obj = {
                    "variable": letter_of_element,
                    "elements": [
                        {
                            "id": element[0],
                            "title": element[1]
                        }
                    ],
                }
                json.append(tmp_obj)


        print(json)

        return json


    def get_all_organizations (self): 

        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute('''
            SELECT id, title, text FROM organizations
        ''')

        data = cdb.fetchall();
        json = []

        for item in data:
            json.append({
                "id":           item[0],
                "title":        item[1],
                "text":         item[2]
            })

        return json


    def get_single_organization (self, id):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        # ////////// Основной контент //////////
        cdb.execute('''
            SELECT *
            FROM organizations
            LEFT JOIN images
            ON organizations.image = images.id
            WHERE organizations.id = ?
        ''', (str(id)))


        data = cdb.fetchone();


        # ////////// фотографии //////////
        cdb.execute('''
            SELECT src
            FROM organizations
            LEFT JOIN images
            ON organizations.logo = images.id
            WHERE organizations.id = ?
        ''', (str(id)))
        logo = cdb.fetchone();

        cdb.execute('''
            SELECT src, desc, images.title as title
            FROM organizations
            LEFT JOIN images
            ON organizations.image = images.id
            WHERE organizations.id = ?
        ''', (str(id)))
        image = cdb.fetchone();

        cdb.execute('''
            SELECT src
            FROM organizations
            LEFT JOIN images
            ON organizations.barcode = images.id
            WHERE organizations.id = ?
        ''', (str(id)))
        barcode = cdb.fetchone();


        # ////////// Сервисы //////////
        cdb.execute('''
            SELECT id, title, image     
            FROM services
            WHERE organization_id = ?
        ''', (str(id)))

        services = cdb.fetchall();

        servicesData = []

        for service in services:
            servicesData.append({
                "id": service[0],
                "title": service[1]
            })

        single_organization = {
            "id":           data[0],
            "title":        data[1],
            "text":         data[3],
            "address":      json.loads(data[4]),
            "phones":       json.loads(data[5]),
            "email":        data[6],
            "link":         data[7],
            "timetable":    data[8],
            "services":     servicesData
        }

        if logo[0] is not None:
           single_organization["logo"] = logo[0]
        if image[0] is not None:
           single_organization["image"]       = image[0]
           single_organization["image_desc"]  = image[1]
           single_organization["image_title"] = image[2]
        if barcode[0] is not None:
           single_organization["barcode"] = barcode[0]

        return single_organization



    def create_new_organization (self, data):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute('''
        INSERT INTO organizations (
            title,
            text,
            address,
            phones,
            email,
            link,
            timetable
        )
        VALUES (?,?,?,?,?,?,?)''', (
            data["title"], 
            data["text"],
            data["address"],
            data["phones"],
            data["email"],
            data["link"],
            data["timetable"])
        )
        db.commit()

        return True


    def update_organization (self, data):

        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute("""
        UPDATE organizations 
        SET 
            title = ?,
            text = ?,
            address = ?, 
            phones = ?, 
            email = ?, 
            link = ?, 
            timetable = ?
        WHERE id = ? """, (
            data["title"], 
            data['text'],
            data["address"], 
            data["phones"], 
            data["email"], 
            data["link"], 
            data["timetable"],
            data["id"]))

        db.commit()

        return self.get_single_organization(data["id"])
            


    def update_organization_logo(self, id, logo):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute("""
        UPDATE organizations 
        SET 
            logo = ?
        WHERE id = ? """, (logo, id))

        db.commit()

    def update_organization_main_image(self, id, image):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute("""
        UPDATE organizations 
        SET 
            image = ?
        WHERE id = ? """, (image, id))

        db.commit()

    def update_organization_barcode(self, id, barcode):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute("""
        UPDATE organizations 
        SET 
            barcode = ?
        WHERE id = ? """, (barcode, id))

        db.commit()


    def delete_organization (self, id):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute('''
            DELETE FROM organizations WHERE id = ?
        ''', (str(id)))

        db.commit()

        return "organizations deleted"