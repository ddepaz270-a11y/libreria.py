import mysql.connector # pyright: ignore[reportMissingImports]
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cafeteria"
)

def Create():
    customerName = input("ENTER CUSTOMER NAME: ")
    productName = input("ENTER PRODUCT NAME: ")
    quantity = int(input("ENTER QUANTITY: "))
    orderType = input("ENTER ORDER TYPE (Regular, Student, Teacher): ")

    if orderType == "Student":
        discount = 10
    elif orderType == "Teacher":
        discount = 15
    elif orderType == "Regular":
        discount = 0
    else:
        print("INVALID ORDER TYPE.")
        return

    total = quantity
    cursor = conexion.cursor()
    query = "INSERT INTO orders (customerName, productName, quantity, orderType, discount, total) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (customerName, productName, quantity, orderType, discount, total))
    conexion.commit()
    print("REGISTRATION COMPLETE.")


def Read():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM orders")

    for fila in cursor.fetchall():
        print(*fila)

def update():
 id_actualizar = int(input("ENTER ID: "))
customerName = input("ENTER CUSTOMER NAME: ")
productName = input("ENTER PRODUCT NAME: ")
quantity = int(input("ENTER QUANTITY: "))
orderType = input("ENTER ORDER TYPE (Regular, Student, Teacher): ")

if orderType == "Student":
        discount = 10
elif orderType == "Teacher":
        discount = 15
elif orderType == "Regular":
        discount = 0
else:
        print("INVALID ORDER TYPE.")


total = quantity
cursor = conexion.cursor()
query = "UPDATE orders SET customerName=%s, productName=%s, quantity=%s, orderType=%s, discount=%s, total=%s WHERE id=%s"
cursor.execute(query, ("customerName, productName, quantity, orderType, discount, total, id_actualizar"))
conexion.commit()

print("UPDATE COMPLETE!!!")

def delete():
    id = int(input("ENTER ID: "))
    cursor = conexion.cursor()
    query = "DELETE FROM orders WHERE id=%s"
    cursor.execute(query, (id,))
    conexion.commit()
    print("DELETE COMPLETE.")


def menu():
    while True:
        fila = ["1. CREATE", "2. READ", "3. UPDATE", "4. DELETE", "5. EXIT"]
        for opcion in fila:
            print(opcion)
        desi = int(input("ENTER THE DESIRED OPTION: "))
        if desi == 1:
            Create()
        elif desi == 2:
            Read()
        elif desi == 3:
            update()
        elif desi == 4:
            delete()
        elif desi == 5:
            print("FINISHED")
            break
        else:
            print("ENTER A VALID OPTION.")

menu()