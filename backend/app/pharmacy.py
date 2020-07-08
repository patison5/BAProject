import json
import os
import config
import string

import sqlite3

database = "mydatabase.db"
 
conn = sqlite3.connect(database, timeout=10)
# conn = sqlite3.connect("mydatabase.db")

cursor = conn.cursor()
 
# # Создание таблицы
# cursor.execute("""CREATE TABLE pharmacy(
#                     p_id int
#                     p_title text, 
#                     p_logo text, 
#                     p_text text,
#                     p_address text, 
#                     p_phones text,
#                     p_phones text,
#                     p_email text,
#                     p_link text,
#                     p_barcode text,
#                     p_timetable text,
#                     p_images text,
#                 )""")


class PharmacyController:
    
    # Вся информация организаций
    data_set = {
        "title": 'Аптечный пункт гуп "медицинский центр" управления делами мэра и правительства Москвы', 
        "logo": "http://127.0.0.1:5000/static/images/icons/img-10.svg",
        "text": "Мы позаботились о том, чтобы Вам было удобно. Воспользовавшись услугами нашей апткеи, Вы получите доступ к широкому ассортименту лекраственных стредств, а удобое расположение в здании клиники значительно сэкономит Ваше время и силы.", 
        "address": [
            "121099, Г. Москва",
            "ул. Новый Арбат, д.36",
            "19 этаж, кабинет 1928"
        ], 
        "phones": [
            "+7 (495) 633-60-02"
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
        print("PharmacyController created")

        conn = sqlite3.connect(database, timeout=10)
        cursor = conn.cursor()

        # Создание таблицы
        cursor.execute(""" DROP TABLE IF EXISTS pharmacy""")
        conn.commit()

        cursor.execute('''CREATE TABLE IF NOT EXISTS pharmacy (
                            p_id INTEGER PRIMARY KEY,
                            p_title text NOT NULL,
                            p_logo text,
                            p_address text, 
                            p_phones text,
                            p_email text,
                            p_link text,
                            p_barcode text,
                            p_timetable text,
                            p_images text
                        )''')
        conn.commit()

        cursor.execute('''INSERT INTO pharmacy (
                             p_title, 
                             p_logo, 
                             p_address, 
                             p_phones, 
                             p_email, 
                             p_link, 
                             p_barcode, 
                             p_timetable)
                          VALUES (?,?,?,?,?,?,?,?)''', (
                             self.data_set["title"], 
                             self.data_set["logo"], 
                             json.dumps(self.data_set["address"]), 
                             json.dumps(self.data_set["phones"]), 
                             self.data_set["email"], 
                             self.data_set["link"], 
                             self.data_set["barcode"], 
                             self.data_set["timetable"]))

        conn.commit()
        cursor.close()
        conn.close()

    def get_pharmacy_info (self):
        sql = "SELECT * FROM pharmacy"

        conn = sqlite3.connect("mydatabase.db", timeout=10) # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()
        cursor.execute(sql)

        print(cursor.fetchone())
        return cursor.fetchone()


    def update_pharmacy_info (self, data):
        # в data придет информация которую нужно обновить. минимум 1 какое-то поле, максимум все поля

        link        = data['link']
        timetable   = data['timetable']
        title       = data['title']
        address     = data['address']
        # print(data)

        return True










# print(cursor.fetchone()) # or use fetchone()


 # data_person_name = [('Michael', 'Fox'),
        #             ('Adam', 'Miller'),
        #             ('Andrew', 'Peck'),
        #             ('James', 'Shroyer'),
        #             ('Eric', 'Burger')]

        # cursor.executemany('INSERT INTO pharmacy (p_id, p_title) VALUES (?,?)', data_person_name)
# for row in c.execute('SELECT * FROM pharmacy '):
#     print(row)



# 1111111111
        # data = []
        # data.append((
        #     self.data_set["title"], 
        #     self.data_set["logo"], 
        #     json.dumps(self.data_set["address"]), 
        #     json.dumps(self.data_set["phones"]), 
        #     self.data_set["email"], 
        #     self.data_set["link"], 
        #     self.data_set["barcode"], 
        #     self.data_set["timetable"]
        # ))

        # cursor.executemany('''INSERT INTO pharmacy 
        #                     (p_title, 
        #                      p_logo, 
        #                      p_address, 
        #                      p_phones, 
        #                      p_email, 
        #                      p_link, 
        #                      p_barcode, 
        #                      p_timetable) 
        #                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', data)