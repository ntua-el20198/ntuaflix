import json
import click
from requests import post
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# File paths for session information
SESSION_FILE_PATH = 'session.json'

@click.group()
def cli():
    pass

def store_session_info(session_info):
    """
    Store session information in a JSON file.
    """
    with open(SESSION_FILE_PATH, 'w') as file:
        json.dump(session_info, file)

def load_session_info():
    """
    Load session information from the JSON file.
    """
    try:
        with open(SESSION_FILE_PATH, 'r') as file:
            session_info = json.load(file)
        return session_info
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        # Handle invalid JSON format
        return None
    
@cli.command()
@click.option('--username', prompt='Username', help='The username for login')
@click.option('--password', prompt=True, hide_input=True, help='The password for login')
@click.option('--format', help='The desired output format', default='json')
def login(username, password, format):
    url = 'https://127.0.0.1:9876/ntuaflix_api/login' # url from api
    data = {'username': username, 'password': password, 'format' : format}

    response = post(url, data=data, verify=False)

    if response.status_code == 200:
        session_info = response.json()
        store_session_info(session_info)
        print(session_info)
    else:
        print(f"Error: {response.status_code} - {response.text}")

@cli.command()
@click.option('--format', help='The desired output format', default='json')
def logout(format):
    session_info = load_session_info()
    print(session_info)
    if session_info:
        url = 'https://127.0.0.1:9876/ntuaflix_api/logout'
        data = {'format': format}

        response = post(url, data=data, verify=False)

        if response.status_code == 200:
            print(response.json())
            # Clear session information after successful logout
            store_session_info(None)
        else:
            print(f"Error: {response.status_code} - {response.text}")
    else:
        print("Error: No session information available. Please log in.")

# format fff
@cli.command()
@click.option('--titleID', prompt='titleID', help='The titleID for searchTitle')
@click.option('--format', help='The desired output format', default='json')
def title(titleid, format):
    url = f'https://127.0.0.1:9876/ntuaflix_api/title/{titleid}' # url from api
    data = {'format' : format}

    response = requests.get(url, data=data, verify=False)
    try:
        if response.status_code == 200:
            if format.lower() == 'json':
                try:
                    print(response.json())
                except json.decoder.JSONDecodeError as json_err:
                    print(f"Error decoding JSON: {json_err}")
            elif format.lower() == 'csv':
                print(response.text)
            else:
                print(f"Error: Invalid format specified: {format}")
        else:
            print(f"Error: {response.status_code} - {response.text}")
                
    except Exception as e:
        print(f"Error: {e}")

@cli.command()
@click.option('--titlepart', prompt='titlepart', help='The titlepart for searchTitle')
@click.option('--format', help='The desired output format', default='json')
def searchtitle(titlepart, format):
    url = 'https://127.0.0.1:9876/ntuaflix_api/searchTitle'
    params = {'titlePart': titlepart, 'format': format}

    try:
        response = requests.get(url, params=params, verify=False)
        response.raise_for_status() 

        if response.status_code == 200:
            if format.lower() == 'json':
                try:
                    print(response.json())
                except json.decoder.JSONDecodeError as json_err:
                    print(f"Error decoding JSON: {json_err}")
            elif format.lower() == 'csv':
                print(response.text)
            else:
                print(f"Error: Invalid format specified: {format}")
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"Error: {e}")

@cli.command()
@click.option('--nameID', prompt='nameID', help='The titleID for searchTitle')
@click.option('--format', help='The desired output format', default='json')
def name(nameid, format):
    url = f'https://127.0.0.1:9876/ntuaflix_api/name/{nameid}'  # URL from API
    data = {'format': format}

    response = requests.get(url, data=data, verify=False)

    try:
        if response.status_code == 200:
            if format.lower() == 'json':
                try:
                    print(response.json())
                except json.decoder.JSONDecodeError as json_err:
                    print(f"Error decoding JSON: {json_err}")
            elif format.lower() == 'csv':
                print(response.text)
            else:
                print(f"Error: Invalid format specified: {format}")
        else:
            print(f"Error: {response.status_code} - {response.text}")
                
    except Exception as e:
        print(f"Error: {e}")


@cli.command()
@click.option('--namepart', prompt='namepart', help='The titlepart for searchPrincipals')
@click.option('--format', help='The desired output format', default='json')
def searchname(namepart, format):
    url = 'https://127.0.0.1:9876/ntuaflix_api/searchname' # url from api
    params = {'namePart': namepart, 'format': format}

    response = requests.get(url, params=params, verify=False)

    try:
        if response.status_code == 200:
            if format.lower() == 'json':
                try:
                    print(response.json())
                except json.decoder.JSONDecodeError as json_err:
                    print(f"Error decoding JSON: {json_err}")
            elif format.lower() == 'csv':
                print(response.text)
            else:
                print(f"Error: Invalid format specified: {format}")
        else:
            print(f"Error: {response.status_code} - {response.text}")
                
    except Exception as e:
        print(f"Error: {e}")
        
if __name__ == '__main__':
    cli()