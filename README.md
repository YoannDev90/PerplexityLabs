# Perplexity AI Python Library

## Description

Cette bibliothèque Python offre une interface simple et puissante pour interagir avec l'IA Perplexity. Elle combine les fonctionnalités de deux projets open-source existants, offrant ainsi une solution complète pour l'utilisation de Perplexity AI dans vos projets Python.

## Fonctionnalités

- Interaction avec l'API Perplexity pour poser des questions et obtenir des réponses
- Création et gestion de comptes utilisateurs
- Authentification sécurisée
- Gestion des sessions
- Traitement avancé des réponses

## Installation

Pour installer la bibliothèque, utilisez pip :

```bash
pip install perplexity-ai-python
```
## Configuration requise

    Python 3.7+
    Connexion Internet stable

# Utilisation rapide
## Initialisation du client

```python
from perplexity_ai import PerplexityClient

client = PerplexityClient()
```

## Création d'un compte

```python
client.create_account("votre_email@example.com", "votre_mot_de_passe")
```
## Connexion

```python
client.login("votre_email@example.com", "votre_mot_de_passe")
```
## Poser une question

```python
response = client.ask("Quelle est la capitale de la France ?")
print(response)
```

# Fonctionnalités détaillées
## PerplexityClient
La classe principale pour interagir avec l'API Perplexity.
### Méthodes

    __init__(token=None): Initialise le client. Un token peut être fourni pour une authentification immédiate.
    create_account(email, password): Crée un nouveau compte utilisateur.
    login(email, password): Connecte l'utilisateur et récupère un token d'authentification.
    ask(query, **kwargs): Envoie une requête à Perplexity et retourne la réponse.
    logout(): Déconnecte l'utilisateur et invalide le token.

### Module d'authentification
Gère les processus d'authentification et de création de compte.
Fonctions

    create_account(email, password): Crée un nouveau compte.
    login(email, password): Authentifie l'utilisateur et retourne un token.
    validate_token(token): Vérifie la validité d'un token.

### Utilitaires
Fonctions auxiliaires pour le traitement des données et la gestion des erreurs.
Exemples d'utilisation avancée
Utilisation avec des paramètres personnalisés

```python
response = client.ask("Résumez l'histoire de la France", 
                      max_tokens=500, 
                      temperature=0.7)
```

### Gestion des erreurs

```python
try:
    response = client.ask("Une question complexe")
except PerplexityAPIError as e:
    print(f"Une erreur est survenue : {e}")
```
## Contribution
Les contributions à ce projet sont les bienvenues ! Voici comment vous pouvez contribuer :

    Forkez le dépôt
    Créez votre branche de fonctionnalité (git checkout -b feature/AmazingFeature)
    Committez vos changements (git commit -m 'Add some AmazingFeature')
    Poussez vers la branche (git push origin feature/AmazingFeature)
    Ouvrez une Pull Request

## Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
### Contact

Yoann - yoanndev@outlook.fr

Lien du projet : https://github.com/YoannDev90/PerplexityLabs

## Remerciements

    nathanrchn/perplexityai
    helallao/perplexity-ai