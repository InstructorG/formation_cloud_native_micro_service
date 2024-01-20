
.PHONY: start_monolithe
start_monolithe:
	uvicorn src.monolithe.api:app  --reload --port 8010 --host "0.0.0.0"


.PHONY: clean
clean:
	kill $$( lsof -i -P | grep LISTEN | grep -iE ':8010' | awk -F " " '{print $2}') 2>/dev/null ; true
