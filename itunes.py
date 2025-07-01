import json
import requests
import sys

#if len(sys.argv) != 2:
 #   sys.exit()
key = input("enter a song title: ")
response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + key)

o = response.json()
for result in o['results']:
    print(result['artistName'], result['trackName'], result['collectionName'], result['releaseDate'])
    """print("Artist Name:", result['artistName'])
    print("Album Name:", result['collectionName'])
    print("Release Date:", result['releaseDate'])
    print("Track Price:", result['trackPrice'])
    print("Collection Price:", result['collectionPrice'])
    print("Track Time:", result['trackTimeMillis'])
    print("Country:", result['country'])
    print("Currency:", result['currency'])"""
 