import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Bk$aug2025',
        database='water_business'
    )

    cursor = connection.cursor()

    query = "INSERT INTO customers (name, phone, address) VALUES (%s, %s, %s)"
    values = ("Bujji", "8247885095", "Kancharam")

    cursor.execute(query, values)
    connection.commit()

    print("Customer inserted successfully!")

except mysql.connector.Error as err:
    print("Database Error:", err)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed.")