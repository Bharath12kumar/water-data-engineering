import mysql.connector
from datetime import date 

def insert_delivery(order_id,delivered_quantity,returned_empty_cans,delivery_date,remarks,status):

    try:
        connection=mysql.connector.connect(
            host='localhost',
            user='root',
            password='Bk$aug2025',
            database='water_business'
        )

        cursor=connection.cursor()

        delivery_query="INSERT INTO deliveries (order_id,delivered_quantity,returned_empty_cans,delivery_date,remarks,status) values(%s,%s,%s,%s,%s,%s)"
        delivery_values=(order_id,delivered_quantity,returned_empty_cans,delivery_date,remarks,status)

        cursor.execute(delivery_query,delivery_values)
        connection.commit()

        delivery_id=cursor.lastrowid
        print("order placed sucessfully -",delivery_id)
        return delivery_id

    except mysql.connector.Error as err:
        connection.rollback()
        print("Error:",err)
        print("Transaction was rolled back")
    
    finally :
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
           connection.close()
           print("Connection closed.")


if __name__=="__main__":
    insert_delivery(3,5,0,date.today(),'')








