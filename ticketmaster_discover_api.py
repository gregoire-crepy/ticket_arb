from ticketmaster_extract_functions import safeget, extract_event_info
import ticketmaster_client as tc
import json
import os
import pandas as pd

tc_client = tc.ApiClient(os.environ['ticketmaster_api_key'])
# Gets 100 venues in 50 miles radius from SF
venue_param_str="""geoPoint=9q8yy&radius=50&size=100"""
venue_data = json.loads(tc_client.executeQuery('discovery_venues', venue_param_str))
df_venue_data = pd.DataFrame(venue_data['_embedded']['venues'])
columns_event_data=['venue_id',
                    'event_id',
                    'event_name',
                    'currency',
                    'min_price',
                    'max_price',
                    'segment',
                    'genre',
                    'date',
                    'date_time']

df_events=pd.DataFrame(columns=columns_event_data)

# Loops on each venue and retrieves events
for venue_id in df_venue_data['id'].values:
    print(venue_id)
    # Initializes the Event df for this venue
    df_event_extracted_temp=pd.DataFrame(columns=columns_event_data)
    # Retrieves 100 events events
    param_str = "venueId={0}".format(venue_id) + "&size=100"
    event_data = json.loads(tc_client.executeQuery('discovery_events', param_str))
    events=safeget(event_data, '_embedded', 'events')
    if events is not None:
        df_event_data_temp = pd.DataFrame(events)
        df_event_extracted_temp[columns_event_data[1:]]= df_event_data_temp.apply(lambda row: extract_event_info(row),
                                                         axis=1)
        df_event_extracted_temp['venue_id'] = venue_id
        df_events = df_events.append(df_event_extracted_temp, ignore_index=True)


event_id='G5vYZ4al6bF94'
event_param_str="/" + event_id + "/offers.json?"
commerce_events_data = json.loads(tc_client.executeQuery('commerce_events', event_param_str))
print(commerce_events_data)


# Print events extracted for all venues
df_events.to_csv('events_extracted', sep=',', encoding='utf-8')



## QA
# venue_id = 'KovZpZAa1JaA'
# # Initializes the Event df for this venue
# df_event_extracted_temp = pd.DataFrame(columns=columns_event_data)
#
# # Retrieves 100 events events
# param_str = "venueId={0}".format(venue_id) + "&size=100"
# event_data = json.loads(tc_client.executeQuery('discovery_events', param_str))
# events = safeget(event_data, '_embedded', 'events')
# if events is not None:
#     df_event_data_temp = pd.DataFrame(events)
#     print(df_event_extracted_temp)
#     df_event_extracted_temp[columns_event_data[1:]] = df_event_data_temp.apply(lambda row: extract_event_info(row),
#                                                                                axis=1)

    #df_events = df_events.append(df_event_extracted_temp, ignore_index=True)
# venue_id='KovZpZAJelvA'
# param_str = "venueId={0}".format(venue_id) + "&size=100"
# event_data = json.loads(tc_client.executeQuery('events', param_str))
# df_event_data_temp = pd.DataFrame(event_data['_embedded']['events'])
# for i in xrange(df_event_data_temp.shape[0]):
#       row=df_event_data_temp.iloc[i]
#       print(row['dates'])
#       print(extract_event_info(row, venue_id))
