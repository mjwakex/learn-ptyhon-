import json

def parsingJson(filepath):
    with open(filepath, "r") as f:
        obj = json.load(f)
    print(obj) #print all the json contents
    print(obj["name"], "was born in", str(obj["dateOfBirth"]["year"])) #print specific data

def writing(filepath):
    info = {"name": "pandas",
            "version": "2.2.0"}
    with open(filepath, "w") as f:
        json.dumps(info)