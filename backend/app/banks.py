import json
import os
import config
import string
from contextlib import closing
import pymysql
from pymysql.cursors import DictCursor

class BanksController:
    
    # Вся информация организаций
    data_set = [
        {
            "title": "Сбербанк",
            "time": "Круглосуточно",
            "stage": "1,5,12,19 Этажи",
            "text": "Прием и выдача наличных, оплата квитанций",
            "img": "http://127.0.0.1:5000/static/images/icons/cafe-1.svg"
        },
        {
            "title": "ВТБ",
            "time": "Круглосуточно",
            "stage": "1,5,12,19 Этажи",
            "text": "Прием и выдача наличных, оплата квитанций",
            "img": "http://127.0.0.1:5000/static/images/icons/cafe-1.svg"
        },
        {
            "title": "АЛЬФА-БАНК",
            "time": "Круглосуточно",
            "stage": "1,5,12,19 Этажи",
            "text": "Прием и выдача наличных, оплата квитанций",
            "img": "http://127.0.0.1:5000/static/images/icons/cafe-1.svg"
        },
        {
            "title": "БАНК-Восточный экспресс",
            "time": "Круглосуточно",
            "stage": "1,5,12,19 Этажи",
            "text": "Прием и выдача наличных, оплата квитанций",
            "img": "http://127.0.0.1:5000/static/images/icons/cafe-1.svg"
        },
    ]

    def __init__ (self):
        print("OrganizationsController created")


    def get_banks (self):
        return self.data_set

    def get_banks_by_id (self, id):
        return self.data_set[id]

    def update_banks_info (self, data):
        # в data придет информация которую нужно обновить. минимум 1 какое-то поле, максимум все поля
        return True