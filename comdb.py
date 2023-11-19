

from pymongo import MongoClient
client = MongoClient("mongodb://127.0.0.1:27017")
database = client.mpc
collection = database.RJ
def add_document():
    data = {
        "name": "Papu",
        "age": 30,
        "email": "papu@example.com",
        "city": "Pune"
    }
    collection.insert_one(data)
    print("Document inserted successfully.")

def update_document():
    update_query = {"name": "Papu"}
    new_values = {"$set": {"age": 20}}
    collection.update_many(update_query, new_values)
    print("Document update successfully.")

def delete_document():
    delete_query = {"name": "Papu"}
    collection.delete_many(delete_query)
    print("Deleted")
def menu():
    while True:
        print("\nMENU")
        print("1. Add Document")
        print("2. Update Document")
        print("3. Delete Document")
        print("4. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            add_document()
        elif choice == "2":
            update_document()
        elif choice == "3":
            delete_document()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a valid option.")
if __name__ == "__main__":
    menu()
client.close()
