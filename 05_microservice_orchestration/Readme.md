

## Orchestration avec Docker-compose :

1. Créer 4 images pour les 4 microservices avec les tags suivants:
 
   - Microservice Stock : `stock:0.0.1`
   - Microservice Payment : `payment:0.0.1`
   - Microservice Deliver : `deliver:0.0.1`
   - Microservice Order : `order:0.0.1`

2. Compléter le fichier `docker-compose.yml`.

   Exemple : https://github.com/docker/awesome-compose/blob/master/official-documentation-samples/django/README.md

3. Exécuter la commande :

 ```bash
 docker-compose -f docker-compose.yml up
 ```