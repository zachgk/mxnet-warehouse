import pymongo
import random
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
if 'mxWarehouse' in client.list_database_names():
    client.drop_database('mxWarehouse')

db = client.mxWarehouse
components = db.components

new_components = [
        {"name": "resnet-18", "type": "symbol-params", "symbol_url": "https://sample.com/res18-symbol.json", "params_url": "https://sample.com/res18-0000.param", "paper": "http://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html", "tags": ["model", "image", "residual"]},
        {"name": "resnet-50", "type": "symbol-params", "symbol_url": "https://sample.com/res50-symbol.json", "params_url": "https://sample.com/res50-0000.param", "paper": "http://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html","tags": ["model", "image", "residual"]},
        {"name": "resnet-152", "type": "symbol-params", "symbol_url": "https://sample.com/res152-symbol.json", "params_url": "https://sample.com/res152-0000.param", "paper": "http://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html", "tags": ["model", "image", "residual"]},
        {"name": "residualBlock", "type": "symbol-params", "symbol_url": "https://sample.com/resblock-symbol.json", "paper": "http://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html", "tags": ["block"]},
        {"name": "inceptionBlock", "type": "symbol-params", "symbol_url": "https://sample.com/inceptionBlock-symbol.json", "paper": "https://www.cv-foundation.org/openaccess/content_cvpr_2015/html/Szegedy_Going_Deeper_With_2015_CVPR_paper.html", "tags": ["block"]},
        {"name": "relu", "type": "symbol-params", "symbol_url": "https://sample.com/relu.json", "paper": "https://www.cs.toronto.edu/~hinton/absps/reluICML.pdf", "tags": ["operator", "activation"]},
        {"name": "elu", "type": "symbol-params", "symbol_url": "https://sample.com/elu.json", "paper": "https://arxiv.org/abs/1511.07289", "tags": ["operator", "activation"]},
        {"name": "leakyRelu", "type": "symbol-params", "symbol_url": "https://sample.com/leakyRelu.json", "paper": "http://robotics.stanford.edu/~amaas/papers/relu_hybrid_icml2013_final.pdf", "tags": ["operator", "activation"]},
        {"name": "elish", "type": "symbol-params", "symbol_url": "https://sample.com/leakyRelu.json", "paper": "https://arxiv.org/pdf/1808.00783.pdf", "tags": ["operator", "activation"]},
]
for comp in new_components:
    comp['labels'] = ["January", "February", "March", "April", "May", "June", "July"]
    comp['usage'] = [random.randint(1000, 10000)]
    while len(comp['usage']) < len(comp['labels']):
        comp['usage'].append(random.randint(-100, 100) + comp['usage'][-1])

components.insert_many(new_components).inserted_ids
