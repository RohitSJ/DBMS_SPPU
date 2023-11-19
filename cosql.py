import mysql.connector

# Function to establish connection to the MySQL database
def connect_to_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="RJ40",
        database="k"
    )
    return mydb
def add_data(mydb):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO stud1 (name, age) VALUES (%s, %s)", (name, age))
    mydb.commit()
    print("Data inserted successfully.")

# Function to delete data from the database
def delete_data(mydb):
    id = int(input("Enter ID to delete: "))
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM stud1 WHERE id = %s", (id,))
    mydb.commit()
    print("Data deleted successfully.")

# Function to edit data in the database
def edit_data(mydb):
    id = int(input("Enter ID to edit: "))
    new_name = input("Enter new name: ")
    new_age = int(input("Enter new age: "))
    cursor = mydb.cursor()
    cursor.execute("UPDATE stud1 SET name = %s, age = %s WHERE id = %s", (new_name, new_age, id))
    mydb.commit()
    print("Data updated successfully.")

# Menu function
def menu():
    print("\nMenu:")
    print("1. Add Data")
    print("2. Delete Data")
    print("3. Edit Data")
    print("4. Exit")

if __name__ == "__main__":
    mydb = connect_to_database()
    while True:
        menu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_data(mydb)
        elif choice == '2':
            delete_data(mydb)
        elif choice == '3':
            edit_data(mydb)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    mydb.close()
