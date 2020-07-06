import json
import os
import config


class AdvController:
    data = []

    def __init__(self):
        self.data = self.__load_ads()

    def load_adv(self):
        r = str(self.data).replace("'", '"')
        r = r.replace('filename="', "filename='")
        r = r.replace('")', "')")
        return r.replace('"static"', "'static'")

    def delete_adv(self, adv_name):
        for element in self.data:
            if element["name"] == adv_name:
                self.data.remove(element)
                self.__save_data()
                break
        return 0

    def banks_len(self):
        return str(len(self.data))

    @staticmethod
    def __load_ads():
        data = []
        try:
            with open(config.UPLOAD_FOLDER + '/' + 'ads.json') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            with open(config.UPLOAD_FOLDER + '/' + 'ads.json', 'w') as outfile:
                json.dump(data, outfile)
        return data

    def __save_data(self):
        with open(config.UPLOAD_FOLDER + '/' + 'ads.json', 'w') as outfile:
            json.dump(self.data, outfile, indent=4)

    def add_new_adv(self, logo, name, time, date_start, date_finish, file2):
        new_bank = {"logo": logo, "name": name, "date_start": date_start, "date_finish": date_finish, "time": time,
                    "file2": file2}
        self.data.append(new_bank)
        self.__save_data()
        return new_bank
