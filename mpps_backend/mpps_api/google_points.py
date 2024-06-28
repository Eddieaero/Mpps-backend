# import json
# import requests


# # Your Google Maps API key
# GOOGLE_MAPS_API_KEY = 'AIzaSyAtl70uE3wOpmFMGgEjN2KdsGwwUM8Rl_k'

# def update_location_coordinates(filename):
#     """
#     This function iterates through a JSON file containing location data,
#     retrieves coordinates using Google Maps Geocoding API, and updates the file.

#     Args:
#         filename (str): Name of the JSON file containing location data.
#     """

#     # Read existing data from the file
#     with open(filename, "r") as f:
#         data = json.load(f)

#     # Prepare base URL for Google Maps Geocoding API
#     geocoding_url = "https://maps.googleapis.com/maps/api/geocode/json"

#     # Loop through each route in the data
#     for route in data:
#         for point in route.get("points", []):
#             location = point.get("name")

#             if not location:
#                 print(f"Missing location name for point: {point}")
#                 continue

#             # Build the API request URL
#             params = {
#                 'address': location,
#                 'key': GOOGLE_MAPS_API_KEY
#             }
#             response = requests.get(geocoding_url, params=params)

#             if response.status_code == 200:
#                 # Extract coordinates from response (assuming successful geocoding)
#                 response_data = response.json()
#                 if response_data["results"]:
#                     coordinates = response_data["results"][0]["geometry"]["location"]
#                     longitude = coordinates["lng"]
#                     latitude = coordinates["lat"]

#                     # Update coordinates in the data structure
#                     point["lng"] = longitude
#                     point["lat"] = latitude
#                 else:
#                     print(f"No results found for {location}")
#             else:
#                 print(f"Error retrieving coordinates for {location}: {response.status_code}")

#     # Write updated data back to the file
#     with open(filename, "w") as f:
#         json.dump(data, f, indent=4)

#     # Print confirmation message
#     print(f"Successfully updated coordinates in {filename}")

# # Example usage (replace with your filename)
# filename = "routes.json"

# update_location_coordinates(filename)




# import json
# import requests
# import random

# Your Google Maps API key
#

# def update_location_coordinates(filename):
#     """
#     This function iterates through a JSON file containing location data,
#     retrieves coordinates using Google Maps Geocoding API, and updates the file.
#     It ensures that all locations are based in Tanzania.

#     Args:
#         filename (str): Name of the JSON file containing location data.
#     """

#     # Read existing data from the file
#     with open(filename, "r") as f:
#         data = json.load(f)

#     # Prepare base URL for Google Maps Geocoding API
#     geocoding_url = "https://maps.googleapis.com/maps/api/geocode/json"

#     # Loop through each route in the data
#     for route in data:
#         for point in route.get("points", []):
#             location = point.get("name")

#             if not location:
#                 print(f"Missing location name for point: {point}")
#                 continue

#             # Build the API request URL
#             params = {
#                 'address': location,
#                 'key': GOOGLE_MAPS_API_KEY
#             }
#             response = requests.get(geocoding_url, params=params)

#             if response.status_code == 200:
#                 # Extract coordinates and address components from response
#                 response_data = response.json()
#                 if response_data["results"]:
#                     address_components = response_data["results"][0]["address_components"]
#                     country = next((component for component in address_components if "country" in component["types"]), None)

#                     # Check if the country is Tanzania
#                     if country and country["short_name"] == "TZ":
#                         coordinates = response_data["results"][0]["geometry"]["location"]
#                         longitude = coordinates["lng"]
#                         latitude = coordinates["lat"]

#                         # Update coordinates in the data structure
#                         point["lng"] = longitude
#                         point["lat"] = latitude
#                     else:
#                         print(f"Location {location} is not in Tanzania.")
#                 else:
#                     print(f"No results found for {location}")
#             else:
#                 print(f"Error retrieving coordinates for {location}: {response.status_code}")

#     # Write updated data back to the file
#     with open(filename, "w") as f:
#         json.dump(data, f, indent=4)

#     # Print confirmation message
#     print(f"Successfully updated coordinates in {filename}")



# def assign_manual_coordinates(filename):
#         """
#         This function manually assigns coordinates for specific locations
#         in the JSON file containing location data.

#         Args:
#             filename (str): Name of the JSON file containing location data.
#         """

#     # Define the manual coordinates for specific locations
#         manual_coordinates = {
#             "Makwawa": {"lng": 35.68604, "lat": -7.76801},
#             "Nata": {"lng": 33.17641, "lat": -4.09762},
#             "Tinde": {"lng": 33.19647, "lat": -3.87030},
#             "Lukungu": {"lng": 33.857887, "lat": -2.230296},
#             "Ruaha Mbuyuni": {"lng": 36.43820, "lat": -7.52170},
#             "Manga": {"lng": 38.24019, "lat": -5.90794},
#             "Maweni": {"lng": 39.01726, "lat": -5.10005},
#             "Nyigo": {"lng": 34.87937, "lat": -8.77533},
#             "Igawisenga": {"lng": 35.31413, "lat": -9.69752},
#             "Nundu": {"lng": 34.75872, "lat": -9.36792},
#             "Mitawa": {"lng": 34.89123, "lat": -11.12573},
#             "Lumecha": {"lng": 35.77091, "lat": -10.57888},
#             "Sauti Moja": {"lng": 38.05540, "lat": -10.84988},
#             "Nyangoa": {"lng": 39.29458, "lat": -10.32237},
#             "Tunko": {"lng": 32.10122, "lat": -8.65505},
#             "Kanondo": {"lng": 31.56980, "lat": -7.91246},
#             "Lyazumbi": {"lng": 31.03690, "lat": -7.24181},
#             "Ipole": {"lng": 32.71232, "lat": -5.78968}
#         }

#         # Read existing data from the file
#         with open(filename, "r") as f:
#             data = json.load(f)

#         # Loop through each route in the data
#         for route in data:
#             for point in route.get("points", []):
#                 point["code"] = str(random.randint(1000, 9999))
#                 location = point.get("name")

#                 if location in manual_coordinates:
#                     # Update coordinates in the data structure
#                     point["lng"] = manual_coordinates[location]["lng"]
#                     point["lat"] = manual_coordinates[location]["lat"]

#         # Write updated data back to the file
#         with open(filename, "w") as f:
#             json.dump(data, f, indent=4)

#         # Print confirmation message
#         print(f"Successfully updated coordinates in {filename}")


# def extract_start_end(filename, output_filename):
#     """
#     This function extracts "start" and "end" keywords from a JSON file
#     and writes them into a new JSON file.

#     Args:
#         filename (str): Name of the input JSON file containing location data.
#         output_filename (str): Name of the output JSON file.
#     """

#     # Read existing data from the file
#     with open(filename, "r") as f:
#         data = json.load(f)

#     # Prepare a list to store the extracted data
#     points = []

#     # Loop through each route in the data
#     for route in data:
#          for point in route.get("points", []):
#              point.pop('id', None)
#              points.append(point)

    
#     unique_points = list({point['name']: point for point in points}.values())

#     # Write extracted data to the new file
#     with open(output_filename, "w") as f:
#             json.dump(list(unique_points), f, indent=4)

#     # Print confirmation message
#     print(f"Successfully extracted unique points into {output_filename}")

# # Example usage (replace with your filenames)
# input_filename = "routes.json"
# output_filename = "points.json"
# output_filename = "Location_points.json"


# # Example usage (replace with your filename)
# filename = "routes.json"

# # assign_manual_coordinates(filename)
# # update_location_coordinates(filename)
# extract_start_end(input_filename, output_filename)





# def extract_location(filename, output_filename):

#     with open(filename, "r") as f:
#         data = json.load(f)

#         locations = []
#         for route in data.get("start", "end"):
#             locations.append(route)

#         # single_locations = list({location['name']: location for location in locations}.values())

#         with open('points.json', 'w') as file:
#             json.dump(locations, file)
              
#         print(locations)

# filename = "routes.json"
# output_filename = "Location_points.json"
# extract_location(filename, output_filename)


import requests
import json

def add_region_and_coordinates(file, GOOGLE_MAPS_API_KEY):
    with open(file, 'r') as f:
        data = json.load(f)

    destinations = data[0]['destination']

    for destination in destinations:
        response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={destination["name"]}, Tanzania&key={GOOGLE_MAPS_API_KEY}')
        result = response.json()

        if result['status'] == 'OK':
            location = result['results'][0]['geometry']['location']
            address_components = result['results'][0]['address_components']
            for component in address_components:
                if 'administrative_area_level_1' in component['types']:
                    destination['region'] = component['long_name']
            destination['coordinates'] = {'lng': location['lng'], 'lat': location['lat']}   

    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

add_region_and_coordinates('points.json', GOOGLE_MAPS_API_KEY)