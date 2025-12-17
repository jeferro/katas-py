from src.import_users.user_csv_fetcher import UserCsvFetcher
from src.import_users.user_web_fetcher import UserWebFetcher


class UserImporter:

    def __init__(self,
                 user_csv_fetcher: UserCsvFetcher,
                 user_web_fetcher: UserWebFetcher):
        self.user_csv_fetcher = user_csv_fetcher
        self.user_web_fetcher = user_web_fetcher

    def import_users(self):
        csv_users = self.user_csv_fetcher.fetch()

        web_users = self.user_web_fetcher.fetch()

        return csv_users + web_users
