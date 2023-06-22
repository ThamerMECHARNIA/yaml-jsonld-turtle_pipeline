from rdflib import Graph
from rdflib.plugin import register, Serializer

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

def main():
    jsonld_file = 'input.jsonld'
    turtle_file = 'output.ttl'

    # Convert JSON-LD to Turtle
    turtle_data = jsonld2turtle(jsonld_file, turtle_file)
    print(turtle_data)


if __name__ == '__main__':
    main()