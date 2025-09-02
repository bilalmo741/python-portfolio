# earthquake_data_fetcher.py
# Python project: Fetch and display real-time earthquake data with approximate locations

import requests
import json

# Your OpenCage API key
opencagekey = "97e98947bfaa450bb5de67f734ef4d93"

# Fetch recent earthquake data from USGS
response = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson")

if response:
    data = response.json()
    earthquake_data = data["features"]

    for quake in earthquake_data:
        # Extract earthquake magnitude
        magnitude = quake["properties"]["mag"]

        # Extract coordinates
        coordinates = quake["geometry"]["coordinates"]
        longitude, latitude = coordinates[0], coordinates[1]

        # Extract time in epoch milliseconds and convert to seconds
        quaketime_ms = quake["properties"]["time"]
        quaketime_sec = quaketime_ms / 1000
        readabletime = f"{quaketime_sec} seconds since epoch"  # Can format further if desired

        # Print earthquake basic info
        print(f"Earthquake of magnitude {magnitude} occurred at {longitude}, {latitude} on time {readabletime}.")

        # Get approximate location from OpenCage API
        location_response = requests.get(
            f"https://api.opencagedata.com/geocode/v1/json?q={latitude},{longitude}&key={opencagekey}"
        )
        if location_response:
            location_data = location_response.json()
            if location_data["results"]:
                location = location_data["results"][0]["formatted"]
                print(f"Location: {location}")
            else:
                print("Location not found.")
        else:
            print("Error connecting to OpenCage API.")
else:
    print("Error connecting to USGS API.")
