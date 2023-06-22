import json
import yaml
from rdflib import Graph
from rdflib.plugin import register, Serializer
# from rdflib.serializer import Serializer


# Register the JSON-LD serializer
register('json-ld', Serializer, 'rdflib_jsonld.serializer', 'JsonLDSerializer')

def jsonld2turtle(jsonld_file, turtle_file):
    # Create an RDF graph
    graph = Graph()

    # Parse the JSON-LD data into the graph
    graph.parse(jsonld_file, format='json-ld')

    # Serialize the graph to Turtle format
    turtle_data = graph.serialize(format='turtle').encode('utf-8')
    graph.serialize(destination=turtle_file, format='turtle')

    return turtle_data


def turtle2jsonld(turtle_file, jsonld_file):
    # Create an RDF graph
    graph = Graph()

    # Parse the Turtle data into the graph
    graph.parse(turtle_file, format='turtle')

    # Serialize the graph to JSON-LD format
    jsonld_data = graph.serialize(format='json-ld', auto_compact=True, indent=4).encode('utf-8')

    # graph.serialize(destination=jsonld_file, format='json-ld')

    return jsonld_data


def json2yaml(json_file, yaml_file):
    file = open(json_file, 'r')
    python_dict = json.load(file)
    yaml_string = yaml.dump(python_dict)
    print('The YAML file is:')
    print(yaml_string)
    file.close()
    fileOut = open(yaml_file, 'w')
    fileOut.write(yaml_string)
    fileOut.close()


def main():
    json_file = 'input.json'
    yaml_file = 'output.yaml'

    jsonld_file = 'jsonld.json'
    turtle_file = 'turtle.ttl'

    # Convert JSON to YAML
    json2yaml(json_file, yaml_file)

    # Convert JSON-LD to Turtle
    turtle_data = jsonld2turtle(jsonld_file, turtle_file)
    print(turtle_data)

    # Convert Turtle to JSON-LD
    jsonld_data = turtle2jsonld(turtle_file, jsonld_file)
    print(jsonld_data)

if __name__ == '__main__':
    main()


