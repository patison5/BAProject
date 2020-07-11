import json
import os
import config
import string
from contextlib import closing
import pymysql
from pymysql.cursors import DictCursor

class TourAgentController:
    
    # Вся информация организаций
    data_set = [
        {
            "id": '0',
            "title": "Комитет общественных связей и молодежной политики города Москвы", 
            "text": "doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.", 
            "note": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reprehenderit, enim.",
            "img": "static/images/woman.png",
            "logo_single": "http://127.0.0.1:5000/static/images/icons/img-10.svg",
            "address": [
                "121099, Г. Москва",
                "ул. Новый Арбат, д.36",
            ], 
            "phones": [
                "+7 (495) 633-60-02",
            ],
            "barcode":  "static/images/qr.png",
            "barcode_single": "static/images/qr.png",
            "email": "kow@mos.ru",
            "link": "https://www.mos.ru/kos",
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
                }
            ]  
        },
        {
            "id": '0',
            "title": "Комитет общественных связей и молодежной политики города Москвы", 
            "text": "doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.", 
            "note": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reprehenderit, enim.",
            "img": "static/images/woman.png",
            "logo_single": "http://127.0.0.1:5000/static/images/icons/img-10.svg",
            "address": [
                "121099, Г. Москва",
                "ул. Новый Арбат, д.36",
            ], 
            "phones": [
                "+7 (495) 633-60-02",
            ],
            "barcode":  "static/images/qr.png",
            "barcode_single": "static/images/qr.png",
            "email": "kow@mos.ru",
            "link": "https://www.mos.ru/kos",
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
                }
            ]  
        },
        {
            "id": '0',
            "title": "Комитет общественных связей и молодежной политики города Москвы", 
            "text": "doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.", 
            "note": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reprehenderit, enim.",
            "img": "static/images/woman.png",
            "logo_single": "http://127.0.0.1:5000/static/images/icons/img-10.svg",
            "address": [
                "121099, Г. Москва",
                "ул. Новый Арбат, д.36",
            ], 
            "phones": [
                "+7 (495) 633-60-02",
            ],
            "barcode":  "static/images/qr.png",
            "barcode_single": "static/images/qr.png",
            "email": "kow@mos.ru",
            "link": "https://www.mos.ru/kos",
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
                }
            ]  
        },
        {
            "id": '0',
            "title": "Комитет общественных связей и молодежной политики города Москвы", 
            "text": "doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.", 
            "note": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reprehenderit, enim.",
            "img": "static/images/woman.png",
            "logo_single": "http://127.0.0.1:5000/static/images/icons/img-10.svg",
            "address": [
                "121099, Г. Москва",
                "ул. Новый Арбат, д.36",
            ], 
            "phones": [
                "+7 (495) 633-60-02",
            ],
            "barcode":  "static/images/qr.png",
            "barcode_single": "static/images/qr.png",
            "email": "kow@mos.ru",
            "link": "https://www.mos.ru/kos",
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
                }
            ]  
        },
        {
            "id": '0',
            "title": "рода Москвы", 
            "text": "doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.", 
            "note": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reprehenderit, enim.",
            "img": "static/images/woman.png",
            "logo_single": "http://127.0.0.1:5000/static/images/icons/img-10.svg",
            "address": [
                "121099, Г. Москва",
                "ул. Новый Арбат, д.36",
            ], 
            "phones": [
                "+7 (495) 633-60-02",
            ],
            "barcode":  "static/images/qr.png",
            "barcode_single": "static/images/qr.png",
            "email": "kow@mos.ru",
            "link": "https://www.mos.ru/kos",
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
                }
            ]  
        }
    ]

    

    def __init__ (self):
        print("OrganizationsController created")


    def get_all_tour_agent (self):
        # находит и возвращает организацию по id
        return self.data_set

    def get_single_tour_agent (self, id):
        # находит и возвращает организацию по id
        id = 0

        single_tour = {
            "title":    self.data_set[id]['title'],
            "logo":     self.data_set[id]['logo_single'],
            "text":     self.data_set[id]['text'],
            "address":  self.data_set[id]['address'], 
            "phones":   self.data_set[id]['phones'],
            "email":    self.data_set[id]['email'],
            "link":     self.data_set[id]['link'],
            "barcode":  self.data_set[id]['barcode_single'],
            "images":   self.data_set[id]['images'],
            "timetable": self.data_set[id]['timetable']
        }

        return single_tour


    def create_new_tour_agent (self, data):
        # в data придет вся необходимая информация для добавления новой организации
        return True


    def update_tour_agent (self, data):
        # в data придет информация которую нужно обновить. минимум 1 какое-то поле, максимум все поля
        return True


    def delete_tour_agent (self, id):
        # удаляет организацию по id
        return True