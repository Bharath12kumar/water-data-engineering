import mysql.connector
from datetime import date 

def customer_payment(order_id,amount,paid,payment_date):
    try:
        connection=mysql.connector.connect(
            host='localhost',
            user='root',
            password='Bk$aug2025',
            database='water_business'

        )
    
        cursor=connection.cursor()

        query="insert into payments(order_id,amount,paid,payment_date) values(%s,%s,%s,%s)"
        values=(order_id,amount,paid,payment_date)

        cursor.execute(query,values)
        connection.commit()

        payment_id=cursor.lastrowid
        print("order sucessfuly placed -",payment_id)

        return payment_id
    
    except mysql.connector.Error as Err:
        print("Error!",Err)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
        print("Connection closed.")



 

customer_payment(1,200,200,date.today())


