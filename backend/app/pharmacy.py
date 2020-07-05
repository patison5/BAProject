import json
import os
import config
import string
from contextlib import closing
import pymysql
from pymysql.cursors import DictCursor

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


    def get_pharmacy_info (self):
        return self.data_set


    def update_pharmacy_info (self, data):
        # в data придет информация которую нужно обновить. минимум 1 какое-то поле, максимум все поля
        return True