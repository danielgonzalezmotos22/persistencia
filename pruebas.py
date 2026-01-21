import json
data_file = "pruebas.json"
with open("./pruebas.json", "r") as f:
    print( json.load(f))

datos = {"id": 123, "nombre": "Jaime"}
with open("./pruebas.json", "w") as f:
    json.dump(datos, f, indent=4)