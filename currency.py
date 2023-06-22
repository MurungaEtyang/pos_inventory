import geocoder
from forex_python.converter import CurrencyCodes

def get_currency(country_code):
    currency = CurrencyCodes()
    country_currency = currency.get_currency_name(country_code)
    return country_currency

# Get current location
g = geocoder.ip('me')
country_code = g.country

# Get currency based on country code
country_currency = get_currency(country_code)
print(f"The currency of {country_code} is {country_currency}")
