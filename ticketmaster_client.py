import requests

class ApiClient:
	 base_url = 'https://app.ticketmaster.com'
	 query_type_dict = {'venues':'/discovery/v2/venues.json?'}
	 def __init__(self, api_key):
	 	self.api_key = api_key
	 def executeQuery(self,query_type, param_string):
	 	query_type_url = self.query_type_dict[query_type]
	 	request_url = self.base_url + query_type_url + param_string + '&apikey=' + self.api_key
	 	r = requests.get(request_url)
	 	print(request_url)
	 	print(r.text)
	 	return(r.text)