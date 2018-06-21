import pandas as pd



def safeget(dct, *keys):
    for key in keys:
        try:
            dct = dct[key]
        except KeyError:
            return None
    return dct

def extract_event_info(row):
    event_id = row['id']
    event_name = row['name']
    currency = None
    min_price = None
    max_price = None
    segment = None
    genre = None
    date = None
    date_time = None

    if 'priceRanges' in row.keys():
        if type(row['priceRanges'])==list:
            if len(row['priceRanges'])==1:
                temp_dict=row['priceRanges'][0]
                currency=safeget(temp_dict, 'currency')
                min_price = safeget(temp_dict, 'min')
                max_price = safeget(temp_dict, 'max')

    if 'classifications' in row.keys():
        if type(row['classifications']) == list:
            if len(row['classifications']) == 1:
                temp_dict=dict(row['classifications'][0])
                segment = safeget(temp_dict, 'segment', 'name')
                genre = safeget(temp_dict, 'genre', 'name')

    if 'dates' in row.keys():
        temp_dict=row['dates']
        date = safeget(temp_dict,'start','localDate')
        date_time = safeget(temp_dict, 'start', 'dateTime')

    return pd.Series((event_id,
                      event_name,
                      currency,
                      min_price,
                      max_price,
                      segment,
                      genre,
                      date,
                      date_time
                      ))

