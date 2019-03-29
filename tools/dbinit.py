import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
if 'mxWarehouse' in client.list_database_names():
    client.drop_database('mxWarehouse')

db = client.mxWarehouse
components = db.components

new_components = [
        {"name": "resnet-18", "type": "symbol-params", "symbol_url": "https://sample.com/res18-symbol.json", "params_url": "https://sample.com/res18-0000.param"},
        {"name": "resnet-50", "type": "symbol-params", "symbol_url": "https://sample.com/res50-symbol.json", "params_url": "https://sample.com/res50-0000.param"},
        {"name": "resnet-152", "type": "symbol-params", "symbol_url": "https://sample.com/res152-symbol.json", "params_url": "https://sample.com/res152-0000.param"},
]
print(components.insert_many(new_components).inserted_ids)
