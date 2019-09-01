import pandas as pd
import pymongo
import json
import os
def import_csvfile(filepath):
    mng_client = pymongo.MongoClient('localhost', 27017)

    # Replace mongo db name
    mng_db = mng_client[input("What DB: ")]

    # Replace mongo db collection name
    collection_name = input("Input collection: ")
    db_cm = mng_db[collection_name]

    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)
    
    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    
    db_cm.remove()
    db_cm.insert(data_json)

if __name__ == "__main__":
    filepath = 'import.csv' # pass csv file path
    import_csvfile(filepath)