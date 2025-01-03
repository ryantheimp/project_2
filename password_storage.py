import json
import csv

class PasswordStorage:
    def __init__(self):
        self.passwords = set()

    def add_password(self, password):
        if password in self.passwords:
            print("Этот пароль уже существует в базе!")
        else:
            self.passwords.add(password)

    def export_to_file(self):
        with open("passwords.json", "w") as json_file:
            json.dump(list(self.passwords), json_file)
        with open("passwords.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Password"])
            for password in self.passwords:
                writer.writerow([password])
