import os

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

    graph.close()

    return turtle_data

def main():
    input_path = 'jsonld2turtle_data/input/'
    output_path = 'jsonld2turtle_data/output/'

    # get a list of all files in the input dir 'jsonld2turtle_data/input'
    files = os.listdir(input_path)

    for file in files:
        input_file = input_path + file
        output_file = output_path + file[:file.find('.')] + '.ttl'

        # Convert JSON-LD to Turtle
        turtle_data = jsonld2turtle(input_file, output_file)
        print('The input file: ', input_file, ' converted to:\n', turtle_data, '\n------------------------------')


if __name__ == '__main__':
    main()