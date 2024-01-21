

## Conteneuriser une image :

1. Créer une image Docker de l'application avec le tag `microservice:0.0.1`.

    docker build -t  microservice:0.0.1  . 


2. Exécuter un conteneur à partir de l'image.

3. Relancer le conteneur en utilisant `order.db` comme volume (`-v`).

    docker run -p 555:8000  -v $(pwd)/order.db:/api/new.db -e DATABASE_CONNEXION="sqlite:///new.db" microservice:0.0.1


4. Exécuter des requêtes à partir du Docker host.

```json
{
    "items" : [
        { 
            "id" : 1,
            "name" : "levis",
            "price" : 20,
            "quantity" : 4 
        },
        { 
            "id" : 2,
            "name" : "celio",
            "price" : 12,
            "quantity" : 4 
        }
    ]
}
```
