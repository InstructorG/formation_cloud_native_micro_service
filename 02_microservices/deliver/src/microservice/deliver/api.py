from fastapi import FastAPI

from deliver.src.microservice.deliver.deliver_service import DeliverService
from deliver.src.microservice.deliver.models.deliver_item import DeliverItem

app = FastAPI(debug=True)


@app.post("/deliver/schedule")
def create(body: dict):
    deliver_object = DeliverItem(object=body.get("object"), transport=body.get("transport"))
    return DeliverService().create(deliver_object)


@app.delete("/deliver/cancel/{deliver_id}")
def delete(deliver_id: str):
    return DeliverService().delete(deliver_id)


@app.post("/deliver/update/{deliver_id}")
def update(deliver_id:str,body: dict):
    deliver_object = DeliverItem(deliver_id=deliver_id, object=body.get("object"), transport=body.get("transport"))
    return DeliverService().update(deliver_object)
