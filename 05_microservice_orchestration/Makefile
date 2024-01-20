

.PHONY: build_deliver
build_deliver:
	cd deliver && docker build -t deliver:0.0.1 .

.PHONY: build_stock
build_stock:
	cd stock && docker build -t stock:0.0.1 .

.PHONY: build_payment
build_payment:
	cd payment && docker build -t payment:0.0.1 .

.PHONY: build_order
build_order:
	cd order && docker build -t order:0.0.1 .


build_microservices: build_deliver build_payment build_stock  build_order


.PHONY: docker_compose_up
docker_compose_up:
	docker-compose -f docker-compose.yml up


.PHONY: clean
clean:
	kill $$( lsof -i -P | grep LISTEN | grep -iE ':8001|:8002|:8003|:8004' | awk -F " " '{print $2}') 2>/dev/null ; true
