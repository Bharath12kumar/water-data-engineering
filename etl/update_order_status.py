import mysql.connector

try:
    connection=mysql.connector.connect(
            host='localhost',
            user='root',
            password='Bk$aug2025',
            database='water_business'
        )

    cursor=connection.cursor()

    update_query="""UPDATE orders o
    JOIN deliveries d ON o.order_id=d.order_id
    SET o.status = 'DELIVERED'
    WHERE  d.status='COMPLETED' and o.status!='DELIVERED'
    """
    cursor.execute(update_query)
    connection.commit()
    print(cursor.rowcount, "orders updated to DELIVERED")

except mysql.connector.Error as Err:
    connection.rollback()
    print("Error:",Err)
    print("Transaction was rolled back")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
    print("connection closed.")