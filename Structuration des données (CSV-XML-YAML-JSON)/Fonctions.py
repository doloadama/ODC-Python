import csv
import json
import yaml
from xml.etree import ElementTree as ET

def csv_to_json(csv_file):
    """
    Fonction pour convertir un fichier CSV en un fichier JSON

    csv_file: le chemin du fichier CSV
    json_file: le chemin du fichier JSON
    """
    while True:
        json_file = input("Donner le nom que vous voulez donner au fichier JSON sous le format nom.json: ")
        if json_file.endswith('.json'):
            break
        else:
            print("Veuillez ajouter l'extension .json au nom de votre fichier JSON")

    # Ouverture du fichier csv en lecture
    with open(csv_file, encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = [row for row in csv_reader]

    # Write the JSON file
    with open(json_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)
def json_to_csv(json_file, csv_file):
    """
        Fonction pour convertir un fichier JSON en un fichier CSV
        csv_file: le chemin du fichier CSV
        json_file: le chemin du fichier JSON
    """

    with open(json_file, 'r') as json_file:
        data = json.load(json_file)

    with open(csv_file, 'w', newline='') as csv_file:
        # Recuperer les en-tête
        fieldnames = data[0].keys()
        # Creation d'un lecteur qui va gérer l'écriture
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        # Ecriture des en-tête
        csv_writer.writeheader()
        # Ecriture des lignes
        for element in data:
            csv_writer.writerow(element)


def csv_to_yaml(csv_file, yaml_file):
    """
    Fonction pour convertir un fichier CSV en un fichier YAML

    csv_file: le chemin du fichier CSV
    yaml_file: le chemin du fichier YAML
    """
    dict_list = []
    # Ouverture du fichier csv en lecture
    with open(csv_file, 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            dict_list.append(row)

    # Ecriture dans le fichier yaml
    with open(yaml_file, 'w') as yamlfile:
        yaml.dump({'lignes': dict_list}, yamlfile, default_flow_style=False)


def csv_to_xml(csv_file):
    """
        Fonction pour convertir un fichier JSON en un XML CSV
        csv_file: le chemin du fichier CSV
        xml_file: le chemin du fichier XML
    """

    xml_file=input("Donner le nom que vous voulez donner au fichier XML: ")

    #Creer un element root
    root = ET.Element('root')

    with open(csv_file, 'r') as f:
        # Creation du lecteur
        reader = csv.reader(f)

        # Recueillir les en-tête
        header = next(reader)

        #Parcours des lignes
        for row in reader:
            # Creation d'un nouvel élement pour la ligne
            row_element = ET.Element('ligne')

                # Pour chaque cellule de la ligne
            for i, cell in enumerate(row):
                # Creation d'un nouvel élément pour la cellule
                cell_element = ET.Element(header[i])

                # Mettre le texte de la cellule
                cell_element.text = cell

                # Ajouter l'élément de la cellule à l'élément de la ligne
                row_element.append(cell_element)

            # Ajouter l'élément de ligne à l'élément de root
            root.append(row_element)

    # Ecriture du fichier XML
    tree = ET.ElementTree(root)
    tree.write(xml_file+".xml")
