from datetime import date,timedelta 
import random
from faker import Faker
import sys
sys.path.append(r'C:\Users\Bharath\Desktop\water-data-engineering\ingestion')


from insert_customer import insert_customer
from insert_order import insert_order
from insert_delivery import insert_delivery
from insert_payment import insert_payment

fake = Faker('en_IN')
for i in range(100):

    name=fake.name()
    number=fake.phone_number()
    address=fake.city()

    customer_id=insert_customer(name,number,address)

    for j in range(random.randint(3,10)):
        random_days=random.randint(1,30)
        order_date=date.today()-(timedelta(days=random_days))
        status=random.choice(['PLACED','DELIVERED'])
        quantity=random.randint(1,10)

        order_id=insert_order(customer_id, quantity, order_date, status)

        if status=='DELIVERED':
            price_per_can = 50
            amount = quantity * price_per_can

            paid=random.choice(['YES','YES','YES','YES','NO'])

            payment_days=random.randint(0,3)
            payment_date=order_date+timedelta(days=payment_days)
            payment_id=insert_payment(order_id,amount,paid,payment_date)

            delivery_date=random.randint(0,3)
            delivery_date=order_date+timedelta(days=delivery_date)

            delivery_id=insert_delivery(order_id,quantity,0,delivery_date,'COMPLETED','COMPLETED')