from src.import_users.user_importer import UserImporter

providers = UserImporter.import_users()

# Print users
print("*********************************************************************************")
print("* ID\t\t* COUNTRY\t* NAME\t\t* EMAIL\t\t\t\t*")
print("*********************************************************************************")
for j in range(len(providers)):
    print(f"* {providers[j][0]}\t* {providers[j][3]}\t* {providers[j][2]}\t* {providers[j][5]}\t*")
print("*********************************************************************************")
print(f"{len(providers)} users in total!")
