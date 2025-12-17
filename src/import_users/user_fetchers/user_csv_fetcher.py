import csv
import os

from src.import_users.user_fetchers.user_fetcher import UserFetcher


class UserCsvFetcher(UserFetcher):

    def fetch(self) -> list[list[str]]:
        # Parse CSV file
        current_working_directory = os.getcwd()
        csv_path = os.path.join(current_working_directory, 'users.csv')

        # fields: ID, gender, Name ,country, postcode, email, Birthdate
        with open(csv_path, 'r') as f:
            reader = csv.reader(f)
            csv_provider = list(reader)

        csv_provider.pop(0)  # Remove header column

        return csv_provider