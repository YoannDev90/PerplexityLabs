import requests
import random
import string
import hashlib
import time
from bs4 import BeautifulSoup
import re

BASE_URL = "https://api.mail.tm"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def generate_random_username(length=8):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def get_domain():
    response = requests.get(f"{BASE_URL}/domains", headers=HEADERS)
    data = response.json()
    if isinstance(data, list) and data:
        return data[0]['domain']
    elif 'hydra:member' in data and data['hydra:member']:
        return data['hydra:member'][0]['domain']
    return None

def create_account():
    domain = get_domain()
    if not domain:
        print("Échec de la récupération du domaine")
        return None

    username = generate_random_username()
    password = generate_random_password()
    email = f"{username}@{domain}"

    data = {
        "address": email,
        "password": password
    }

    response = requests.post(f"{BASE_URL}/accounts", headers=HEADERS, json=data)
    
    if response.status_code in [200, 201]:
        account_info = response.json()
        account_info['password'] = password
        return account_info
    else:
        print(f"Erreur lors de la création du compte. Code: {response.status_code}")
        print(f"Réponse: {response.text}")
        return None

def get_token(email, password):
    data = {
        "address": email,
        "password": password
    }
    response = requests.post(f"{BASE_URL}/token", headers=HEADERS, json=data)
    if response.status_code == 200:
        return response.json().get('token')
    else:
        print(f"Erreur de récupération du token. Code: {response.status_code}")
        print(f"Réponse: {response.text}")
        return None

def list_messages(token):
    headers = HEADERS.copy()
    headers["Authorization"] = f"Bearer {token}"
    response = requests.get(f"{BASE_URL}/messages", headers=headers)
    data = response.json()
    if isinstance(data, list):
        return data
    elif 'hydra:member' in data:
        return data['hydra:member']
    else:
        return []

def get_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    for a_tag in soup.find_all('a', href=True):
        url = a_tag['href']
        new_content = f"{a_tag.text} [{url}]"
        a_tag.string = new_content
    text_content = soup.get_text()
    cleaned_content = re.sub(r'\s+', ' ', text_content).strip()
    return cleaned_content

def read_message(token, message_id):
    headers = HEADERS.copy()
    headers["Authorization"] = f"Bearer {token}"
    response = requests.get(f"{BASE_URL}/messages/{message_id}", headers=headers)
    if response.status_code == 200:
        details = response.json()
        if 'html' in details:
            message_text = get_text_from_html(details['html'])
        elif 'text' in details:
            message_text = details['text']
        else:
            message_text = "Contenu non disponible."
        return {
            "from": details['from']['address'],
            "subject": details['subject'],
            "content": message_text
        }
    else:
        return None

# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'un compte
    account = create_account()
    if account:
        print("Compte créé avec succès :")
        print(f"Email: {account['address']}")
        print(f"Mot de passe: {account['password']}")
        
        # Obtention du token
        token = get_token(account['address'], account['password'])
        if token:
            print(f"Token obtenu: {token}")
            
            # Listage des messages
            messages = list_messages(token)
            print("\nMessages reçus :")
            for idx, msg in enumerate(messages, 1):
                print(f"{idx}. De: {msg['from']['address']} - Sujet: {msg['subject']}")
            
            # Lecture d'un message (si des messages sont présents)
            if messages:
                message_details = read_message(token, messages[0]['id'])
                if message_details:
                    print("\nDétails du premier message :")
                    print(f"De: {message_details['from']}")
                    print(f"Sujet: {message_details['subject']}")
                    print(f"Contenu:\n{message_details['content']}")
                else:
                    print("Erreur lors de la lecture du message.")
            else:
                print("Aucun message trouvé.")
        else:
            print("Échec de l'obtention du token.")
    else:
        print("Échec de la création du compte.")
