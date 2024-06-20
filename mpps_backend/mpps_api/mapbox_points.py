import json
import requests

# Your Mapbox API token
MAPBOX_API_TOKEN = 'pk.eyJ1IjoiZWRzb25hZXJvIiwiYSI6ImNsc3lvbmI1bjBlY2syam9lMnh4ZDh0M3QifQ.qwA-N7LelcYG224oesajOQ'

def update_location_coordinates(filename):
    """
    This function iterates through a JSON file containing location data,
    retrieves coordinates using Mapbox Geocoding API, and updates the file.

    Args:
        filename (str): Name of the JSON file containing location data.
    """

    # Read existing data from the file
    with open(filename, "r") as f:
        data = json.load(f)

    # Prepare base URL for Mapbox Geocoding API
    geocoding_url = "https://api.mapbox.com/geocoding/v5/{endpoint}/{query}.json?access_token={token}"

    # Loop through each route in the data
    for route in data:
        for point in route.get("points", []):
            location = point.get("name")

            if not location:
                print(f"Missing location name for point: {point}")
                continue

            # Build the API request URL
            url = geocoding_url.format(endpoint="mapbox.places", query=location, token=MAPBOX_API_TOKEN)

            # Send request to Mapbox API
            response = requests.get(url)

            if response.status_code == 200:
                # Extract coordinates from response (assuming successful geocoding)
                response_data = response.json()
                if response_data["features"]:
                    coordinates = response_data["features"][0]["geometry"]["coordinates"]
                    longitude, latitude = coordinates

                    # Update coordinates in the data structure
                    point["lng"] = longitude
                    point["lat"] = latitude
                else:
                    print(f"No features found for {location}")
            else:
                print(f"Error retrieving coordinates for {location}: {response.status_code}")

    # Write updated data back to the file
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    # Print confirmation message
    print(f"Successfully updated coordinates in {filename}")

# Example usage (replace with your filename)
filename = "routes.json"

update_location_coordinates(filename)
