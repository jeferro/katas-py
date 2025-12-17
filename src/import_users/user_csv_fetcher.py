import csv
import os

from src.import_users.user_fetcher import UserFetcher


class UserCsvFetcher(UserFetcher):

    def fetch(self) -> list[list[str]]:
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