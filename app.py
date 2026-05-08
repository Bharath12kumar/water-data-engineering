from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from datetime import date

from db import get_connection



import sys 
sys.path.append(r'C:\Users\Bharath\Desktop\water-data-engineering\ingestion')
                
from insert_customer import insert_customer
from insert_order import insert_order
from insert_payment import insert_payment
from insert_delivery import insert_delivery

app=FastAPI()

class customer(BaseModel):
    name:str
    phone:int
    address:str


@app.post('/customer/register')
def register_customer(customer:customer):
    customer_id=insert_customer(customer.name,customer.phone,customer.address)
    if customer_id:
        return {"message":"sucessfully created","customer_id":customer_id}

    else :
         raise HTTPException(status_code=500,detail="user not created please try again ")

class order(BaseModel):
    customer_id:int
    quantity: int
    status:str

@app.post('/customer/insert_order')
def place_order(order:order):
    order_id=insert_order(order.customer_id,order.quantity,date.today(),order.status)
    if order_id:
        return{"message":"order placed","order id":order_id ,"no.of quantity":order.quantity}
    else:
         raise HTTPException(status_code=500,detail="order not placed please try again")



class payments(BaseModel):
    order_id:int
    amount:int
    paid:str


@app.post('/customer/payments')
def customer_payments(payments:payments):
    payment_id=insert_payment(payments.order_id,payments.amount,payments.paid,date.today())
    if payment_id:
        return {"message":"payment completed","payment id ":payment_id,"amount paid":payments.amount}
    else:
        raise HTTPException(status_code=500,detail="payment failed please try again")

class delivery(BaseModel):
    order_id:int
    delivered_quantity:int
    returned_empty_cans:int
    remarks:str
    status:str

@app.post('/worker/delivery_update')
def delivery_update(delivery:delivery):
    delivery_id=insert_delivery(delivery.order_id,delivery.delivered_quantity,delivery.returned_empty_cans,date.today(),delivery.remarks,delivery.status)
    if delivery_id:
        return {"message":"delivery completed","delivery id":delivery_id ,"deliverd_quantity":delivery.delivered_quantity}
    else:
        raise HTTPException(status_code=500,detail="delivery failed please attempt")
    



@app.get('/customer/order')
def get_order():
        connection = get_connection()
        cursor=connection.cursor(dictionary=True)
        order_query="""select a.customer_id,a.name,b.order_date,b.order_id,b.quantity,b.status from customers a join orders b on a.customer_id=b.customer_id """
        cursor.execute(order_query)
        results=cursor.fetchall()
        connection.close()
        return results           


@app.get('/client/order')
def client_order(user_id:int):
    connection=get_connection()
    cursor=connection.cursor(dictionary=True)
    order_query="""select a.customer_id,a.name,b.order_date,b.order_id,b.quantity,b.status from customers a join orders b on a.customer_id=b.customer_id where a.customer_id=%s"""
    cursor.execute(order_query,(user_id,))
    results=cursor.fetchall()
    cursor.close()
    connection.close()
    return results 


 