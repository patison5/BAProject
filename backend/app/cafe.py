import json
import os
import config
import string
from contextlib import closing
import pymysql
from pymysql.cursors import DictCursor

class CafeController:
    
    # Вся информация организаций
    data_set = {
        "title": 'Столовая комбината питания', 
        "logo": "http://127.0.0.1:5000/static/images/icons/img-10.svg",
        "text": "Минимаркет Green - это новая концепция организаций правильного питания. Мы предлагаем баланс между полноценным питанием, разнообразным меню, множеством форматов готовой еды и недостатком времени, предлагая здоровые пищевые привычки, удобство выбора, свежесть и качество.", 
        "right_part": {
            "image": "http://127.0.0.1:5000/static/images/woman.png",
            "title": "Драгунова Екатерина Вячеслаовна",
            "desc": "Председатель коммитета общественных сязей и молодежной политики города Москвы,"
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

    

    def __init__ (self):
        print("OrganizationsController created")


    def get_cafe_info (self):
        return self.data_set


    def update_cafe_info (self, data):
        # в data придет информация которую нужно обновить. минимум 1 какое-то поле, максимум все поля
        return True