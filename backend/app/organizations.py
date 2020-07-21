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
            image_title TEXT,
            image_desc TEXT,
            type INTEGER DEFAULT 0,
            -- orgs = 0
            -- restaraunts = 1
            -- servs = 2
            -- banks = 3
            -- polygraphies = 4
            -- markets = 5
            -- pharms = 6

            FOREIGN KEY (image)   REFERENCES images (id)
            FOREIGN KEY (logo)    REFERENCES images (id)
            FOREIGN KEY (barcode) REFERENCES images (id)
        )
        ''')
        self.conn.commit()


    def init_data(self):
        # организации
        self.cursor.execute('''
        INSERT INTO organizations (
            title,
            logo,
            text,
            address,
            phones,
            email,
            link,
            timetable,
            type
        )
        VALUES (?,?,?,?,?,?,?,?,?)''', (
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
            "ПН-ЧТ – 09:00 - 17:00 ПТ – 08:00 - 15:45 СБ-ВС – выходной",
            0)
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
            timetable,
            type
        )
        VALUES (?,?,?,?,?,?,?,?,?)''', (
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
            "ПН-ЧТ – 09:00 - 17:00 ПТ – 08:00 - 15:45 СБ-ВС – выходной",
            0)
        )
        self.conn.commit()

        # кафе
        self.cursor.execute('''
        INSERT INTO organizations (
            title,
            logo,
            text,
            address,
            phones,
            email,
            link,
            timetable,
            type
        )
        VALUES (?,?,?,?,?,?,?,?,?)''', (
            "Столовая комбината питания", 
            1,
            "Минимаркет Green - это новая концепция организаций правильного питания. Мы предлагаем баланс между полноценным питанием, разнообразным меню, множеством форматов готовой еды и недостатком времени, предлагая здоровые пищевые привычки, удобство выбора, свежесть и качество.",
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
            "ПН-ЧТ – 09:00 - 17:00 ПТ – 08:00 - 15:45 СБ-ВС – выходной",
            1)
        )
        self.conn.commit()

        # Аптечный пункт
        self.cursor.execute('''
        INSERT INTO organizations (
            title,
            logo,
            text,
            address,
            phones,
            email,
            link,
            timetable,
            type
        )
        VALUES (?,?,?,?,?,?,?,?,?)''', (
            'Аптечный пункт гуп "медицинский центр" управления делами мэра и правительства Москвы', 
            1,
            "Мы позаботились о том, чтобы Вам было удобно. Воспользовавшись услугами нашей апткеи, Вы получите доступ к широкому ассортименту лекраственных стредств, а удобое расположение в здании клиники значительно сэкономит Ваше время и силы.",
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
            "ПН-ЧТ – 09:00 - 17:00 ПТ – 08:00 - 15:45 СБ-ВС – выходной",
            6)
        )
        self.conn.commit()

        # Минимаркет
        self.cursor.execute('''
        INSERT INTO organizations (
            title,
            logo,
            text,
            address,
            phones,
            email,
            link,
            timetable,
            type
        )
        VALUES (?,?,?,?,?,?,?,?,?)''', (
            'Минимаркет GREEN', 
            1,
            "Минимаркет Green - это новая концепция организаций правильного питания. Мы предлагаем баланс между полноценным питанием, разнообразным меню, множеством форматов готовой еды и недостатком времени, предлагая здоровые пищевые привычки, удобство выбора, свежесть и качество.",
            json.dumps([
                "121099, Г. Москва",
                "ул. Новый Арбат, д.36",
                "19 этаж, кабинет 1928"
            ]),
            json.dumps([
                "+7 (495) 633-60-02",
            ]),
            "kow@mos.ru",
            "https://www.mos.ru/kos",
            "ПН-ЧТ – 09:00 - 17:00 ПТ – 08:00 - 15:45 СБ-ВС – выходной",
            5)
        )
        self.conn.commit()

        # Фото и полиграфия
        self.cursor.execute('''
        INSERT INTO organizations (
            title,
            logo,
            text,
            address,
            phones,
            email,
            link,
            timetable,
            type
        )
        VALUES (?,?,?,?,?,?,?,?,?)''', (
            'Студия дизайна и полиграфии', 
            1,
            "Студия дизайна и полиграфии оказывает широкий спектр услуг производства и печати: оперативная печать фото на документы, копирования/канирование, разработка и производство полиграфической продукции, разработка дизайна и фирменного стиля, а также верстка, брошюровка, печать визиток и многое другое",
            json.dumps([
                "121099, Г. Москва",
                "ул. Новый Арбат, д.36",
                "19 этаж, кабинет 1928"
            ]),
            json.dumps([
                "+7 (495) 633-60-02",
            ]),
            "kow@mos.ru",
            "https://www.mos.ru/kos",
            "ПН-ЧТ – 09:00 - 17:00 ПТ – 08:00 - 15:45 СБ-ВС – выходной",
            4)
        )
        self.conn.commit()

        # Сервисы
        self.cursor.execute('''
        INSERT INTO organizations (
            title,
            logo,
            text,
            address,
            phones,
            email,
            link,
            timetable,
            type
        )
        VALUES (?,?,?,?,?,?,?,?,?)''', (
            'Студия дизайна и полиграфии', 
            1,
            "Студия дизайна и полиграфии оказывает широкий спектр услуг производства и печати: оперативная печать фото на документы, копирования/канирование, разработка и производство полиграфической продукции, разработка дизайна и фирменного стиля, а также верстка, брошюровка, печать визиток и многое другое",
            json.dumps([
                "121099, Г. Москва",
                "ул. Новый Арбат, д.36",
                "19 этаж, кабинет 1928"
            ]),
            json.dumps([
                "+7 (495) 633-60-02",
            ]),
            "kow@mos.ru",
            "https://www.mos.ru/kos",
            "ПН-ЧТ – 09:00 - 17:00 ПТ – 08:00 - 15:45 СБ-ВС – выходной",
            2)
        )
        self.conn.commit()


        # Банки
        self.cursor.execute('''
         INSERT INTO organizations (
            title,
            logo,
            text,
            address,
            phones,
            email,
            link,
            timetable,
            type
        )
        VALUES (?,?,?,?,?,?,?,?,?)''', (
            'Студия дизайна и полиграфии', 
            1,
            "Студия дизайна и полиграфии оказывает широкий спектр услуг производства и печати: оперативная печать фото на документы, копирования/канирование, разработка и производство полиграфической продукции, разработка дизайна и фирменного стиля, а также верстка, брошюровка, печать визиток и многое другое",
            json.dumps([
                "121099, Г. Москва",
                "ул. Новый Арбат, д.36",
                "19 этаж, кабинет 1928"
            ]),
            json.dumps([
                "+7 (495) 633-60-02",
            ]),
            "kow@mos.ru",
            "https://www.mos.ru/kos",
            "ПН-ЧТ – 09:00 - 17:00 ПТ – 08:00 - 15:45 СБ-ВС – выходной",
            3)
        )
        self.conn.commit()


        #  # Банки
        # self.cursor.execute('''
        # INSERT INTO organizations (
        #     title,
        #     logo,
        #     text,
        #     address,
        #     timetable,
        #     type
        # )
        # VALUES (?,?,?,?,?,?)''', (
        #     'АЛЬФА-БАНК', 
        #     1,
        #     "Прием и выдача наличных, оплата квитанций",
        #     "1,5,12,19 Этажи",
        #     "Круглосуточно",
        #     3)
        # )
        # self.conn.commit()

    def letter_index_in_data(self, data, letter):
        for i in range(len(data)):
            if data[i]["variable"] == letter:
                return i
        return -1


    def get_organization_titles (self):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute('''
            SELECT id, title FROM organizations WHERE type = '0'
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


    def get_all_organizations (self, type=0): 

        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute('''
            SELECT id, title, text FROM organizations
            WHERE type = ?
        ''', (type,))

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
            "img_title":    data[11] if data[11] is not None else "",
            "img_desc":     data[12] if data[12] is not None else "",
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


    def get_single_organization_by_type (self, type=0):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        # ////////// Основной контент //////////
        cdb.execute('''
            SELECT *
            FROM organizations
            WHERE organizations.type = ?
        ''', (str(type)))


        data = cdb.fetchone();


        # ////////// фотографии //////////
        cdb.execute('''
            SELECT src
            FROM organizations
            LEFT JOIN images
            ON organizations.logo = images.id
            WHERE organizations.type = ?
        ''', (str(type)))
        logo = cdb.fetchone();

        cdb.execute('''
            SELECT src, desc, images.title as title
            FROM organizations
            LEFT JOIN images
            ON organizations.image = images.id
            WHERE organizations.type = ?
        ''', (str(type)))
        image = cdb.fetchone();

        cdb.execute('''
            SELECT src
            FROM organizations
            LEFT JOIN images
            ON organizations.barcode = images.id
            WHERE organizations.type = ?
        ''', (str(type)))
        barcode = cdb.fetchone();


        # ////////// Сервисы //////////
        cdb.execute('''
            SELECT id, title, image     
            FROM services
            WHERE organization_id = ?
        ''', (str(data[0])))

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
            "img_title":    data[11] if data[11] is not None else "",
            "img_desc":     data[12] if data[12] is not None else "",
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

        page_type = data["page_type"]

        cdb.execute('''
        INSERT INTO organizations (
            title,
            text,
            address,
            phones,
            email,
            link,
            timetable,
            type
        )
        VALUES (?,?,?,?,?,?,?,?)''', (
            data["title"], 
            data["text"],
            data["address"],
            data["phones"],
            data["email"],
            data["link"],
            data["timetable"],
            page_type)
        )
        cdb.execute('''SELECT last_insert_rowid()''')
        id = cdb.fetchall()[0][0]
        db.commit()

        return id


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
            timetable = ?,
            image_desc = ?,
            image_title = ?
        WHERE id = ? """, (
            data["title"], 
            data['text'],
            data["address"], 
            data["phones"], 
            data["email"], 
            data["link"], 
            data["timetable"],
            data["img_desc"], 
            data["img_title"],
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
        cdb.execute("""SELECT src FROM images WHERE id = ?""", (id,))
        src = cdb.fetchall()[0][0]
        db.commit()
        return src

    def update_organization_main_image(self, id, image):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute("""
        UPDATE organizations 
        SET 
            image = ?
        WHERE id = ? """, (image, id))
        cdb.execute("""SELECT src FROM images WHERE id = ?""", (id,))
        src = cdb.fetchall()[0][0]
        db.commit()
        return src

    def update_organization_barcode(self, id, barcode):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute("""
        UPDATE organizations 
        SET 
            barcode = ?
        WHERE id = ? """, (barcode, id))
        cdb.execute("""SELECT src FROM images WHERE id = ?""", (id,))
        src = cdb.fetchall()[0][0]
        db.commit()
        return src


    def delete_organization (self, id):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute('''
            DELETE FROM organizations WHERE id = ?
        ''', (str(id)))

        db.commit()

        return "organizations deleted"