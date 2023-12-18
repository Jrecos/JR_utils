import requests
import base64
import json

def get_users_list(token, environment):
    """
    Retrieve the list of users using the service account token.

    Parameters:
    token (str): The service account token.
    environment (str): The Talend Cloud environment (e.g., 'us', 'eu').

    Returns:
    list: The list of users.
    """
    users_url = f"https://api.{environment}.cloud.talend.com/account/users"  # Update with actual endpoint
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(users_url, headers=headers)

    if response.status_code == 200:
        return response.json()  # Adjust this based on the actual response format
    else:
        raise Exception(f"Error retrieving users: {response.status_code} {response.text}")


def generate_service_account_token(client_id, client_secret, environment):
    token_url = f"https://api.{environment}.cloud.talend.com/security/oauth/token"
    audience = f"https://api.{environment}.cloud.talend.com"
    print("Audience:", audience)
    print("Client ID:", token_url)
    credentials = f"{client_id}:{client_secret}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    print("Encoded Credentials:", encoded_credentials)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {encoded_credentials}"
    }
    body = {
        "audience": audience,
        "grant_type": "client_credentials"
    }

    response = requests.post(token_url, headers=headers, json=body)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error generating token: {response.status_code} {response.text} {response.content}")


client_id = "DML2k3X-SK2-aYhw_jovDat0MhQ1IbWAlgMRmZJZCZo"
client_secret = "ktuvHUHMJgRtht_q-dxxRrLndpPqRGwq8gOokr9WOQcLSFG2TI5sHh-iYIM-95nb"
environment = "us"

try:
    token = generate_service_account_token(client_id, client_secret, environment)
    print("Service Account Token:", token)

    # Retrieve and print the list of users
    users = get_users_list(token, environment)
    print("List of Users:", users)
except Exception as e:
    print(str(e))