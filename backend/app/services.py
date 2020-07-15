import json
import os
import config
import string
from contextlib import closing
import pymysql
from pymysql.cursors import DictCursor
import sqlite3

database = "mydatabase.db"

class ServicesController:
    
    # Вся информация организаций
    data_set = [
        {
            "title": 'Ремонт обуви', 
            "logo": "http://127.0.0.1:5000/static/images/icons/img-10.svg",
            "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quae eaque, totam dolorem ratione, quibusdam, blanditiis possimus ab cumque libero, vero ea officiis a! Dolor nesciunt quia exercitationem, quaerat ratione quidem beatae ad accusamus nobis. Obcaecati ab consequuntur voluptates aliquam officiis facere nemo deserunt accusantium, expedita. Illo ducimus fugiat veniam, perferendis porro, repellat velit neque odit quis illum assumenda. Reprehenderit labore sunt tempora suscipit quaerat, sint, asperiores distinctio repellendus optio atque sequi corrupti voluptatum autem quis laboriosam et laudantium accusamus. Nesciunt pariatur at iusto. Provident, dolores placeat iusto in illo dolorem minima sit voluptates iure aut, est culpa, ut. Alias iure distinctio neque deleniti minus dignissimos ab perferendis facere accusantium sunt. Saepe aperiam, facere illum. Nostrum vel, dicta perspiciatis. Tempora illo accusamus odit accusantium, rerum eum sed non necessitatibus incidunt enim officia id similique voluptate error, quas. Quisquam error enim pariatur sapiente deleniti, nobis consectetur optio, totam amet, nam aut maxime libero ea blanditiis temporibus. Sed recusandae atque architecto enim odio beatae aliquam quisquam provident consequuntur soluta quos fugiat vero eos repudiandae, esse incidunt in voluptates optio, nam itaque nihil nulla at, est! Aliquam perspiciatis saepe id atque. Culpa, architecto, deserunt! Molestiae asperiores et, ullam, adipisci commodi itaque quaerat eum culpa.", 
            "right_part": {
                "image": "http://127.0.0.1:5000/static/images/woman.png"
            },
            "address": [
                "121099, Г. Москва",
                "ул. Новый Арбат, д.36"
            ], 
            "phones": [
                "+7 (495) 633-60-02"
            ],
            "email": "kow@mos.ru",
            "link": "https://www.mos.ru/kos",
            "images": ""
        },
        {
            "title": 'Ремонт обуви', 
            "logo": "http://127.0.0.1:5000/static/images/icons/img-10.svg",
            "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quae eaque, totam dolorem ratione, quibusdam, blanditiis possimus ab cumque libero, vero ea officiis a! Dolor nesciunt quia exercitationem, quaerat ratione quidem beatae ad accusamus nobis. Obcaecati ab consequuntur voluptates aliquam officiis facere nemo deserunt accusantium, expedita. Illo ducimus fugiat veniam, perferendis porro, repellat velit neque odit quis illum assumenda. Reprehenderit labore sunt tempora suscipit quaerat, sint, asperiores distinctio repellendus optio atque sequi corrupti voluptatum autem quis laboriosam et laudantium accusamus. Nesciunt pariatur at iusto. Provident, dolores placeat iusto in illo dolorem minima sit voluptates iure aut, est culpa, ut. Alias iure distinctio neque deleniti minus dignissimos ab perferendis facere accusantium sunt. Saepe aperiam, facere illum. Nostrum vel, dicta perspiciatis. Tempora illo accusamus odit accusantium, rerum eum sed non necessitatibus incidunt enim officia id similique voluptate error, quas. Quisquam error enim pariatur sapiente deleniti, nobis consectetur optio, totam amet, nam aut maxime libero ea blanditiis temporibus. Sed recusandae atque architecto enim odio beatae aliquam quisquam provident consequuntur soluta quos fugiat vero eos repudiandae, esse incidunt in voluptates optio, nam itaque nihil nulla at, est! Aliquam perspiciatis saepe id atque. Culpa, architecto, deserunt! Molestiae asperiores et, ullam, adipisci commodi itaque quaerat eum culpa.", 
            "right_part": {
                "image": "http://127.0.0.1:5000/static/images/woman.png"
            },
            "address": [
                "121099, Г. Москва",
                "ул. Новый Арбат, д.36"
            ], 
            "phones": [
                "+7 (495) 633-60-02"
            ],
            "email": "kow@mos.ru",
            "link": "https://www.mos.ru/kos",
            "images": ""
        }
    ]

    def __init__ (self):
        self.conn = sqlite3.connect(database, timeout=10)
        self.cursor = self.conn.cursor()
        print("ServicesController created")

    def drop_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS services""")
        self.conn.commit()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            organization_id INTEGER NOT NULL,
            title TEXT,
            image INTEGER,
            text TEXT,
            address TEXT,
            phones TEXT,
            email TEXT,
            link TEXT,
            barcode TEXT,
            timetable TEXT,
            FOREIGN KEY (organization_id) REFERENCES organizations (id),
            FOREIGN KEY (image) REFERENCES images (id)
        )
        ''')
        self.conn.commit()

    def get_titles_of_services (self):
        arr = []
        for item in self.data_set:
            arr.append(item['title'])

        return arr

    def update_services_info (self, data):
        # print(data)

        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute("""
        UPDATE services 
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

        return json.dumps({"status": "ok"})



    def init_data(self):
        self.cursor.execute('''
        INSERT INTO services (
            organization_id,
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
        VALUES (?,?,?,?,?,?,?,?,?,?)''', (
            1,
            "Это какой-то 1 тестовый сервис у организации, хранящийся в бд", 
            1,
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
        INSERT INTO services (
            organization_id,
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
        VALUES (?,?,?,?,?,?,?,?,?,?)''', (
            1,
            "Это какой-то 2 тестовый сервис у организации, хранящийся в бд", 
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
            "barcode",
            "ПН-ЧТ – 09:00 - 17:00 ПТ – 08:00 - 15:45 СБ-ВС – выходной")
        )
        self.conn.commit()




    def create_service(self, data):

        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute('''
        INSERT INTO services (
            organization_id,
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
        VALUES (?,?,?,?,?,?,?,?,?,?)''', (
            data["id"],
            data["title"], 
            1, # надо сделать инсерт этого в таблицу images (можно с пустым desc, но с определенным id, например 1) и после этого уже сюда написать этот id
            data["text"],
            data["address"],
            data["phones"],
            data["email"],
            data["link"],
            "barcode",
            data["timetable"]
        ))

        db.commit()

        return json.dumps({"status": "ok"})



    def get_single_service(self, id):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute('''
            SELECT *
            FROM services
            INNER JOIN images
            ON services.image = images.id
            WHERE services.id = ?
        ''', (str(id)))

        data = cdb.fetchone();

        return {
            "id":           data[0],
            "title":        data[2],
            "text":         data[4],
            "address":      json.loads(data[5]),
            "phones":       json.loads(data[6]),
            "email":        data[7],
            "link":         data[8],
            "barcode":      data[9],
            "timetable":    data[10],
            "logo":         data[12],
        }