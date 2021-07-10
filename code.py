
import json
from pathlib import Path
import os.path


f = open("code.json", "r")
file_data = json.loads(f.read())
path = ""

def traverse(data):
    global path
    for directory in data:
        if data[directory]["isDir"]:
            path = path + "/" + directory
            traverse(data[directory]['content'])
        else:
            print(path+"/"+directory)
            content = data[directory]['content']
            Path("qap/"+path).mkdir(parents=True, exist_ok=True)
            
            f = open("qap"+path+"/"+directory, "w+", encoding="utf-8")
            f.write(content)
            f.close()
        path = path.replace("/"+directory, "")

traverse(file_data)