import urllib.request
import json
import datetime

from src.import_users.user_fetcher import UserFetcher


class UserWebFetcher(UserFetcher):

    def fetch(self) -> list[list[str]]:
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