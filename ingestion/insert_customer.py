import mysql.connector

def insert_customer(name,phone,address):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Bk$aug2025',
            database='water_business'
        )
      
        cursor = connection.cursor()

        query = "INSERT INTO customers (name, phone, address) VALUES (%s, %s, %s)"
        values = (name, phone, address)

        cursor.execute(query, values)
        connection.commit()

        customer_id=cursor.lastrowid
        print("sucessfully created your cust no -",customer_id)
        return customer_id
       

    except mysql.connector.Error as err:
        print(" Error!:", err)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
        print("Connection closed.")

insert_customer("Ravi", "9876543210", "Hyderabad")