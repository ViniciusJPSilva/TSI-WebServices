import random
from connection import Client
import json

def run_client() -> None:
    try:
        with Client() as client:
            classes = json.loads(client.receive())
            show_class_json(classes)
            input()
            client.send(json.dumps(select_class_leaders(classes)))

    except ConnectionRefusedError:
        print("\nConexão recusada! Verifique o estado do servidor e tente novamente.\n")

# run_client()

def show_class_json(classes_json) -> None:
    for element_class in classes_json:
        print("Turma {} - {} ({}):".format(element_class["id"],
                                            element_class["name"], 
                                            element_class["year"]))
        for student in element_class["students"]:
            print("\t- {}, {} anos, matrícula {}".format(student["name"],
                                                            student["age"], 
                                                            student["registration"]))
        print("\n")

# show_class_json()

def select_class_leaders(classes_json) -> str:
    selected_leaders = {}
    for element_class in classes_json:
        key = "{} ({})".format(element_class["name"], element_class["id"])
        selected_leaders[key] = {"leader": random.choice(element_class["students"])}
        
    return selected_leaders

# select_class_leaders()

if __name__ == "__main__":
    run_client()