import json
import os
import config
import string
from contextlib import closing
import pymysql
from pymysql.cursors import DictCursor
import sqlite3

database = "mydatabase.db"

class MiscController:
    
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
        self.cursor.execute("""DROP TABLE IF EXISTS misc""")
        self.conn.commit()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE misc (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            endpoint TEXT NOT NULL,
            data TEXT NOT NULL
        )
        ''')
        self.conn.commit()


    def get_image_info (self):
        return self.data_set


    def update_image_info (self, data):
        # в data придет информация которую нужно обновить. минимум 1 какое-то поле, максимум все поля
        return True




    def init_data(self):

        sql = ''' INSERT INTO misc(endpoint, data)
              VALUES(?,?) '''

        self.cursor.execute(sql, ("pharmacy", json.dumps({
            "title": 'Аптечный пункт гуп "медицинский центр" управления делами мэра и правительства Москвы', 
            "logo": "http://127.0.0.1:5000/static/images/icons/img-10.svg",
            "text": "Мы позаботились о том, чтобы Вам было удобно. Воспользовавшись услугами нашей апткеи, Вы получите доступ к широкому ассортименту лекраственных стредств, а удобое расположение в здании клиники значительно сэкономит Ваше время и силы.", 
            "address": json.dumps([
                "121099, Г. Москва",
                "ул. Новый Арбат, д.36"
            ]), 
            "phones": json.dumps([
                "+7 (495) 633-60-02",
                 "ул. Новый Арбат, д.36"
            ]),
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
        })))

        self.conn.commit()


        self.cursor.execute(sql, ("photo", json.dumps({
            "title": "Студия дизайна и полиграфии", 
            "logo": "http://127.0.0.1:5000/static/images/icons/img-10.svg",
            "text": "Студия дизайна и полиграфии оказывает широкий спектр услуг производства и печати: оперативная печать фото на документы, копирования/канирование, разработка и производство полиграфической продукции, разработка дизайна и фирменного стиля, а также верстка, брошюровка, печать визиток и многое другое", 
            "address": json.dumps([
                "121099, Г. Москва",
                "ул. Новый Арбат, д.36"
            ]), 
            "phones": json.dumps([
                "+7 (495) 633-60-02",
                 "ул. Новый Арбат, д.36"
            ]),
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
        })))

        self.conn.commit()


        self.cursor.execute(sql, ("minimarket", json.dumps({
            "title": 'Минимаркет GREEN', 
            "logo": "http://127.0.0.1:5000/static/images/icons/img-10.svg",
            "text": "Минимаркет Green - это новая концепция организаций правильного питания. Мы предлагаем баланс между полноценным питанием, разнообразным меню, множеством форматов готовой еды и недостатком времени, предлагая здоровые пищевые привычки, удобство выбора, свежесть и качество.", 
            "address": json.dumps([
                "121099, Г. Москва",
                "ул. Новый Арбат, д.36"
            ]), 
            "phones": json.dumps([
                "+7 (495) 633-60-02",
                 "ул. Новый Арбат, д.36"
            ]),
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
        })))

        self.conn.commit()

        self.cursor.execute(sql, ("cafe", json.dumps({
            "title": 'Столовая комбината питания', 
            "logo": "http://127.0.0.1:5000/static/images/icons/img-10.svg",
            "text": "Минимаркет Green - это новая концепция организаций правильного питания. Мы предлагаем баланс между полноценным питанием, разнообразным меню, множеством форматов готовой еды и недостатком времени, предлагая здоровые пищевые привычки, удобство выбора, свежесть и качество.", 
            "right_part": {
                "image": "http://127.0.0.1:5000/static/images/woman.png",
                "title": "Драгунова Екатерина Вячеслаовна",
                "desc": "Председатель коммитета общественных сязей и молодежной политики города Москвы,"
            },
            "timetable": "ПН-ЧТ – 08:00 - 17:00 ПТ – 08:00 - 15:45 СБ-ВС – выходной",
            "address": json.dumps([
                "121099, Г. Москва",
                "ул. Новый Арбат, д.36"
            ]), 
            "phones": json.dumps([
                "+7 (495) 633-60-02",
                 "ул. Новый Арбат, д.36"
            ]),
            "email": "kow@mos.ru",
            "link": "https://www.mos.ru/kos",
            "images": ""
        })))

        self.conn.commit()




    def get_misc_info (self, endpoint):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute('''
            SELECT data FROM misc WHERE endpoint = ?
        ''', (endpoint,))
       
        data = cdb.fetchone()[0]
        data = json.loads(data)
        data["address"] = json.loads(data["address"])
        data["phones"]  = json.loads(data["phones"])


        return data



    def update_misc_info (self, endpoint, data):

        print("WATAFUCK IS GOING ON!")


        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute('''
            SELECT data FROM misc WHERE endpoint = ?
        ''', (endpoint,))
       
        sqlData = json.loads(cdb.fetchone()[0])

        print(sqlData["address"])
        print(data["address"])

        sqlData["title"]        = data["title"]
        sqlData["text"]         = data["text"]
        sqlData["timetable"]    = data["timetable"]
        sqlData["address"]      = data["address"]
        sqlData["phones"]       = data["phones"]
        sqlData["email"]        = data["email"]
        sqlData["link"]         = data["link"]


        sql = '''
            UPDATE misc 
            SET data = ?
            WHERE endpoint = ?
        '''

        cdb.execute(sql, (json.dumps(sqlData), endpoint))
        db.commit()


        return json.dumps({"status": "ok"})