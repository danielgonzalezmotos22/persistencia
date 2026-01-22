import json
import os
data_file = "pruebas.json"
def read(file_path):
    with open(file_path, "r") as f:
        print(json.load(f))

def write(file_path, datos):
    datos = {"id": 123, "nombre": "Jaime"}
    with open(file_path, "w") as f:
        json.dump(datos, f, indent=4)

def update(file_path, data):
    data = {"id": 123,"nombre": "Jaime"}
    for read in file_path["id"]:
        if data == file_path:
            pass

def clear(file_path):
    write(file_path, {})

def delete(file_path):
    os.remove(file_path)
