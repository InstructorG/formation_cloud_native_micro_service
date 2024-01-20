from fastapi import FastAPI

from payment.src.microservice.payment.payment_service import PaymentService

app = FastAPI(debug=True)


@app.post("/payment/pay")
def create(to_pay_object: dict):
    return PaymentService().create(to_pay_object)


@app.delete("/payment/cancel/{bill_id}")
def delete(bill_id: str):
    return PaymentService().cancel(bill_id)


@app.post("/payment/update/{bill_id}")
def update(bill_id: str, to_pay_object: dict):
    return PaymentService().update(bill_id, to_pay_object)

