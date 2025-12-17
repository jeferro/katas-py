from src.import_users.user_importer import UserImporter


def test_import_users(snapshot):
    result = UserImporter.import_users()
    assert result == snapshot
