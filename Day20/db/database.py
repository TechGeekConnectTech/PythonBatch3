import json



def setup_db():
    file_name="students.json"


def get_db(file_name="students.json"):
    with open(file_name,'r') as f:
        return json.load(f)
    
def write_db(data, file_name="students.json"):
    with open(file_name,'w') as f:
        json.dump(data,f,indent=4)
