from src.import_users.user_csv_fetcher import UserCsvFetcher
from src.import_users.user_web_fetcher import UserWebFetcher


class UserImporter:

    @staticmethod
    def import_users():
        user_csv_fetcher = UserCsvFetcher()
        user_web_fetcher = UserWebFetcher()

        csv_provider = user_csv_fetcher.fetch()

        b = user_web_fetcher.fetch()

        # merge arrays
        return csv_provider + b
