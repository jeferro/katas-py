from src.import_users.user_fetchers.user_csv_fetcher import UserCsvFetcher
from src.import_users.user_importer import UserImporter
from src.import_users.user_fetchers.user_web_fetcher import UserWebFetcher


def test_import_users(snapshot):
    user_importer = UserImporter([
        UserCsvFetcher(),
        UserWebFetcher()
    ])

    result = user_importer.import_users()

    assert result == snapshot
