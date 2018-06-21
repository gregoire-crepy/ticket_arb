import requests

class ApiClient:
    base_url = 'https://app.ticketmaster.com'
    query_type_dict = {'discovery_venues': '/discovery/v2/venues.json?',
					   'discovery_events': '/discovery/v2/events.json?',
					   'commerce_events': '/commerce/v2/events',
					   }

    def __init__(self, api_key):
        self.api_key = api_key

    def executeQuery(self, query_type, param_string):
        query_type_url = self.query_type_dict[query_type]
        request_url = self.base_url + query_type_url + param_string + '&apikey=' + self.api_key
        r = requests.get(request_url)
        return (r.text)
