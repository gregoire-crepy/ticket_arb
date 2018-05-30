import ticketmaster_client as tc
import json
import pandas as pd
import os

tc = os.environ['ticketmaster_api_key']
venue_data = json.loads(tc.executeQuery('venues',"""geoPoint=9q8yy&radius=50"""))
df_venue_data = pd.DataFrame(data['_embedded']['venues'])