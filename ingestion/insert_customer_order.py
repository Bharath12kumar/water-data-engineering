import mysql.connector 
from datetime import date
date.today()
try:
    connection=mysql.connector.connect(
        host='localhost',
        user='root',
        password='Bk$aug2025',
        database='water_business'
    )

    cursor=connection.cursor()

    connection.start_transaction()

    query = "INSERT INTO customers (name, phone, address) VALUES (%s, %s, %s)"
    values = ("tirumla", "9122305645", "Kancharam")

    cursor.execute(query,values)
    customer_id = cursor.lastrowid

    order_query="insert into orders (customer_id,quantity,order_date,status) values(%s, %s, %s,%s)"
    order_values=(customer_id,4,date.today(),"placed")

    cursor.execute(order_query,order_values)
    
    connection.commit()
    print("Transaction  successful")

except mysql.connector.Error as err:
    connection.rollback()
    print("Error:",err)
    print("Transaction was rolled back")


finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed.")