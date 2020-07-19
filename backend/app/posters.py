import json
import os
import config
import string
from contextlib import closing
import pymysql
from pymysql.cursors import DictCursor
import sqlite3

database = "mydatabase.db"

class PostersController:
    
    # Вся информация организаций
    data_set = [
        {
            "title": "Комитет общественных связей и молодежной политики города Москвы", 
            "logo": "http://127.0.0.1:5000/static/images/woman.png",
            "text": "kv ipsum dolor sit amet, consectetur adipisicing elit. Maxime iure adipisci fuga tenetur repudiandae explicabo ad voluptas unde distinctio? Sint laudantium quae minus nesciunt repellendus doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.", 
            "date": "22.02.12",
            "time": "13:00",
            "address": "Большой концертный зал",
            "img": "http://127.0.0.1:5000/static/images/afisha.png"
        }
    ]

    

    def __init__ (self):
        self.conn = sqlite3.connect(database, timeout=10)
        self.cursor = self.conn.cursor()
        print("PostersController created")

    def drop_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS posters""")
        self.conn.commit()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE posters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            address TEXT,
            date TEXT,
            time TEXT,
            text TEXT,
            image INTEGER DEFAULT NULL,
            logo INTEGER DEFAULT NULL,
            FOREIGN KEY (image) REFERENCES images (id),
            FOREIGN KEY (logo) REFERENCES images (id)
        )
        ''')
        self.conn.commit()


    def get_all_afisha (self):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute('''
            SELECT *
            FROM posters
            LEFT JOIN images
            ON posters.image = images.id
        ''')


        afisha = cdb.fetchall();

        afishaData = []

        for element in afisha:
            print(element)
            afishaData.append({
                "id":       element[0],
                "title":    element[1],
                "text":     element[5], 
                "date":     element[3],
                "time":     element[4],
                "address":  element[2],
                "img":      element[8],
            })

        return afishaData

    def get_single_afisha (self, id):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute('''
            SELECT *
            FROM posters
            LEFT JOIN images
            ON posters.image = images.id
            WHERE posters.id = ?
        ''', (str(id)))


        afisha = cdb.fetchone();

        cdb.execute('''
            SELECT src
            FROM posters
            LEFT JOIN images
            ON posters.logo = images.id
            WHERE posters.id = ?
        ''', (str(id)))


        logo = cdb.fetchone();

        single_afisha = {
            "id":       afisha[0],
            "title":    afisha[1],
            "text":     afisha[5], 
            "date":     afisha[3],
            "time":     afisha[4],
            "address":  afisha[2],
            "img":      afisha[9],
        }

        print(logo)

        if logo[0] is not None:
           single_afisha["logo"] = logo[0]

        print("AFISHA IMAGE " + str(afisha[6]))

        return single_afisha

    def create_new_poster (self, data):
        print(data)

        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        sql = ''' INSERT INTO posters(title, text, date, time, address)
                  VALUES(?,?,?,?,?) '''

        cdb.execute(sql, (
            data["title"], 
            data['text'],
            data["date"], 
            data["timetable"], 
            data["address"]
        ))
        db.commit()

        return json.dumps({"status": "ok"})



    def update_afisha (self, data):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute("""
        UPDATE posters 
        SET 
            title = ?,
            text = ?,
            date = ?,
            time = ?,
            address = ?
        WHERE id = ? """, (
            data["title"], 
            data['text'],
            data["date"], 
            data["timetable"], 
            data["address"],
            data["id"]
        ))

        db.commit()
        cdb.close()
        db.close()
        

        return json.dumps({"status": "ok"})


    def update_poster_logo (self, poster_id, image_id):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute("""
        UPDATE posters 
        SET 
            logo = ?
        WHERE id = ? """, (
            image_id,
            poster_id
        ))

        db.commit()
        cdb.close()
        db.close()

        return json.dumps({
            "poster_id" : poster_id,
            "image_id" : image_id
        })


    def update_poster_main_image (self, poster_id, image_id):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute("""
        UPDATE posters 
        SET 
            image = ?
        WHERE id = ? """, (
            image_id,
            poster_id
        ))

        db.commit()
        cdb.close()
        db.close()

        return json.dumps({
            "poster_id" : poster_id,
            "image_id" : image_id
        })


    def delete_poster (self, id):

        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        cdb.execute('''
            DELETE FROM posters WHERE id = ?
        ''', (str(id)))

        db.commit()

        return "afisha deleted"



    def init_data(self):
        db = sqlite3.connect(database, timeout=10)
        cdb = db.cursor()

        sql = ''' INSERT INTO posters(title, text, address, date, time, image)
              VALUES(?,?,?,?,?,?) '''


        cdb.execute(sql, (
            "Комитет общественных связей и молодежной политики города Москвы", 
            "kv ipsum dolor sit amet, consectetur adipisicing elit. Maxime iure adipisci fuga tenetur repudiandae explicabo ad voluptas unde distinctio? Sint laudantium quae minus nesciunt repellendus doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.", 
            "Большой концертный зал",
            "22.02.12",
            "13:00",
            "1"
        ))
        db.commit()

        cdb.execute(sql, (
            "Комитет общественных связей и молодежной политики города Москвы", 
            "kv ipsum dolor sit amet, consectetur adipisicing elit. Maxime iure adipisci fuga tenetur repudiandae explicabo ad voluptas unde distinctio? Sint laudantium quae minus nesciunt repellendus doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.", 
            "Большой концертный зал",
            "22.02.12",
            "13:00",
            "1"
        ))
        db.commit()