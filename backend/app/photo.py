import json
import os
import config
import string
from contextlib import closing
import pymysql
from pymysql.cursors import DictCursor

class PhotoController:
    
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
        print("OrganizationsController created")


    def get_photo_info (self):
        return self.data_set


    def update_photo_info (self, data):
        # в data придет информация которую нужно обновить. минимум 1 какое-то поле, максимум все поля
        return True