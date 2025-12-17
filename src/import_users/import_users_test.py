from src.import_users.user_csv_fetcher import UserCsvFetcher
from src.import_users.user_importer import UserImporter
from src.import_users.user_web_fetcher import UserWebFetcher


def test_import_users(snapshot):
    user_csv_fetcher = UserCsvFetcher()
    user_web_fetcher = UserWebFetcher()
    user_importer = UserImporter(user_csv_fetcher, user_web_fetcher)

    result = user_importer.import_users()

    assert result == snapshot
