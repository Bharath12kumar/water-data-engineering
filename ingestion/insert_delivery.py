import mysql.connector
from datetime import date 

def insert_delivery(order_id,delivery_quantity,_returned_empty_cans,delivery_date,remarks):
    try:
        connection=mysql.connector.connect(
        hostname='localhost',
        user='root',
        password='Bk$aug2025',
        database='water_business'
        )

    cursor=connection.cursor()

    query="INSERT INTO deliveries"
