import requests
  
# api-endpoint
URL = "https://api.nasa.gov/planetary/apod"
  
# location given here
location = "delhi technological university"
  
# defining a params dict for the parameters to be sent to the API
# PARAMS = {'address':location}
  
# sending get request and saving the response as response object
r = requests.get(url = URL)
  
# extracting data in json format
data = r.json()