import mysql.connector
from datetime import date,timedelta
target_date=date.today()-timedelta(days=1)

try:
    connection=mysql.connector.connect(
        host='localhost',
        user='root',
        password='Bk$aug2025',
        database='water_business'
    )

    cursor=connection.cursor()

    delete_query="Delete from daily_summary where summary_date =%s"
    delete_values=(target_date,)

    cursor.execute(delete_query,delete_values)


    orders_query = """
    select count(*) as total_orders ,
    coalesce(sum(quantity), 0) as total_quantity ,
    count(distinct customer_id) as total_customers
    from orders where order_date=%s and status='DELIVERED'
    """

    cursor.execute(orders_query, (target_date,))
    result = cursor.fetchone()  
    total_orders, total_quantity, total_customers = result

    revenue_query = """
    SELECT COALESCE(SUM(amount), 0)
    FROM payments
    WHERE payment_date = %s
    AND paid = 'YES'
    """

    cursor.execute(revenue_query, (target_date,))
    revenue_result = cursor.fetchone()

    total_revenue = revenue_result[0]

    insert_query = """
    INSERT INTO daily_summary
    (summary_date, total_orders, total_quantity, total_revenue, total_customers)
    VALUES (%s, %s, %s, %s, %s)
    """

    insert_values = (target_date, total_orders, total_quantity, total_revenue, total_customers)

    cursor.execute(insert_query, insert_values)

    connection.commit()

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
