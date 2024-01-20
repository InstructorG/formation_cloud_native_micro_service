from microservice.payment.models.bill import Bill
from microservice.payment.storage.payment import PAYEMENT_STORAGE


class PaymentService:

    def create(self, to_pay_object):
        bill = Bill(object_details=str(to_pay_object))
        PAYEMENT_STORAGE[bill.bill_id] = bill.dict()
        return {"message": "Factrue créé", "facture": bill.dict()}

    def cancel(self, bill_id):
        del PAYEMENT_STORAGE[bill_id]
        return {"message": "Facture supprimé ", "id": bill_id}

    def update(self, bill_id, to_pay_object):
        bill = Bill(bill_id=bill_id, object_details=str(to_pay_object))
        PAYEMENT_STORAGE[bill.bill_id] = bill.dict()
        return {"message": "Facture mis à jour", "facture": bill.dict()}
