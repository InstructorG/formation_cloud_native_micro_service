

## Conteneuriser une image :

1. Créer une image Docker de l'application avec le tag `microservice:0.0.1`.

2. Exécuter un conteneur à partir de l'image.

3. Relancer le conteneur en utilisant `order.db` comme volume (`-v`).

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
