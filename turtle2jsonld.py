import os

from rdflib import Graph

def turtle2jsonld(turtle_file, jsonld_file):
    # Create an RDF graph
    graph = Graph()

    # Parse the Turtle data into the graph
    graph.parse(turtle_file, format='turtle')

    # Serialize the graph to JSON-LD format
    jsonld_data = graph.serialize(format='json-ld').encode('utf-8')
    graph.serialize(destination=jsonld_file, format='json-ld')

    return jsonld_data



def main():
    input_path = 'turtle2jsonld_data/input/'
    output_path = 'turtle2jsonld_data/output/'

    # get a list of all files in the input dir 'turtle2jsonld_data/input'
    files = os.listdir(input_path)

    for file in files:
        input_file = input_path + file
        output_file = output_path + file[:file.find('.')] + '.jsonld'

        # Convert Turtle to JSON-LD
        jsonld_data = turtle2jsonld(input_file, output_file)
        print('The input file: ', input_file, ' converted to:\n', jsonld_data, '\n------------------------------')


if __name__ == '__main__':
    main()