from sqlmodel import Session

from db import engine
from models import Customer, Transaction

session = Session(engine)
customer = Customer(
    name="Freddy",
    description="Dev Platam",
    email="freddy@platam.co",
    age=33,
)
session.add(customer)
session.commit()

for x in range(100):
    session.add(
        Transaction(
            customer_id=customer.id,
            description=f"Test number {x}",
            ammount=10 * x,
        )
    )
session.commit()