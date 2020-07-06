import json
import os
import config


class BanksController:
    data = []

    def __init__(self):
        self.data = self.__load_banks()

    def load_bank(self, index):
        r = str(self.data[index]).replace("'", '"')
        r = r.replace('filename="', "filename='")
        r = r.replace('")', "')")
        return r.replace('"static"', "'static'")

    def delete_bank(self, bank_name):
        for element in self.data:
            if element["name"] == bank_name:
                self.data.remove(element)
                self.__save_data()
                break
        return 0

    def banks_len(self):
        return str(len(self.data))

    @staticmethod
    def __load_banks():
        data = []
        try:
            with open(config.UPLOAD_FOLDER + '/' + 'banks.json') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            with open(config.UPLOAD_FOLDER + '/' + 'banks.json', 'w') as outfile:
                json.dump(data, outfile)
        return data

    def __save_data(self):
        with open(config.UPLOAD_FOLDER + '/' + 'banks.json', 'w') as outfile:
            json.dump(self.data, outfile, indent=4)

    def add_new_bank(self, logo, name, time, floors, description):
        new_bank = {"logo": logo, "name": name, "time": time, "floors": floors, "description": description}
        self.data.append(new_bank)
        self.__save_data()
        return new_bank