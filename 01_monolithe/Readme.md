# LE MONOLITHE

## PARTIE 1:

1. Lever une erreur si un produit n'est pas disponible dans le stock !

   Pour cela, utilisez le code suivant à l'emplacement approprié :

```python
raise Exception({"status": "failed", "message": f"Les produits suivants ne sont pas disponibles : {not_available_items}"})
```

Vérifiez que les tests sont réussis a+vec la commande suivante :

```bash
pytest 01_monolithe/tests
```

2. Les magasins de Lille ne font plus partie de la marketplace !

Merci d'enlever tous les magasins situés dans cette ville !

    Indice : la gestion des stocks et magasins se trouve dans le fichier stocks.py

Ré-exécutez les tests avec la même commande:

```bash
pytest 01_monolithe/tests
```

- Si l'un des tests échoue, pouvez-vous expliquer pourquoi?

---

## PARTIE 2

```bash
cd 01_monolithe && make start_monolithe
```

-- Grâce à Swagger, créez une commande et programmez sa livraison

Vous pouvez accéder à Swagger sur l'adresse de votre machine en utilisant l'URL suivante :

Remplacez `<ip>` par votre adresse IP

    http://<ip>:8010/docs

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