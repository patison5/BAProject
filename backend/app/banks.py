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
            "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Tempore odit at impedit corporis, deserunt, totam velit architecto exercitationem enim similique quia expedita, fugit quam praesentium accusantium! Earum velit mollitia fuga minus quae quaerat at cumque nobis adipisci commodi est aliquid quis reprehenderit animi veniam, architecto nemo doloribus illo harum! Distinctio sit iure mollitia consequuntur libero! Ex, minus ducimus. Temporibus obcaecati quibusdam cupiditate, quasi impedit nostrum dolores ab laborum odit excepturi, recusandae voluptas, quisquam tenetur blanditiis est nesciunt tempora ipsa inventore necessitatibus. Earum suscipit sapiente, velit cum quis, ratione maxime minus dignissimos alias unde! Quae excepturi, sapiente ipsum vitae voluptatibus vero?",
            "img": "http://127.0.0.1:5000/static/images/afisha.png"
        },
        {
            "title": "Сбербанк",
            "time": "Круглосуточно",
            "stage": "1,5,12,19 Этажи",
            "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Tempore odit at impedit corporis, deserunt, totam velit architecto exercitationem enim similique quia expedita, fugit quam praesentium accusantium! Earum velit mollitia fuga minus quae quaerat at cumque nobis adipisci commodi est aliquid quis reprehenderit animi veniam, architecto nemo doloribus illo harum! Distinctio sit iure mollitia consequuntur libero! Ex, minus ducimus. Temporibus obcaecati quibusdam cupiditate, quasi impedit nostrum dolores ab laborum odit excepturi, recusandae voluptas, quisquam tenetur blanditiis est nesciunt tempora ipsa inventore necessitatibus. Earum suscipit sapiente, velit cum quis, ratione maxime minus dignissimos alias unde! Quae excepturi, sapiente ipsum vitae voluptatibus vero?",
            "img": "http://127.0.0.1:5000/static/images/afisha.png"
        }
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