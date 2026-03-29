import mysql.connector 
from datetime import date


def insert_order(customer_id, quantity, order_date, status):
    try:
        connection=mysql.connector.connect(
            host='localhost',
            user='root',
            password='Bk$aug2025',
            database='water_business'
        )


        cursor=connection.cursor()

        order_query="insert into orders (customer_id,quantity,order_date,status) values(%s, %s, %s,%s)"
        order_values=(customer_id,quantity,order_date,status)
    
        cursor.execute(order_query,order_values)
        connection.commit()

        order_id=cursor.lastrowid
        print ("order placed sucessfully")
        return order_id

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

insert_order(1,4, date.today(),"placed")