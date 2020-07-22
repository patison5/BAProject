import json
import os
import config
import string
from contextlib import closing
import pymysql
from pymysql.cursors import DictCursor
import sqlite3

database = "mydatabase.db"

class TravelsController:
    
    def __init__ (self):
        self.conn = sqlite3.connect(database, timeout=10)
        self.cursor = self.conn.cursor()
        print("OrganizationsController created")

    def drop_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS travels""")
        self.cursor.execute("""DROP TABLE IF EXISTS trv_rubrics""")
        self.conn.commit()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE trv_rubrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            address TEXT NOT NULL,
            timetable TEXT NOT NULL,
            desc TEXT NOT NULL,
            image INTEGER,
            FOREIGN KEY (image) REFERENCES images (id)
        )
        ''')
        self.cursor.execute('''
        CREATE TABLE travels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rub_id INTEGER NOT NULL DEFAULT 0,
            title TEXT DEFAULT NULL,
            image INTEGER,
            sec_title TEXT,
            txt_a TEXT,
            txt_b TEXT,
            FOREIGN KEY (rub_id) REFERENCES trv_rubrics (id),
            FOREIGN KEY (image) REFERENCES images (id)
        )
        ''')
        self.conn.commit()


    def create_new_rubric(self, data):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute('''
        INSERT INTO trv_rubrics (
            title,
            address,
            timetable,
            desc
        )
        VALUES (?)''', (
                data["title"],
                data["address"],
                data["timetable"],
                data["desc"]
            )
        )
        cdb.execute('''SELECT last_insert_rowid()''')
        id = cdb.fetchall()[0][0]
        db.commit()

        return id


    def delete_rubric(self, id):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute('''DELETE FROM travels WHERE rub_id = ?''', (str(id)))
        cdb.execute('''DELETE FROM trv_rubrics WHERE id = ?''', (str(id)))

        db.commit()


    def update_rubric(self, data):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute("""
        UPDATE trv_rubric 
        SET 
            title = ?,
            address = ?,
            timetable = ?,
            desc = ?
        WHERE id = ?""", (
            data["title"],
            data["address"],
            data["timetable"],
            data["desc"],
            data["id"]))

        db.commit()

        return self.get_single_rubric(data["id"])


    def update_rubric_image(self, id, image):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute("""
        UPDATE trv_rubrics
        SET 
            image = ?
        WHERE id = ? """, (image, id))
        cdb.execute("""SELECT src FROM images WHERE id = ?""", (image,))
        src = cdb.fetchall()[0][0]
        db.commit()
        return src


    def get_all_rubrics(self):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()
        cdb.execute('''
            SELECT trv_rubrics.id, trv_rubrics.title, images.src FROM trv_rubrics
            INNER JOIN images ON trv_rubrics.image = images.id
        ''')
        data = cdb.fetchall();
        json = []

        for item in data:
            json.append({
                "id":           item[0],
                "title":        item[1],
                "image_src":    item[2]
            })

        return json

    def get_all_travels_by_rubric(self, rub_id):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()
        cdb.execute('''
            SELECT id, title, data, images.src FROM travels
            INNER JOIN images ON travels.image = images.id
            WHERE rub_id = ?
            ORDER BY id ASC
        ''', (rub_id,))
        data = cdb.fetchall();
        json = []
        ids = []

        for item in data:
            json.append({
                "id":              item[0],
                "title":           item[1],
                "timetable":       item[2],
                "desc":            item[3],
                "image_src":       item[4],
                "additional_data": item[5],
                "images_src":      []
            })
            ids.append(item[0])


        cdb.execute('''
            SELECT images.src, travel_id FROM trv_images
            INNER JOIN images ON trv_images.image_id = images.id
            WHERE travel_id IN (?)
            ORDER BY travel_id ASC
        ''', (str(ids).strip('[]'),))
        data = cdb.fetchall();
        for i in data:
            if i[1] in ids:
                index = ids.index(i[1])
                json[index]['images_src'].append(i[0])

        return json


    def get_single_rubric(self, id):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute('''
            SELECT *
            FROM trv_rubrics
            WHERE trv_rubrics.id = ?
        ''', (str(id)))


        afisha = cdb.fetchone();

        cdb.execute('''
            SELECT src
            FROM trv_rubrics
            LEFT JOIN images
            ON trv_rubrics.image = images.id
            WHERE trv_rubrics.id = ?
        ''', (str(id)))


        logo = cdb.fetchone();
        
        single_rubric = {
            "id":       afisha[0],
            "title":     afisha[1], 
        }


        if logo[0] is not None:
           single_rubric["image"] = logo[0]

        return single_rubric


    def create_new_travel(self, data):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute('''
        INSERT INTO travels (
            rub_id,
            title,
            sec_title,
            txt_a,
            txt_b
        )
        VALUES (?,?)''', (
                data["rub_id"],
                data["title"],
                data["sec_title"],
                data["txt_a"],
                data["txt_b"]
            )
        )
        cdb.execute('''SELECT last_insert_rowid()''')
        id = cdb.fetchall()[0][0]
        db.commit()

        return id


    def update_travel(self, data):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute("""
        UPDATE travels 
        SET 
            rub_id = ?,
            title = ?,
            sec_title = ?,
            txt_a = ?,
            txt_b = ?
        WHERE id = ?""", (
            data["rub_id"],
            data["title"],
            data["sec_title"],
            data["txt_a"],
            data["txt_b"]
            data["id"]
        ))
        db.commit()

        return self.get_travel(data["id"])

    def update_travel_image(self, id, image):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute("""
        UPDATE travels
        SET 
            image = ?
        WHERE id = ? """, (image, id))
        cdb.execute("""SELECT src FROM images WHERE id = ?""", (image,))
        src = cdb.fetchall()[0][0]
        db.commit()
        return src

    def get_travel(self, id):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()
        cdb.execute('''
            SELECT id, title, images.src, sec_title, txt_a, txt_b FROM travels
            INNER JOIN images ON travels.image = images.id
            WHERE id = ?
        ''', (id,))
        data = cdb.fetchall();
        json = []

        for item in data:
            json.append({
                "id":              item[0],
                "title":           item[1],
                "image_src":       item[2],
                "sec_title":       item[3],
                "txt_a":           item[4],
                "txt_b":           item[5]
            })

        cdb.execute('''
            SELECT images.src FROM trv_images
            INNER JOIN images ON trv_images.image_id = images.id
            WHERE travel_id = ?
        ''', (id,))
        pics = cdb.fetchall();

        return (json, pics)

    def get_travel_images(self, id):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()
        cdb.execute("""SELECT images.src, trv_images.image_id
            FROM trv_images
            LEFT JOIN images ON images.id = trv_images.image_id
            WHERE travel_id = ?""", (id,))
        data = cdb.fetchall()
        imgs = []
        for item in data:
            imgs.append({
                "src" : item[0],
                "id"  : item[1]
                })
        return imgs


    def get_organization_titles (self):
        # arr = []
        # for item in self.data_set:
        #     if item[0] not in arr:
        #         arr[item[0]] = {}
            # arr["item[0]"].title = item['title']

        return self.organizations_titles


    def get_all_organizations (self): 
        return self.data_set


    def create_new_organization (self, data):
        # в data придет вся необходимая информация для добавления новой организации
        return True


    def update_organization (self, data):
        # в data придет информация которую нужно обновить. минимум 1 какое-то поле, максимум все поля
        return True


    def delete_organization (self, id):
        # удаляет организацию по id
        return True