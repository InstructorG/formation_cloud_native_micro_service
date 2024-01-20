from deliver.src.microservice.deliver.models.deliver_item import DeliverItem
from deliver.src.microservice.deliver.storage.schedule import SCHEDULE_STORAGE


class DeliverService:

    def create(self, deliver_item : DeliverItem):
        SCHEDULE_STORAGE[deliver_item.deliver_id] = deliver_item.dict()
        return {"message": "objet programmé pour livraison", "deliver": deliver_item.dict()}

    def delete(self, deliver_id):
        if not SCHEDULE_STORAGE.get(deliver_id):
            return { "error" : f"objet {deliver_id} absent !"}
        del SCHEDULE_STORAGE[deliver_id]
        return {"message": "objet supprimé pour livraison", "id": deliver_id}

    def update(self,  deliver_item : DeliverItem):
        SCHEDULE_STORAGE[deliver_item.deliver_id] = deliver_item.dict()
        return {"message": "livraison mis à jour", "deliver": deliver_item.dict() }
