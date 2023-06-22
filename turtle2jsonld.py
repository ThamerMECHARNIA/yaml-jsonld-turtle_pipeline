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
    jsonld_file = "turtle2jsonld_data/output.jsonld"
    turtle_file = "turtle2jsonld_data/input.ttl"

    # Convert Turtle to JSON-LD
    jsonld_data = turtle2jsonld(turtle_file, jsonld_file)
    print(jsonld_data)

if __name__ == '__main__':
    main()