# Transmission-Cleaner
Transmission Cleaner is a Python script that interacts with the Transmission BitTorrent client's remote procedure call (RPC) interface to stop seeding torrents that were added more than a week ago.

Requirements:
- Python 3.x
- requests library (install dependencies from requirements.txt)

Installation:
1. Clone this repository:
   git clone https://github.com/your-username/transmission-cleaner.git

2. Install the dependencies:
   pip install -r requirements.txt

Configuration:
Before running the script, make sure to configure the Transmission RPC connection:
1. On first run it will attempt to create a transmission-cleaner.conf
2. Enter your Transmission username, password, and RPC URL.
3. If creating transmission-cleaner.conf fails, then transmission-cleaner.conf in a text editor.

Usage:
Run the script using the following command:
python Transmission-Cleaner.py

The script will connect to the Transmission RPC interface, retrieve a list of torrents, and stop seeding torrents that were added more than a week ago.

Contributing:
Contributions are welcome! If you have any suggestions, bug fixes, or new features, please open an issue or submit a pull request.

License:
This project is licensed under the MIT License. See the LICENSE file for details.
