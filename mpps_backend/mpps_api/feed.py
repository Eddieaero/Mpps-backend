# import json


# def trim_data(tz_regions_json, trim_json):
#     with open(tz_regions_json, 'r') as f:
#         data = json.load(f)
    
#     trimmed_data = []
#     for item in data:
#         trimmed_item = {
#             'city': item.get('city'),
#             'lng': item.get('lng'),
#             'lat': item.get('lat'),
#             'admin_name': item.get('admin_name')
#         }
#         trimmed_data.append(trimmed_item)
    
#     with open(trim_json, 'w') as f:
#         json.dump(trim_json, f)

# trim_data('tz_regions.json', 'trim.json')


import json

def trim_json_data(json_data, input_file="tz_regions.json", output_file="trimmed.json"):
# def trim_json_data(input_file="tz_regions.json", output_file="trimmed.json"):
  """
  Trims data from a JSON string, keeping only city, lng, lat, and admin_name.
  Writes the trimmed data to a new JSON file.

  Args:
      data_string: The JSON data string to be trimmed.
      input_file (str, optional): The filename of the input JSON file (default: "tz_regions.json").
      output_file (str, optional): The filename of the output JSON file (default: "trimmed.json").
  """

  # Parse the JSON string
  data = json.loads(json_data)

  # Trim each item in the data
  trimmed_data = []
  for item in data:
    trimmed_item = {
      "city": item.get("city"),
      "lng": item.get("lng"),
      "lat": item.get("lat"),
      "admin_name": item.get("admin_name"),
    }
    trimmed_data.append(trimmed_item)

  # Write the trimmed data to a new JSON file
  with open(output_file, 'w') as f:
    json.dump(trimmed_data, f)

# Example usage with the provided JSON string
json_data = [
  {
    "city": "Dar es Salaam", 
    "lat": "-6.8161", 
    "lng": "39.2803", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Dar es Salaam", 
    "capital": "admin", 
    "population": "7962000", 
    "population_proper": "4364541"
  }, 
  {
    "city": "Mwanza", 
    "lat": "-2.5167", 
    "lng": "32.9000", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Mwanza", 
    "capital": "admin", 
    "population": "1104521", 
    "population_proper": "706453"
  }, 
  {
    "city": "Ubungo", 
    "lat": "-6.7889", 
    "lng": "39.2056", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Dar es Salaam", 
    "capital": "", 
    "population": "1086912", 
    "population_proper": "1086912"
  }, 
  {
    "city": "Mbeya", 
    "lat": "-8.9000", 
    "lng": "33.4500", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Mbeya", 
    "capital": "admin", 
    "population": "541603", 
    "population_proper": "541603"
  }, 
  {
    "city": "Arusha", 
    "lat": "-3.3667", 
    "lng": "36.6833", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Arusha", 
    "capital": "admin", 
    "population": "416442", 
    "population_proper": "416442"
  }, 
  {
    "city": "Uvinza", 
    "lat": "-5.1069", 
    "lng": "30.3839", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Kigoma", 
    "capital": "", 
    "population": "387442", 
    "population_proper": "387442"
  }, 
  {
    "city": "Geita", 
    "lat": "-2.8714", 
    "lng": "32.2294", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Geita", 
    "capital": "admin", 
    "population": "318006", 
    "population_proper": "318006"
  }, 
  {
    "city": "Sumbawanga", 
    "lat": "-7.9667", 
    "lng": "31.6167", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Rukwa", 
    "capital": "admin", 
    "population": "303986", 
    "population_proper": "147483"
  }, 
  {
    "city": "Kibaha", 
    "lat": "-6.7667", 
    "lng": "38.9167", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Coast", 
    "capital": "admin", 
    "population": "265360", 
    "population_proper": "23050"
  }, 
  {
    "city": "Bariadi", 
    "lat": "-2.7919", 
    "lng": "33.9894", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Simiyu", 
    "capital": "admin", 
    "population": "260927", 
    "population_proper": "260927"
  }, 
  {
    "city": "Kahama", 
    "lat": "-3.8375", 
    "lng": "32.6000", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Shinyanga", 
    "capital": "", 
    "population": "242208", 
    "population_proper": "242208"
  }, 
  {
    "city": "Kasulu", 
    "lat": "-4.5800", 
    "lng": "30.1000", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Kigoma", 
    "capital": "", 
    "population": "238321", 
    "population_proper": "234452"
  }, 
  {
    "city": "Tabora", 
    "lat": "-5.0167", 
    "lng": "32.8000", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Tabora", 
    "capital": "admin", 
    "population": "221466", 
    "population_proper": "127880"
  }, 
  {
    "city": "Zanzibar", 
    "lat": "-6.1650", 
    "lng": "39.1990", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Zanzibar Urban/West", 
    "capital": "admin", 
    "population": "219007", 
    "population_proper": "219007"
  }, 
  {
    "city": "Morogoro", 
    "lat": "-6.8242", 
    "lng": "37.6633", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Morogoro", 
    "capital": "admin", 
    "population": "207000", 
    "population_proper": "207000"
  }, 
  {
    "city": "Ifakara", 
    "lat": "-8.1000", 
    "lng": "36.6833", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Morogoro", 
    "capital": "", 
    "population": "205843", 
    "population_proper": "205843"
  }, 
  {
    "city": "Mpanda", 
    "lat": "-6.3500", 
    "lng": "31.0667", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Katavi", 
    "capital": "admin", 
    "population": "204338", 
    "population_proper": "204338"
  }, 
  {
    "city": "Iringa", 
    "lat": "-7.7700", 
    "lng": "35.6900", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Iringa", 
    "capital": "admin", 
    "population": "202490", 
    "population_proper": "202490"
  }, 
  {
    "city": "Singida", 
    "lat": "-4.8167", 
    "lng": "34.7500", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Singida", 
    "capital": "admin", 
    "population": "165492", 
    "population_proper": "29258"
  }, 
  {
    "city": "Bukoba", 
    "lat": "-1.3333", 
    "lng": "31.8167", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Kagera", 
    "capital": "admin", 
    "population": "144938", 
    "population_proper": "144938"
  }, 
  {
    "city": "Moshi", 
    "lat": "-3.3349", 
    "lng": "37.3404", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Kilimanjaro", 
    "capital": "admin", 
    "population": "144739", 
    "population_proper": "144739"
  }, 
  {
    "city": "Kigoma", 
    "lat": "-4.8833", 
    "lng": "29.6333", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Kigoma", 
    "capital": "admin", 
    "population": "135234", 
    "population_proper": "135234"
  }, 
  {
    "city": "Tarime", 
    "lat": "-1.3500", 
    "lng": "34.3833", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Mara", 
    "capital": "", 
    "population": "133043", 
    "population_proper": "133043"
  }, 
  {
    "city": "Nzega", 
    "lat": "-4.2169", 
    "lng": "33.1864", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Tabora", 
    "capital": "", 
    "population": "125193", 
    "population_proper": "125193"
  }, 
  {
    "city": "Handeni", 
    "lat": "-5.4242", 
    "lng": "38.0194", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Tanga", 
    "capital": "", 
    "population": "108968", 
    "population_proper": "108968"
  }, 
  {
    "city": "Shinyanga", 
    "lat": "-3.6619", 
    "lng": "33.4231", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Shinyanga", 
    "capital": "admin", 
    "population": "107362", 
    "population_proper": "107362"
  }, 
  {
    "city": "Musoma", 
    "lat": "-1.5000", 
    "lng": "33.8000", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Mara", 
    "capital": "admin", 
    "population": "103497", 
    "population_proper": "103497"
  }, 
  {
    "city": "Tanga", 
    "lat": "-5.0742", 
    "lng": "39.0992", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Tanga", 
    "capital": "admin", 
    "population": "103399", 
    "population_proper": "103399"
  }, 
  {
    "city": "Songea", 
    "lat": "-10.6833", 
    "lng": "35.6500", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Ruvuma", 
    "capital": "admin", 
    "population": "99961", 
    "population_proper": "99961"
  }, 
  {
    "city": "Mtwara", 
    "lat": "-10.2736", 
    "lng": "40.1828", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Mtwara", 
    "capital": "admin", 
    "population": "92602", 
    "population_proper": "92602"
  }, 
  {
    "city": "Tukuyu", 
    "lat": "-9.2500", 
    "lng": "33.6500", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Mbeya", 
    "capital": "", 
    "population": "50000", 
    "population_proper": "50000"
  }, 
  {
    "city": "Chake Chake", 
    "lat": "-5.2395", 
    "lng": "39.7700", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Pemba South", 
    "capital": "admin", 
    "population": "49959", 
    "population_proper": "49959"
  }, 
  {
    "city": "Dodoma", 
    "lat": "-6.1731", 
    "lng": "35.7419", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Dodoma", 
    "capital": "primary", 
    "population": "45807", 
    "population_proper": "45807"
  }, 
  {
    "city": "Kilosa", 
    "lat": "-6.8300", 
    "lng": "36.9875", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Morogoro", 
    "capital": "", 
    "population": "43418", 
    "population_proper": "43418"
  }, 
  {
    "city": "Lindi", 
    "lat": "-9.9969", 
    "lng": "39.7144", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Lindi", 
    "capital": "admin", 
    "population": "41549", 
    "population_proper": "41549"
  }, 
  {
    "city": "Njombe", 
    "lat": "-9.3333", 
    "lng": "34.7667", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Njombe", 
    "capital": "admin", 
    "population": "40607", 
    "population_proper": "40607"
  }, 
  {
    "city": "Tunduma", 
    "lat": "-9.3000", 
    "lng": "32.7667", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Mbeya", 
    "capital": "", 
    "population": "36556", 
    "population_proper": "36556"
  }, 
  {
    "city": "Masasi", 
    "lat": "-10.7296", 
    "lng": "38.7999", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Mtwara", 
    "capital": "", 
    "population": "36032", 
    "population_proper": "36032"
  }, 
  {
    "city": "Magu", 
    "lat": "-2.5833", 
    "lng": "33.4333", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Mwanza", 
    "capital": "", 
    "population": "35000", 
    "population_proper": "35000"
  }, 
  {
    "city": "Babati", 
    "lat": "-4.2167", 
    "lng": "35.7500", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Manyara", 
    "capital": "admin", 
    "population": "30975", 
    "population_proper": "30975"
  }, 
  {
    "city": "Chato", 
    "lat": "-2.6378", 
    "lng": "31.7669", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Geita", 
    "capital": "", 
    "population": "27776", 
    "population_proper": "27776"
  }, 
  {
    "city": "Wete", 
    "lat": "-5.0567", 
    "lng": "39.7281", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Pemba North", 
    "capital": "admin", 
    "population": "26450", 
    "population_proper": "26450"
  }, 
  {
    "city": "Biharamulo", 
    "lat": "-2.6333", 
    "lng": "31.3167", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Kagera", 
    "capital": "", 
    "population": "24573", 
    "population_proper": "24573"
  }, 
  {
    "city": "Itigi", 
    "lat": "-5.7000", 
    "lng": "34.4833", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Singida", 
    "capital": "", 
    "population": "24000", 
    "population_proper": "24000"
  }, 
  {
    "city": "Mkokotoni", 
    "lat": "-5.8800", 
    "lng": "39.2731", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Zanzibar North", 
    "capital": "minor", 
    "population": "2572", 
    "population_proper": "2572"
  }, 
  {
    "city": "Mahonda", 
    "lat": "-5.9897", 
    "lng": "39.2519", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Zanzibar North", 
    "capital": "admin", 
    "population": "", 
    "population_proper": ""
  }, 
  {
    "city": "Vwawa", 
    "lat": "-9.1081", 
    "lng": "32.9347", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Songwe", 
    "capital": "admin", 
    "population": "", 
    "population_proper": ""
  }, 
  {
    "city": "Koani", 
    "lat": "-6.1333", 
    "lng": "39.2833", 
    "country": "Tanzania", 
    "iso2": "TZ", 
    "admin_name": "Zanzibar Central/South", 
    "capital": "admin", 
    "population": "", 
    "population_proper": ""
  }
]
  # Replace "..." with your actual JSON string
trim_json_data(json_data)

