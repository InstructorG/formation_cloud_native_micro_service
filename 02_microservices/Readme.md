# LES MICROSERVICES

Commencez par lancer les microservices grâce à la commande suivante:

```bash
cd 02_microservices && make start_microservices
```

## PARTIE 1:

### ***Assurez-vous que tous les tests sont fonctionnels !*** 

Dans un autre terminal, vérifiez que les tests sont réussis avec la commande suivante :

```bash
pytest 02_microservices/order/tests
```

### 1 - Lever une erreur si un produit n'est pas disponible dans le stock ! 

Pour ce faire, utilisez le code suivant à l'emplacement approprié :

```python
raise Exception({"status": "failed", "message": f"Les produits suivants ne sont pas disponibles : {not_available_items}"})
```

### 2 - Les magasins de Lille ne font plus partie de la marketplace ! 

Merci de supprimer tous les magasins situés dans cette ville ! 

Ré-exécutez les tests.

---

## PARTIE 2 

### ***Grâce à Swagger, créez une commande et programmez sa livraison***

Vous pouvez accéder aux Swaggers des différents microservices en utilisant les URLs suivantes :

Remplacez `<ip>` par votre adresse IP 

- ORDER : http://<ip>:8004/docs
- PAYMENT : http://<ip>:8003/docs
- STOCK : http://<ip>:8002/docs
- DELIVER : http://<ip>:8001/docs

### 1 - Créez une commande avec les produits suivants :

```json
{
    "products" : [
        { 
            "name" : "levis",
            "type" : "chemise",
            "quantity" : 4 
        },
        { 
            "name" : "celio",
            "type" : "pantalon",
            "quantity" : 4 
        }
    ]
}
```

### 2 - Payez la commande

### 3 - Programmez la commande pour une livraison

```json
{
    "object" : {
            "products" : [
                { 
                    "name" : "levis",
                    "type" : "chemise",
                    "quantity" : 4 
                },
                { 
                    "name" : "celio",
                    "type" : "pantalon",
                    "quantity" : 4 
                }
            ]
        },
    "transport" : "avion"
}
```