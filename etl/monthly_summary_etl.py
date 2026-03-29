from datetime import date,timedelta
import mysql.connector
today=date.today()
first_date=today.replace(day=1)
target_date=first_date-timedelta(days=1)
target_year=target_date.year
target_month=target_date.month




try:
    connection=mysql.connector.connect(
        host='localhost',
        user='root',
        password='Bk$aug2025',
        database='water_business'
    )


    cursor=connection.cursor()

    delete_query="Delete from monthly_summary where Year =%s and month=%s"
    delete_values=(target_year,target_month)

    cursor.execute(delete_query,delete_values)

    orders_query = """
    select 
    count(distinct customer_id)
    from orders
    WHERE status='DELIVERED' and YEAR(order_date)=%s and MONTH(order_date)=%s;
    """

    cursor.execute(orders_query,(target_year,target_month))
    result=cursor.fetchone()
    total_customers=result[0]


    monthly_summary="""select 
    coalesce(sum(total_orders),0) as total_orders,
    coalesce(sum(total_quantity),0) as total_quantity,
    coalesce(sum(total_revenue),0) as total_revenue
    FROM daily_summary
    where year(summary_date)=%s
    and month(summary_date)=%s
    """

    cursor.execute(monthly_summary,(target_year,target_month))
    monthly_result=cursor.fetchone()

    total_orders, total_quantity, total_revenue=monthly_result

    insert_query="""
     INSERT INTO monthly_summary
    (year, month, total_orders,total_quantity, total_revenue, total_customers)
    VALUES (%s, %s, %s, %s, %s,%s) 
    """

    insert_values = (target_year,target_month, total_orders, total_quantity,total_revenue, total_customers)

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



    




