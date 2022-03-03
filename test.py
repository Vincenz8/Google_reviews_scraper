import pickle
import json
with open("data/raw_reviews/toyota_reviews", "rb") as rev:
    prova = pickle.load(rev)
    
with open("data/prova_conf.json", "r") as read_file:
    data = json.load(read_file)
    
print(data.keys())