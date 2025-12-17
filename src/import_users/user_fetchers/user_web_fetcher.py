import urllib.request
import json
import datetime

from src.import_users.user_fetchers.user_fetcher import UserFetcher


class UserWebFetcher(UserFetcher):

    USER_URL = 'https://randomuser.me/api/?inc=gender,name,email,location&results=5&seed=a9b25cd955e2037h'

    def fetch(self) -> list[list[str]]:
        # Parse URL content
        url = self.USER_URL

        with urllib.request.urlopen(url) as response:
            web_provider = json.loads(response.read())['results']

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