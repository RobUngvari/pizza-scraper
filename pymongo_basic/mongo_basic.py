import pymongo
import pandas as pd

create_mongo = True

df = pd.DataFrame({'ticker' : range(10), 'year' : range(10,21)})

if create_mongo:
    host='localhost'
    port=27017
    db='python_import'
    collection='earnings_call_transcript_motley_fool'

    # While no entries added, the new collection doesn't initliaized in database
    client = pymongo.MongoClient(host=host, port=port)
    db = client[db]
    collection = db[collection]
    # db.collection_names() # Function to get the list of all currently existing collcetion underneath db

    # Insert data into database
    for ind, row in df.iterrows():
        grain = {
         'ticker' : row['ticker'],
            'year' : row['year'], }

        collection.insert_one(grain)


def get_data(key):
    """
    get row from database as a dictronary by a lookup key
    """
    ticker_query = { "ticker" : key }
    item = collection.find(ticker_query)
    return item