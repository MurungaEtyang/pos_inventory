import phonenumbers
from geocoder import ipinfo # geocoder's geolocation service

# Get current location
g = ipinfo.ipinfo()
country_code = g.country_code

# Get country phone code
country_phone_code = phonenumbers.country_code_for_region(country_code)

print(f"The phone code for {country_code} is +{country_phone_code}")
