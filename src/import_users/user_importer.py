from typing import List

from src.import_users.user_fetchers.user_fetcher import UserFetcher


class UserImporter:

    def __init__(self,
                 user_fetchers: List[UserFetcher]):
        self.user_fetchers = user_fetchers

    def import_users(self):
        users = []
        for user_fetcher in self.user_fetchers:
            users.extend(user_fetcher.fetch())

        return users
