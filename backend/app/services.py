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
            title TEXT NOT NULL,
            image INTEGER NOT NULL,
            address TEXT NOT NULL,
            phones TEXT NOT NULL,
            email TEXT NOT NULL,
            link TEXT NOT NULL,
            barcode TEXT NOT NULL,
            timetable TEXT NOT NULL,
            FOREIGN KEY (organization_id) REFERENCES organizations (id),
            FOREIGN KEY (image) REFERENCES images (id)
        )
        ''')
        self.conn.commit()


    def get_single_service (self, id):
        return self.data_set[id]

    def get_titles_of_services (self):
        arr = []
        for item in self.data_set:
            arr.append(item['title'])

        return arr

    def update_services_info (self, data):
        # в data придет информация которую нужно обновить. минимум 1 какое-то поле, максимум все поля
        return True