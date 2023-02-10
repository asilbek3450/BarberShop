url = 'https://goo.gl/maps/iALSiTvR5SpmZHm27'

# Split the URL
url_parts = url.split('=')

# Get the parameters
params = url_parts[1].split(',')

# Get the longitude and latitude
longitude = params[0]
latitude = params[1]

print(longitude, latitude)