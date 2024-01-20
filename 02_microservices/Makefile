

.PHONY: start_deliver
start_deliver:
	uvicorn deliver.src.microservice.deliver.api:app  --reload --port 8001 --host "0.0.0.0" &

.PHONY: start_stock
start_stock:
	uvicorn stock.src.microservice.stock.api:app  --reload --port 8002 --host "0.0.0.0" &

.PHONY: start_payment
start_payment:
	uvicorn payment.src.microservice.payment.api:app  --reload --port 8003 --host "0.0.0.0" &


.PHONY: start_order
start_order:
	uvicorn order.src.microservice.order.api:app  --reload --port 8004 --host "0.0.0.0"


start_microservices: start_deliver start_payment start_stock  start_order


.PHONY: clean
clean:
	kill $$( lsof -i -P | grep LISTEN | grep -iE ':8001|:8002|:8003|:8004' | awk -F " " '{print $2}') 2>/dev/null ; true
