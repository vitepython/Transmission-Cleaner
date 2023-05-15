import requests
import datetime

# Set the Transmission RPC URL
url = 'http://localhost:9091/transmission/rpc'

# Set the authentication credentials if required
username = 'your_username'  # Replace with your Transmission username
password = 'your_password'  # Replace with your Transmission password

# Set the headers for authentication and session ID
headers = {
    'Content-Type': 'application/json',
    'X-Transmission-Session-Id': '',  # Session ID will be filled later
}

# Create the request payload
payload = {
    'method': 'torrent-get',
    'arguments': {
        'fields': ['id', 'name', 'addedDate'],
    },
}

try:
    # Send the initial request to get the session ID
    response = requests.get(url, auth=(username, password))

    # Extract the session ID from the response headers
    session_id = response.headers['X-Transmission-Session-Id']
    headers['X-Transmission-Session-Id'] = session_id

    # Send the actual request to the Transmission RPC interface
    response = requests.post(url, json=payload, auth=(username, password), headers=headers)

    # Check the response status code
    if response.status_code == 200:
        # Process the response data
        data = response.json()
        torrents = data['arguments']['torrents']

        # Calculate the threshold date (one week ago)
        threshold_date = datetime.datetime.now() - datetime.timedelta(weeks=1)

        # Iterate over the torrents
        for torrent in torrents:
            added_date = datetime.datetime.fromtimestamp(torrent['addedDate'])
            if added_date < threshold_date:
                # Stop seeding the torrent
                torrent_id = torrent['id']
                stop_payload = {
                    'method': 'torrent-stop',
                    'arguments': {
                        'ids': [torrent_id],
                    },
                }
                stop_response = requests.post(url, json=stop_payload, auth=(username, password), headers=headers)
                if stop_response.status_code == 200:
                    print(f"Torrent ID {torrent_id}: Stopped seeding")
                else:
                    print(f"Error occurred while stopping torrent ID {torrent_id}: {stop_response.status_code} - {stop_response.text}")

    else:
        print(f"Error occurred: {response.status_code} - {response.text}")

except requests.exceptions.RequestException as e:
    print(f"Error occurred: {e}")
