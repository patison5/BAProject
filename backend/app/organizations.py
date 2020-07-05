import json
import os
import config
import string


class OrganizationsController:
    data = []

    def __init__(self):
        self.data = self.__load_org()

    def find_all(self, org_type):
        alphabet_li = list(string.ascii_lowercase)
        result_d = {}
        for element in alphabet_li:
            result_d[element] = (self.find_org(element, org_type))
        return str(result_d).replace("'", '"')

    def find_org(self, char, org_type):
        result = []
        char = char.lower()
        for element in self.data:
            if (element["page_type"] == org_type) and (element["name"][0] == char or element["name"][0] == char.upper()):
                result.append(element["name"])
        return result

    def load_org(self, org_name):
        data = {}

        for element in self.data:
            if element["page_type"] == org_name:
                data = element
                r = str(data).replace("'", '"')
                r = r.replace('filename="', "filename='")
                r = r.replace('")', "')")
                return r.replace('"static"', "'static'")

        for element in self.data:
            if element["name"] == org_name:
                data = element
                break

        r = str(data).replace("'", '"')
        r = r.replace('filename="', "filename='")
        r = r.replace('")', "')")
        return r.replace('"static"', "'static'")

    def delete_org(self, org_name):
        for element in self.data:
            if element["name"] == org_name:
                self.data.remove(element)
                self.__save_data()
                break
        return 0

    def org_len(self):
        return str(len(self.data))

    @staticmethod
    def __load_org():
        data = []
        try:
            with open(config.UPLOAD_FOLDER + '/' + 'organizations.json') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            with open(config.UPLOAD_FOLDER + '/' + 'organizations.json', 'w') as outfile:
                json.dump(data, outfile)
        return data

    def __save_data(self):
        with open(config.UPLOAD_FOLDER + '/' + 'organizations.json', 'w') as outfile:
            json.dump(self.data, outfile, indent=4)

    def add_new_org(self, logo_src, name, description, address, phones, mail, url, time, main_photo_src,
                    additional_title, additional_photos, additional_photos_text, main_photo_description, page_type):

        new_org = {"logo": logo_src, "name": name, "description": description, "address": address,
                   "phone": phones, "mail": mail, "url": url, "time": time, "main_photo": main_photo_src,
                   "additional_title": additional_title, "additional_photos": additional_photos,
                   "additional_photos_text": additional_photos_text, "main_photo_description": main_photo_description,
                   "page_type": page_type}
        self.data.append(new_org)
        self.__save_data()
        return new_org


class ToursController:
    data = []
    def __init__(self):
        self.data = self.__load_org()

    def load_org(self, org_name):
        data = {}

        for element in self.data:
            if element["page_type"] == org_name:
                data = element
                r = str(data).replace("'", '"')
                r = r.replace('filename="', "filename='")
                r = r.replace('")', "')")
                return r.replace('"static"', "'static'")

        for element in self.data:
            if element["name"] == org_name:
                data = element
                break

        r = str(data).replace("'", '"')
        r = r.replace('filename="', "filename='")
        r = r.replace('")', "')")
        return r.replace('"static"', "'static'")

    @staticmethod
    def __load_org():
        data = []
        try:
            with open(config.UPLOAD_FOLDER + '/' + 'travels.json') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            with open(config.UPLOAD_FOLDER + '/' + 'travels.json', 'w') as outfile:
                json.dump(data, outfile)
        return data

    def __save_data(self):
        with open(config.UPLOAD_FOLDER + '/' + 'travels.json', 'w') as outfile:
            json.dump(self.data, outfile, indent=4)

    def add_new_travel_tour(self, path, name, description, address, additional_photo):
        new_travel = {"path": path, "name": name, "description": description,
                      "address": address, "additional_photo": additional_photo, "type": "tour"}

        self.data.append(new_travel)
        self.__save_data()

    def add_adv(self, imgs, text1, text2, text3, text4):
        new_travel = {"imgs": imgs, "text1": text1, "text2": text2,
                      "text3": text3, "text4": text4, "type": "adv"}

        self.data.append(new_travel)
        self.__save_data()

    def load_all(self):
        d = self.data
        r = str(d).replace("'", '"')
        r = r.replace('filename="', "filename='")
        r = r.replace('")', "')")
        return r.replace('"static"', "'static'")
