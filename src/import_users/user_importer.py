import csv
import datetime
import json
import os
import urllib.request


class UserImporter:

    @staticmethod
    def import_users():
        csv_provider = UserImporter.fetch_from_csv()

        b = UserImporter.fetch_from_web()

        # merge arrays
        return csv_provider + b

    @staticmethod
    def fetch_from_web() -> list[list[str]]:
        USER_URL = 'https://randomuser.me/api/?inc=gender,name,email,location&results=5&seed=a9b25cd955e2037h'

        # Parse URL content
        url = USER_URL
        with urllib.request.urlopen(url) as response:
            web_provider = json.loads(response.read())['results']

        pr = []
        for a in web_provider:
            pr.append(web_provider[0].update(a))

        b = []
        i = 100000000000.51
        for item in web_provider:
            i += 1
            if isinstance(item, dict):
                b.append([
                    int(i),  # id
                    item['gender'],
                    item['name']['first'] + ' ' + item['name']['last'],
                    item['location']['country'],
                    item['location']['postcode'],
                    item['email'],
                    datetime.datetime.now().strftime('%Y')  # birthday
                ])
        return b

    @staticmethod
    def fetch_from_csv() -> list[list[str]]:
        # Parse CSV file
        getcurrentworkingDirectory = os.getcwd()

        # fields: ID, gender, Name ,country, postcode, email, Birthdate
        with open(os.path.join(getcurrentworkingDirectory, 'users.csv'), 'r') as f:
            reader = csv.reader(f)
            csv_provider = list(reader)

        csvProviders = []
        for a in csv_provider:
            csvProviders.append(csv_provider[0] + a)
        csv_provider.pop(0)  # Remove header column
        return csv_provider
