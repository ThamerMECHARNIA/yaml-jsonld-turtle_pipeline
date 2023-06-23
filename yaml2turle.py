import yaml
from rdflib import Graph, Literal, Namespace, RDF, URIRef

def yaml2turtle(yaml_file, turtle_file):
    # Create an RDF graph
    graph = Graph()

    # Load YAML data
    with open(yaml_file, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)

    # Define the namespace prefixes
    my_ns = Namespace('http://example.com/')
    graph.bind('my', my_ns)

    # Convert YAML data to RDF triples
    for key, value in data.items():
        subject = URIRef(my_ns[key])
        for sub_key, sub_value in value:
            predicate = URIRef(my_ns[sub_key])
            object_ = Literal(sub_value)
            graph.add((subject, predicate, object_))

    # Serialize the graph to Turtle format
    with open(turtle_file, 'w') as turtle_file:
        turtle_file.write(graph.serialize(format='turtle'))

def main():
    # Specify the file paths
    yaml_file = 'yaml2turtle_data/input.yaml'
    turtle_file = 'yaml2turtle_data/output.ttl'

    # Convert YAML to Turtle
    yaml2turtle(yaml_file, turtle_file)

if __name__ == '__main__':
    main()