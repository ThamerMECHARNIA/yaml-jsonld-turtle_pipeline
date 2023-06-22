from rdflib import Graph

def turtle2jsonld(turtle_file, jsonld_file):
    # Create an RDF graph
    graph = Graph()

    # Parse the Turtle data into the graph
    graph.parse(turtle_file, format='turtle')

    # Serialize the graph to JSON-LD format
    jsonld_data = graph.serialize(format='json-ld', auto_compact=True, indent=4).encode('utf-8')
    graph.serialize(destination=jsonld_file, format='json-ld')

    return jsonld_data



def main():
    jsonld_file = 'jsonld.json'
    turtle_file = 'turtle.ttl'

    # Convert Turtle to JSON-LD
    jsonld_data = turtle2jsonld(turtle_file, jsonld_file)
    print(jsonld_data)

if __name__ == '__main__':
    main()